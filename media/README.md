# 视频、制作方式与署名

## 直接看结果

点击进入 GitHub 文件页；若网页没有播放器，点 **Raw / Download raw file** 获取 MP4，再用浏览器或本地播放器观看。README 里的普通链接不等于内嵌播放器。

- [简单 UI 复刻 v4](simple-ui-v4.mp4)：14 秒，1440×1440，60fps，840 帧，约 6.3MB。
- [复杂动效复刻 R2](complex-showreel-r2.mp4)：15 秒，1280×720，60fps，900 帧，约 3.7MB。
- [复杂动效左右同步对比](complex-side-by-side.mp4)：15 秒，1920×628，60fps，900 帧，约 6.5MB；左原作、右 R2。
- [Stephan 复杂形变复刻](stephan-showreel-replica.mp4)：15 秒，1280×720，60fps，900 帧，约 5.1MB，含自写程序合成配乐。
- [Stephan 左右同步对比（静音）](stephan-side-by-side-silent.mp4)：15 秒，2560×768，60fps，900 帧，约 8.0MB；左原作、右复刻。

## 谁做的，用了什么

这三条复刻由 GPT/dot 根据参考视频写代码，并经历多轮修改。现有制作记录没有保留可以核实的 GPT 精确模型版本，因此不写猜测的型号。

原作收录在 Claude Opus 5.5 案例页面中，那说的是原作者的案例，不能拿来当作本次复刻使用的模型证明。画面里保留的 Claude 字样也是参考作品的视觉内容。

- 简单 UI v4：已通过 Remotion 4.0.532 正式导出，视频文件确已生成。
- 复杂 R2：当时没有取得并核实可交付的正式 Remotion 输出；本页提供的是用 Native Canvas + FFmpeg 实际渲染的 MP4。“正式 Remotion 输出未核实”不等于“完全没渲染视频”。
- Daryl 对比：左右同一起点、无重定时；只使用 R2 的一条音轨，没有叠加原片音轨。
- Stephan 复刻：Native Canvas + FFmpeg，独立代码重建；15 秒配乐为本次程序合成，无第三方或原曲采样。
- Stephan 对比：左右从 PTS 0 同步、无变速、无运动插帧；静音。

技术检查包括完整解码、时长、帧数与时间戳；制作侧没有完成正常速度全片连续观看及主观听音验收。复杂 R2 的粒子、拖尾和部分细节仍有差异。

## 视频不适用整包 MIT

这些视频是复刻学习与比较案例。仓库 MIT 只覆盖原创代码和原创文档；视频中的第三方视觉设计、字体、标识与音乐各有自己的权利边界，不因随仓库发布而被重新授权。

原片未单独上传。两条对比视频左侧分别包含 Daryl 和 Stephan 的原作画面，用于展示复刻差异；其再使用权仍归原权利人，本仓库不代为授予再发布或商业使用权。没有原作者或配乐作者背书。

## 简单 UI v4

参考作者：zero / @twoclipping。
- 原作：https://x.com/twoclipping/status/2103273003555402193
- 案例页：https://jasonzhu.ai/en/prompts/claude-opus-5-5/2103273003555402193

本片画面为独立代码实现，未直接拼接原片画面或原片音乐。

音乐：“Protofunk” — Kevin MacLeod（[Incompetech](https://incompetech.com/)）。Guitar: Dan Ritter。
- 来源：https://incompetech.com/music/royalty-free/index.html?isrc=USUAN1100103
- 许可：CC BY 4.0，https://creativecommons.org/licenses/by/4.0/
- 修改：截取原曲 16.974131–30.974131 秒，调整音量并加入淡入淡出；保留原速、原调及 113 BPM。

音效（CC0）：Kenney Interface Sounds / UI Audio / Impact Sounds；Brian MacIntosh（BMacZero）Bubble Sound Effects；EZduzziteh Pop Sounds；artisticdude Swishes Sound Pack。
- https://kenney.nl/assets/interface-sounds
- https://kenney.nl/assets/ui-audio
- https://kenney.nl/assets/impact-sounds
- https://opengameart.org/content/bubble-sound-effects
- https://opengameart.org/content/pop-sounds-0
- https://opengameart.org/content/swishes-sound-pack

字体：Geist by Vercel，SIL Open Font License 1.1。

## 复杂 R2 及其对比视频

参考作者：Daryl Patigas / @darel023。
- 原作：https://x.com/darel023/status/2103424524297420829
- 案例页：https://jasonzhu.ai/en/prompts/claude-opus-5-5/2103424524297420829

音乐：“Enter the Party” — Kevin MacLeod（[Incompetech](https://incompetech.com/)）。
- 来源：https://incompetech.com/music/royalty-free/index.html?isrc=USUAN1100240
- 许可：CC BY 4.0，https://creativecommons.org/licenses/by/4.0/
- 修改：截取并剪成 15 秒，120→128 BPM 保调变速，调整响度、加淡化及 CC0 音效。对比视频直接沿用 R2 音轨。

音效（CC0）：artisticdude Swishes、EZduzziteh Pop Sounds、Kenney Interface Sounds、JaggedStone Magic Spell SFX。
- https://opengameart.org/content/swishes-sound-pack
- https://opengameart.org/content/pop-sounds-0
- https://kenney.nl/assets/interface-sounds
- https://opengameart.org/content/magic-spell-sfx

字体：Inter Tight、Instrument Serif Italic、Liberation Mono，原工程保留对应 SIL OFL 1.1 许可。此目录不单独分发字体文件。

## Stephan 复杂形变及其静音对比

参考作者：Stephan Livera / @stephanlivera。
- 原作：https://x.com/stephanlivera/status/2103315922098470926
- 案例页：https://jasonzhu.ai/en/prompts/claude-opus-5-5/2103315922098470926
- [公开制作记录与剩余差异](../examples/stephan-showreel.md)

本片用 Native Canvas JavaScript 重建画面，FFmpeg 编码。没有拿原作栅格帧当成片纹理，没有原作者源码。画面的 CLAUDE 字样是参考设计的一部分，不表示这条复刻由 Opus 原生生成。

音乐为本次用振荡器、包络和固定种子噪声合成的 15 秒替换声轨，没有第三方音乐或原片音频采样。它不是原作音乐的复刻。新对比文件静音，没有原片音轨。

字体：Inter Tight（900 字重实例）、Instrument Serif Italic、Liberation Mono，按 SIL OFL 1.1 使用。字体文件不在本仓库单独分发。

成片和对比已获本次发起者审核认可；仍保留字体、曲线场相位、点阵表面、相机和模糊等近似。制作侧没有完成正常速度全片连续播放和主观听音评价。原创实现和新配乐不会改变原作视觉设计的权利归属，视频不整体纳入 MIT。

## 文件校验

发布文件与此前验收附件字节一致，SHA-256：

```text
9ca0edfd65e0dfa830f8aa0e4617db0f438fb3989bcc2848e8f05d75603eb07c  simple-ui-v4.mp4
634b2c098f9da483c8046bd5786473a2c3740072c81fef4e89945165c48195ba  complex-showreel-r2.mp4
e80c31f6a5db537e9b20a35d89c8dfa68d4598f77a4e2e252d6963e67e9a77b8  complex-side-by-side.mp4
799a8ddf19e62654251fc2dcca2cb56c956fb32fdf38df15f57bac220a245c45  stephan-showreel-replica.mp4
779c50bb1064f7c5e0900e311bf02bc0ec5a1129835c2ffaf36447c9e6fa00cf  stephan-side-by-side-silent.mp4
```

旧视频元数据中可能保留“预览/私人研究/正式导出待验证”等制作当时的文字；当前制作方式与检查范围以上面的说明为准。发布文件未重新压缩或重配音乐。分享现有视频时请同时保留本页对应音乐署名与修改说明。
