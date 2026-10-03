# 参考视频动效复刻 Skill

把一条参考视频拆成可测量的节奏、构图和对象关系，再用代码重建、逐段对比、检查导出。

适合想让 AI 做参考复刻、动效练习、或者修正现有复刻的人。包含可复用提示词和一个 15 秒复杂动效案例。本仓库提供方法和检查工具，不含该案例的一键渲染源工程，也不承诺一次生成或像素一致。

## 先看视频

- [简单 UI 复刻，14 秒](media/simple-ui-v4.mp4)
- [复杂动效复刻，15 秒](media/complex-showreel-r2.mp4)
- [复杂动效左右同步对比](media/complex-side-by-side.mp4)

链接进入 GitHub 文件页；没有播放器时点 **Raw / Download raw file** 下载观看。视频制作说明、文件校验与完整音乐署名在 [media/README.md](media/README.md)。

## 谁做的，渲染到了哪一步

由 GPT/dot 按参考视频写代码并多轮修改；制作记录没有保留可核实的 GPT 精确型号。原作页面写的 Claude Opus 5.5 属于原作者案例，不能当作这次复刻的模型说明。

简单 UI v4 已用 Remotion 4.0.532 正式导出。复杂 R2 当时未取得并核实正式 Remotion 输出，当前给出的 MP4 是 Native Canvas + FFmpeg 真正渲染出来的，不能说成“完全没渲染”。

## 它会做什么

- 从真实视频提取带时间的事件表，区分静止、变速、错峰、遮罩与相机运动
- 在转场中保留对象身份，让曲线和点、按钮和通知、柱阵和粒子共用连续状态
- 先修节奏与因果关系，再修形状、字体、光照和质感
- 制作同时间轴左右比较，明确音轨来源与剩余差异
- 用实际成片检查尺寸、时长、帧数、时间戳和解码，而非只看源码

## 安装

需要 Node.js 和 npm。使用 [Vercel 的 Skills CLI](https://github.com/vercel-labs/skills)，在你想使用 Skill 的项目目录运行：

```sh
npx --yes skills add suanrongbaicai/recreate-motion-from-reference --skill recreate-motion-from-reference --agent codex --copy -y
```

这是项目范围安装，不会修改全局 Skill。其他 Agent 可用交互式选择：

```sh
npx skills add suanrongbaicai/recreate-motion-from-reference
```

不安装也可以：打开 [SKILL.md](skills/recreate-motion-from-reference/SKILL.md)，把它作为任务指导，连同可访问的参考视频发给你的 Agent。使用哪个模型、编辑器或渲染器，由当前任务和可用环境决定。

## 怎么调用

```text
请使用 recreate-motion-from-reference 复刻这个视频：[附件或原作链接]。
输出：[尺寸、时长、帧率、格式]。
我最在意：[节奏／转场关系／排版／其他验收点]。
先分析真实参考，再实现连续骨架；逐段对比后导出。
保留可编辑工程，说明使用工具、近似部分和没有完成的检查。
```

更多分阶段指令见 [复用提示词](skills/recreate-motion-from-reference/references/reusable-prompts.md)。这些是整理后的模板，不是原作者提示词或历史会话的逐字复制。

## 实例

[案例介绍与输出规格](examples/daryl-r2.md)：根据 [Daryl Patigas 的原作](https://x.com/darel023/status/2103424524297420829) 制作的 15 秒 R2 复刻，包含曲线、排版、界面、图表、立体柱阵、粒子和片尾。

实际复刻视频采用 Native Canvas + FFmpeg，1280×720、60fps、900 帧。配乐使用另外取得许可的音乐。左右对比为 1920×628、15 秒，左原作、右复刻，保持原时间轴。粒子质感等仍有可见差异。

本仓库附两条复刻与一条左右对比，不单独上传原片。对比左侧包含原作画面，相关权利仍归原作者；视频不整体套用 MIT。案例的参考作用、实际迭代和复现边界见 [详细记录](skills/recreate-motion-from-reference/references/case-daryl-r2.md)。

## 导出检查

需要 Python 3.9+、FFmpeg 和 ffprobe。检查脚本不联网、不修改输入文件：

```sh
python3 skills/recreate-motion-from-reference/scripts/check_video.py ./output.mp4 --fps 60 --frames 900 --duration 15 > ./checks.json
```

将参数换成当前项目要求。对可变帧率参考省略 `--fps`；比较时按实际呈现时间对齐，不能直接用帧号除以标称帧率。脚本不判断审美、音乐听感、音画同步或版权。更多说明见 [使用与验证](skills/recreate-motion-from-reference/references/checking-and-use.md)。

## 验证范围

已完成：Skill 结构检查、脚本正反例回归、案例导出参数检查、三个边界场景的独立静态审查。安装验证记录见 [验证说明](VALIDATION.md)。

没有从头用这个新 Skill 完成独立留出视频的端到端验证；案例认可也不等于所有画面、声音和工具路线都已经验收。欢迎通过 Issue 提供具体时间段、实际偏差与可复现材料。

## 目录

```text
skills/recreate-motion-from-reference/
  SKILL.md
  references/                 工作方法、案例、署名与验证说明
  scripts/check_video.py      本地导出检查
examples/daryl-r2.md          案例入口
media/                       两条复刻、左右对比及音乐署名
LICENSE                      原创内容的 MIT 许可
THIRD_PARTY_NOTICES.md        第三方内容与许可边界
```

## 许可与署名

本仓库原创代码和原创文档采用 [MIT](LICENSE)。第三方作品、提示词短引、字体、音乐、商标和外链内容不因出现在本仓库中而获得 MIT 授权，详见 [第三方声明](THIRD_PARTY_NOTICES.md)。

原作：Daryl Patigas / [@darel023](https://x.com/darel023/status/2103424524297420829)。本项目是独立复刻方法总结，没有原作者源码或背书。若公开你制作的视频，请另外核对其中所有素材的使用权并保留必要署名。
