#!/usr/bin/env python3
"""Inspect local media without changing it. Requires ffmpeg and ffprobe on PATH."""
import argparse
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys


def call(args):
    return subprocess.run(args, capture_output=True, text=True, check=True).stdout


def positive(value):
    number = float(value)
    if number <= 0:
        raise argparse.ArgumentTypeError('must be greater than zero')
    return number


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('file', type=Path)
    parser.add_argument('--fps', type=positive, help='expected constant frame rate; omit for VFR')
    parser.add_argument('--frames', type=int, help='expected decoded video-frame count')
    parser.add_argument('--duration', type=positive, help='expected video duration in seconds')
    args = parser.parse_args()
    if not args.file.is_file():
        parser.error('input must be a local regular file')
    if args.frames is not None and args.frames <= 0:
        parser.error('--frames must be greater than zero')
    if not all(shutil.which(name) for name in ['ffprobe', 'ffmpeg']):
        parser.error('ffprobe and ffmpeg must be installed on PATH')
    file = str(args.file.resolve())
    probe = json.loads(call(['ffprobe', '-v', 'error', '-count_frames', '-show_streams',
                             '-show_format', '-of', 'json', file]))
    videos = [s for s in probe['streams'] if s.get('codec_type') == 'video']
    if not videos:
        parser.error('no video stream found')
    video = videos[0]
    raw_frames = json.loads(call(['ffprobe', '-v', 'error', '-select_streams', 'v:0',
                                  '-show_frames', '-show_entries',
                                  'frame=pts_time,best_effort_timestamp_time', '-of', 'json', file]))['frames']
    timestamps = [float(f['pts_time']) for f in raw_frames if 'pts_time' in f]
    inferred_count = sum('best_effort_timestamp_time' in f for f in raw_frames)
    deltas = [b - a for a, b in zip(timestamps, timestamps[1:])]
    complete_pts = len(timestamps) == len(raw_frames)
    monotonic = complete_pts and bool(timestamps) and all(d > 0 for d in deltas)
    duration = float(video.get('duration') or probe['format']['duration'])
    fps_text = video.get('avg_frame_rate', '0/1')
    fps = float(Fraction(fps_text)) if fps_text != '0/0' else 0
    decode = subprocess.run(['ffmpeg', '-hide_banner', '-v', 'error', '-xerror', '-i', file,
                              '-map', '0:v:0', '-map', '0:a?', '-f', 'null', '-'],
                             capture_output=True, text=True)
    # Strict decode: do not silently ignore ffmpeg errors even when its exit status is zero.
    decode_ok = decode.returncode == 0 and not decode.stderr.strip()
    checks = {'complete_decode': decode_ok, 'frame_pts_complete': complete_pts,
              'frame_pts_strictly_increasing': monotonic}
    if args.frames is not None:
        checks['expected_frame_count'] = len(raw_frames) == args.frames
    if args.duration is not None:
        tolerance = max(0.002, 1 / (args.fps or fps or 30))
        checks['expected_duration'] = abs(duration - args.duration) <= tolerance
    if args.fps is not None:
        # ffprobe timestamp strings are rounded, so allow a few microseconds.
        step = 1 / args.fps
        tolerance = max(0.000005, step * 0.001)
        checks['expected_cfr_rate'] = abs(fps - args.fps) <= args.fps * 0.0001
        checks['constant_frame_spacing'] = bool(deltas) and all(abs(d - step) <= tolerance for d in deltas)
    digest = hashlib.sha256()
    with args.file.open('rb') as handle:
        for chunk in iter(lambda: handle.read(1048576), b''):
            digest.update(chunk)
    result = {
        'file_name': args.file.name, 'bytes': args.file.stat().st_size,
        'sha256': digest.hexdigest(), 'width': video['width'], 'height': video['height'],
        'video_duration_seconds': duration, 'average_fps': fps,
        'video_frame_count': len(raw_frames),
        'frames_with_pts': len(timestamps),
        'frames_with_best_effort_time': inferred_count,
        'first_pts_seconds': timestamps[0] if timestamps else None,
        'audio_streams': [{k: s.get(k) for k in ['codec_name', 'sample_rate', 'channels', 'duration']}
                          for s in probe['streams'] if s.get('codec_type') == 'audio'],
        'checks': checks, 'passed': all(checks.values()),
        'not_checked': ['visual_similarity', 'normal_speed_playback', 'subjective_audio',
                        'audio_video_sync', 'loudness', 'clipping', 'source_or_asset_rights']
    }
    if not decode_ok:
        result['decode_error'] = decode.stderr.strip()[:2000]
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return 0 if result['passed'] else 1


if __name__ == '__main__':
    try:
        sys.exit(main())
    except (subprocess.CalledProcessError, ValueError, KeyError) as error:
        print('Media inspection failed: ' + str(error), file=sys.stderr)
        sys.exit(2)
