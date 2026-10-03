# 15 秒复杂动效复刻案例

参考作品：Daryl Patigas / @darel023。

- [原作](https://x.com/darel023/status/2103424524297420829)
- [公开案例页](https://jasonzhu.ai/en/prompts/claude-opus-5-5/2103424524297420829)
- [本例材料、迭代和复现边界](../skills/recreate-motion-from-reference/references/case-daryl-r2.md)
- [重新整理的复用提示词](../skills/recreate-motion-from-reference/references/reusable-prompts.md)

## 产物规格

1. R2 复刻：15 秒、1280×720、60fps、900 帧，Native Canvas + FFmpeg。该版本获得本次制作发起者认可。并非已核实的官方 Remotion 导出。
2. 左右同步对比：15 秒、1920×628、60fps、900 帧；左原作、右 R2，两侧完整画幅，无重定时，仅使用 R2 的一条音轨。

[R2 复刻视频](../media/complex-showreel-r2.mp4) · [左右对比](../media/complex-side-by-side.mp4)。原片未单独上传。对比左侧画面权利属于原作者，不提供第三方转授权；音乐与文件说明见 [媒体说明](../media/README.md)。

## 参考与迭代

原视频实际用于测量事件边界、构图、字体比例、真实停顿、逐字遮罩和对象衔接。制作经历多轮代码修正，不是只靠一个简短 prompt 一次生成。粒子形态、拖尾、光照和局部时序仍有差异。

## 验收状态

已做完整解码、时长/帧数与连续时间戳检查，查看编码后的关键阶段联系表及片尾。制作侧未完成正常速度全片连续观看和主观听音验证；这些限制不会被用户认可或技术检查覆盖。

安装 Skill 可复用这套分析与修正方式；本仓库不含此视频的完整渲染工程，不能一键复现字节完全相同的 R2。
