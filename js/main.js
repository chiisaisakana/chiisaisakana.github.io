// Main app logic
(function() {
  'use strict';

  function init() {
    var path = window.location.pathname.split('/').pop() || 'index.html';
    var testKey = path.replace('.html', '');
    var test = window.TESTS[testKey];

    if (!test) return;

    var i18n = window.I18N[window.CURRENT_LANG] || {};
    var translatedOptions = i18n[testKey + '_options'] || test.options;
    var answers = [];
    var currentQ = 0;
    var questions = window.I18N[window.CURRENT_LANG] ? test.questionsList.map(function(q, i) { return { text: q.text, options: window.I18N[window.CURRENT_LANG][testKey + '_options'] }; }) : test.questionsList;
    var options = translatedOptions;

    var container = document.getElementById('questions-container');
    if (!container) return;

    function renderQuestion() {
      var q = questions[currentQ];

      container.innerHTML = '<div class="question-block">' +
        '<div class="question-num">第 ' + (currentQ + 1) + ' 题 / 共 ' + questions.length + ' 题</div>' +
        '<div class="question-text">' + (i18n[testKey + '_questions'] && i18n[testKey + '_questions'][currentQ] ? i18n[testKey + '_questions'][currentQ] : q.text) + '</div>' +
        '<div class="options"></div>' +
      '</div>';

      var optionsDiv = container.querySelector('.options');
      options.forEach(function(opt, j) {
        var label = document.createElement('label');
        label.className = 'option-label';
        var isSelected = answers[currentQ] === j;

        var input = document.createElement('input');
        input.type = 'radio';
        input.name = 'q';
        input.value = j;
        input.checked = isSelected;

        var radio = document.createElement('span');
        radio.className = 'radio';

        var optionText = document.createElement('span');
        optionText.className = 'option-text';
        optionText.textContent = translatedOptions[j] || opt;

        label.appendChild(input);
        label.appendChild(radio);
        label.appendChild(optionText);
        optionsDiv.appendChild(label);

        label.addEventListener('click', function(e) {
          e.stopPropagation();
          e.preventDefault();
          answers[currentQ] = j;
          currentQ++;
          updateProgress();
          if (currentQ >= questions.length) {
            showResult();
          } else {
            renderQuestion();
            (adsbygoogle = window.adsbygoogle || []).push({});
          }
        });
      });
    }

    function updateProgress() {
      var answered = answers.filter(function(a) { return a !== -1; }).length;
      var pct = (answered / questions.length) * 100;
      var fill = document.getElementById('progress-fill');
      var text = document.getElementById('progress-text');
      if (fill) fill.style.width = pct + '%';
      if (text) text.textContent = (i18n['answered'] || '已回答') + ' ' + answered + '/' + questions.length + (i18n['of'] || '题');
    }

    function showResult() {
      var score = 0;
      for (var k = 0; k < answers.length; k++) {
        score += answers[k];
      }
      var maxScore = questions.length * (options.length - 1);
      var level = test.scoring.level(score);

      var resultHtml = '<div class="result-page">';
      resultHtml += '<div class="result-card">';
      resultHtml += '<div class="test-icon">' + test.icon + '</div>';
      resultHtml += '<h2>' + test.title + '</h2>';
      resultHtml += '<div class="result-score">' + score + '</div>';
      resultHtml += '<div class="result-level ' + level.cls + '">' + level.text + '</div>';
      resultHtml += '<div class="result-desc">';
      resultHtml += '满分 ' + maxScore + ' 分 | 得分率 ' + ((score / maxScore) * 100).toFixed(1) + '%';
      resultHtml += '</div></div>';

      if (test.dimensions && test.dimensions.length > 1) {
        resultHtml += '<div class="result-card"><h3>各维度分析</h3><div class="factor-grid">';
        test.dimensions.forEach(function(dim) {
          var dimScore = score;
          var dimLevel = test.scoring.level(dimScore);
          var dimPercent = (dimScore / maxScore) * 100;
          var barColor = dimLevel.cls === 'level-normal' ? '#22c55e' :
                        dimLevel.cls === 'level-mild' ? '#f59e0b' : '#ef4444';
          resultHtml += '<div class="factor-item">';
          resultHtml += '<div class="factor-name">' + dim + '</div>';
          resultHtml += '<div class="factor-score" style="color:' + barColor + '">' + dimScore + '</div>';
          resultHtml += '<div class="factor-bar"><div class="factor-bar-fill" style="width:' + dimPercent + '%;background:' + barColor + '"></div></div>';
          resultHtml += '</div>';
        });
        resultHtml += '</div></div>';
      }

      resultHtml += '<div class="ad-placeholder"><ins class="adsbygoogle" style="display:block" data-ad-client="ca-pub-4116656020104879" data-ad-slot="4402557622"></ins></div>';
      resultHtml += '<div class="result-actions">';
      resultHtml += '<a href="index.html" class="btn btn-primary">返回首页</a>';
      resultHtml += '<button class="btn btn-secondary" onclick="location.reload()">重新测评</button>';
      resultHtml += '</div>';
      resultHtml += '<div class="disclaimer" style="margin-top:24px">⚠️ 本测试结果仅供参考，不构成医疗诊断。如检测到严重心理问题，请及时咨询专业心理咨询师或就医。</div>';
      resultHtml += '</div>';

      document.body.innerHTML = resultHtml;
      (adsbygoogle = window.adsbygoogle || []).push({});
    }

    // Start first question
    renderQuestion();
    (adsbygoogle = window.adsbygoogle || []).push({});
    updateProgress();
  }

  
  // Apply i18n translations
  function applyTranslations() {
    var elements = document.querySelectorAll('[data-i18n]');
    elements.forEach(function(el) {
      var key = el.getAttribute('data-i18n');
      var translations = window.I18N[window.CURRENT_LANG];
      if (translations && translations[key]) {
        var value = translations[key];
        // Handle array values by joining with ' · '
        if (Array.isArray(value)) {
          value = value.join(' · ');
        }
        if (el.tagName === 'INPUT' || el.tagName === 'TEXTAREA') {
          el.placeholder = value;
        } else {
          el.innerHTML = value;
        }
      }
    });

    // Update lang buttons
    document.getElementById('lang-zh').classList.toggle('active', window.CURRENT_LANG === 'zh');
    document.getElementById('lang-en').classList.toggle('active', window.CURRENT_LANG === 'en');
  }
  
  // Apply on load
  applyTranslations();

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
