# MindTest 心理测评站

免费在线心理健康测评平台，支持 SCL-90、PHQ-9、GAD-7、MBTI、压力指数、睡眠质量等多款心理测评。

## 项目结构

```
mindtest-shop/
├── index.html          # 首页（测试列表）
├── scl90.html          # SCL-90 症状自评量表
├── phq9.html           # PHQ-9 抑郁自评量表
├── gad7.html           # GAD-7 焦虑自评量表
├── mbti.html           # MBTI 人格类型测试
├── stress.html         # 压力指数测评
├── sleep.html          # 睡眠质量测评 (PSQI)
├── css/
│   └── style.css       # 全站样式
├── js/
│   ├── tests.js        # 所有测试数据和评分逻辑
│   └── main.js         # 主程序逻辑
└── images/             # 图片资源目录
```

## 功能特性

- ✅ 6 款心理测评，覆盖抑郁/焦虑/人格/压力/睡眠
- ✅ 纯前端实现，无需后端，部署简单
- ✅ 完全匿名，数据不上传
- ✅ 即时出分，附带专业解读
- ✅ 暗色主题，视觉舒适
- ✅ 响应式设计，移动端友好
- ✅ 预留 Adsterra 广告位（每个测试页底部）

## 部署方式

直接上传到服务器即可，无需任何编译步骤。支持：
- GitHub Pages
- Netlify
- Vercel
- 任何静态网站托管服务

## Adsterra 广告接入

在每个 `.html` 文件中的 `<div class="ad-placeholder">` 处替换为 Adsterra 代码：

```html
<!-- Adsterra Native Banner -->
<script type="text/javascript">
  atTeamRun();
</script>
<script src="//cdn.adsterra.com/team/team.js" async="async"></script>
```

推荐位置：
1. 测试页底部（已有占位符）
2. 结果页顶部
3. 首页侧边栏（后续扩展）

## 下一步

- [ ] 接入 Adsterra 广告代码
- [ ] 添加更多测评（MBTI完整版、职业倦怠等）
- [ ] 增加博客/科普文章页面
- [ ] SEO优化（sitemap、meta标签）
- [ ] 添加分享功能（微信/QQ）
- [ ] 考虑添加用户登录记录历史（可选）
