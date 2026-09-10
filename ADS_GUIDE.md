# Adsterra 广告接入指南

## 快速开始

1. 登录 [Adsterra Publisher Dashboard](https://beta.publishers.adsterra.com/stats)
2. 进入 "Manage Placements" → "Create Placement"
3. 选择广告格式，复制生成的代码
4. 将代码替换到对应 HTML 文件的 `.ad-placeholder` 位置

---

## 推荐广告格式（按优先级）

| 格式 | 代码示例 | 适合位置 | eCPM 范围 |
|------|---------|---------|-----------|
| **Native Banner** | 见下方 | 测评页顶部/结果页 | $2-8 |
| **In-Page Push** | 见下方 | 结果页中部 | $3-10 |
| **Social Bar** | 见下方 | 全站右下角 | $1-5 |
| **Interstitial** | 见下方 | PC端侧边栏 | $2-6 |

---

## 各页面广告位置标注

### 1. SCL-90 页面 (`scl90.html`)

```html
<!-- 广告位 1: 测评说明下方，题目上方 -->
<div class="ad-placeholder" id="ad-top-banner">
  <!-- 替换为 Native Banner 代码 -->
  📢 广告位 · 支持我们继续提供免费服务
</div>

<div id="questions-container"></div>

<!-- 广告位 2: 提交按钮下方 -->
<div class="ad-placeholder" id="ad-bottom-banner">
  <!-- 替换为 In-Page Push 代码 -->
  📢 广告位 · 支持我们继续提供免费服务
</div>
```

### 2. PHQ-9 页面 (`phq9.html`)

```html
<!-- 广告位 1: 页面顶部，标题下方 -->
<div class="ad-placeholder" id="ad-top-banner">
  <!-- 替换为 Native Banner 代码 -->
</div>

<div id="questions-container"></div>

<!-- 广告位 2: 结果页（JS 动态生成） -->
<div class="ad-placeholder">
  <!-- 替换为 In-Page Push 代码 -->
</div>
```

### 3. GAD-7 页面 (`gad7.html`)

```html
<!-- 广告位 1: 测评说明下方 -->
<div class="ad-placeholder" id="ad-top-banner">
  <!-- 替换为 Native Banner 代码 -->
</div>

<div id="questions-container"></div>

<!-- 广告位 2: 提交按钮下方 -->
<div class="ad-placeholder" id="ad-bottom-banner">
  <!-- 替换为 In-Page Push 代码 -->
</div>
```

### 4. MBTI 页面 (`mbti.html`)

```html
<!-- 广告位 1: 页面顶部 -->
<div class="ad-placeholder" id="ad-top-banner">
  <!-- 替换为 Native Banner 代码 -->
</div>

<div id="questions-container"></div>

<!-- 广告位 2: 结果页 -->
<div class="ad-placeholder">
  <!-- 替换为 In-Page Push 代码 -->
</div>
```

### 5. 压力指数页面 (`stress.html`)

```html
<!-- 广告位 1: 页面顶部 -->
<div class="ad-placeholder" id="ad-top-banner">
  <!-- 替换为 Native Banner 代码 -->
</div>

<div id="questions-container"></div>

<!-- 广告位 2: 提交按钮下方 -->
<div class="ad-placeholder" id="ad-bottom-banner">
  <!-- 替换为 In-Page Push 代码 -->
</div>
```

### 6. 睡眠测评页面 (`sleep.html`)

```html
<!-- 广告位 1: 页面顶部 -->
<div class="ad-placeholder" id="ad-top-banner">
  <!-- 替换为 Native Banner 代码 -->
</div>

<div id="questions-container"></div>

<!-- 广告位 2: 提交按钮下方 -->
<div class="ad-placeholder" id="ad-bottom-banner">
  <!-- 替换为 In-Page Push 代码 -->
</div>
```

### 7. 首页 (`index.html`)

```html
<!-- 广告位: 测试列表下方 -->
<div class="ad-placeholder" id="ad-home-banner">
  <!-- 替换为 Native Banner 代码 -->
</div>
```

---

## 广告代码模板

### Native Banner (推荐首选)

```html
<!-- Adsterra Native Banner -->
<script type="text/javascript">
  atTeamRun();
</script>
<script src="//cdn.adsterra.com/team/team.js" async="async"></script>
```

**Placement ID**: 在 Adsterra 后台创建时获取，格式如 `12345678`

**完整代码示例**:
```html
<div id="ad-native-banner" style="margin: 20px 0;">
  <script type="text/javascript">
    var atteam = atteam || [];
    atteam.push({'id': 12345678, 'mode': 'in-feed'});
    (function(d, s, id) {
      var js, t = d.createElement(s);
      t.type = 'text/javascript';
      t.id = id;
      t.async = true;
      t.src = '//cdn.adsterra.com/team/team.js';
      var sct = d.getElementsByTagName(s)[0];
      sct.parentNode.insertBefore(t, sct);
    })(document, 'script', 'adsterra-team-js');
  </script>
</div>
```

### In-Page Push

```html
<!-- Adsterra In-Page Push -->
<script type="text/javascript">
  var atinv = atinv || [];
  atinv.push({'id': 12345678, 'mode': 'in-page-push'});
  (function(d, s, id) {
    var js, t = d.createElement(s);
    t.type = 'text/javascript';
    t.id = id;
    t.async = true;
    t.src = '//cdn.adsterra.com/team/team.js';
    var sct = d.getElementsByTagName(s)[0];
    sct.parentNode.insertBefore(t, sct);
  })(document, 'script', 'adsterra-inpage-js');
</script>
```

### Social Bar

```html
<!-- Adsterra Social Bar (放在 footer 前) -->
<script type="text/javascript">
  var atbar = atbar || [];
  atbar.push({'id': 12345678, 'mode': 'social-bar'});
  (function(d, s, id) {
    var js, t = d.createElement(s);
    t.type = 'text/javascript';
    t.id = id;
    t.async = true;
    t.src = '//cdn.adsterra.com/team/team.js';
    var sct = d.getElementsByTagName(s)[0];
    sct.parentNode.insertBefore(t, sct);
  })(document, 'script', 'adsterra-social-bar-js');
</script>
```

---

## 接入步骤

1. **创建 Placement**
   - 登录 Adsterra → Manage Placements → Create Placement
   - 选择格式（建议先选 Native Banner）
   - 设置名称如 "MindTest-Top-Banner"
   - 复制 Placement ID

2. **替换占位符**
   - 打开对应 HTML 文件
   - 找到 `<div class="ad-placeholder" id="ad-xxx">`
   - 删除占位符内容，粘贴广告代码
   - 把 `12345678` 替换为你的真实 Placement ID

3. **设置 Auto-fill（可选）**
   - 在 Adsterra 后台开启 "Auto-fill" 功能
   - 这样广告会自动填充，无需手动维护多个 Placement

4. **测试验证**
   - 刷新页面，确认广告正常显示
   - 检查是否有控制台报错

---

## 注意事项

### 合规提醒
- 心理测评站用户心智偏敏感，**避免 Popunder 和强制弹窗**
- 广告内容选择"教育/健康/工具类"，避免博彩/成人/虚假医疗广告
- 用户举报可能导致账户被封

### 性能优化
- 使用 `async` 加载广告脚本，避免阻塞页面渲染
- 限制每页广告数量：最多 3 个（Top + Mid + Bottom）
- 移动端可以只保留 1-2 个广告位

### 收入优化
- **GAD-7 和 PHQ-9** 搜索量最大，优先放在核心位置
- **SCL-90** 题目多、停留时间长，适合放更多广告位
- **MBTI** 传播性强，用户会分享结果，适合 Social Bar
- 不同时段切换不同广告格式，观察哪个 eCPM 最高

---

## 预期收入估算

| 日访问量 | 广告曝光 | 预估 eCPM | 日收入 |
|---------|---------|----------|--------|
| 100 | 300 | $3 | $0.90 |
| 500 | 1500 | $4 | $6.00 |
| 1000 | 3000 | $5 | $15.00 |
| 5000 | 15000 | $6 | $90.00 |
| 10000 | 30000 | $7 | $210.00 |

*注：实际收入取决于流量质量、Geo 分布、季节因素*

---

## 下一步

1. ✅ 网站已搭建完成，6 个测试页面可正常运行
2. ⏳ 接入 Adsterra 广告代码
3. ⏳ 部署到 `mindtest.shop`
4. ⏳ 推广引流（小红书/知乎）
5. ⏳ 优化广告位布局，提升 eCPM
