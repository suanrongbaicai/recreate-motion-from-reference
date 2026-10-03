# 验证说明

2026-10-03 初版：

- Skill 结构、资源引用及未完成占位检查通过。
- 原 R2 文件检查：15.000 秒、1280×720、60fps、900 帧，完整解码及解码帧 PTS 连续性通过。
- 检查脚本回归：错误帧率/时长/帧数返回 1；缺失文件返回 2；未指定恒帧率要求时正常检查。
- 独立静态情境审查覆盖：原作无法访问、可变帧率参考与 60fps 输出比较、第三方素材错误套 MIT。

这些是结构与工具测试，不是新 Skill 在独立留出视频上的端到端效果证明。

## 远端安装实测

2026-10-03，Linux / Node.js 24.19.0 / npm 11.9.0 / Skills CLI 1.7.0。
从 GitHub 的公开 main 分支安装，测试时对应提交 `1aef01014494776f7827feb00db973662adcbded`。

```sh
npx --yes skills add suanrongbaicai/recreate-motion-from-reference --skill recreate-motion-from-reference --agent codex --copy -y
```

结果：发现 1 个 Skill，项目范围复制安装成功。安装到隔离测试项目的 8 个文件全部与发布源的 SHA-256 一致，包括 SKILL.md、4 个 references 文件、检查脚本及两份许可声明。安装后的检查脚本再次检查 R2 成片通过。

测试使用隔离的项目、HOME 与 npm 缓存，关闭 CLI 遥测，没有修改用户全局安装，没有创建新凭据。其他 Agent 的实际安装与端到端视频效果尚未验证。本仓库当前未配置 GitHub Actions，不能把这次测试描述成 CI 通过。


## 公开视频核验

2026-10-03，三条已指定 MP4 上传至 media/。随后从公开仓库重新克隆提交 `89310a9ab6b7455e834e096807fab997e61736aa`，三文件大小及 SHA-256 全部与此前已交付版本一致。校验值见 media/README.md。

GitHub 的大文件页面提供 Raw / Download raw file 入口；这里提供的是文件链接，不声明 README 内嵌播放。视频没有重压缩或重配音乐。

## 新增 Stephan 案例

2026-10-03，经发起者审核认可后加入 Stephan 15 秒复刻及静音左右对比。两文件的完整解码、60fps、900 帧及呈现时间戳检查通过；复刻含 1 条音轨，对比不含音轨。上传后 GitHub 返回的两个 blob SHA 与本地 Git 对象校验值完全相同。

本轮仅新增案例、媒体和署名登记，没有更改 SKILL.md 主规则，也不把此认可表述为新 Skill 已完成独立留出任务验证。
