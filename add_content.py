#!/usr/bin/env python3
"""Add substantial content to test pages for AdSense approval."""

import os
import re

PROJECT_DIR = r"C:\Users\Sen\WorkBuddy\2026-09-09-20-09-37\mindtest-shop"

# Content to add BEFORE the disclaimer (after the test-header div)
# Format: (test_key, zh_content, en_content)

CONTENT_INJECT = {
    "scl90": """
  <!-- Test Description -->
  <div class="test-content-section">
    <h2 data-i18n="scl90_intro_title">关于 SCL-90 症状自评量表</h2>
    <p data-i18n="scl90_intro_p1">SCL-90（Symptom Checklist 90），又称症状自检表，是由 Derogatis 于 1975 年编制的心理健康评定量表，是目前国内外最广泛使用的心理健康筛查工具之一。该量表包含 90 个项目，涵盖广泛的精神症状学内容，能够全面评估个体在近期的心理感受和行为表现。</p>
    <p data-i18n="scl90_intro_p2">SCL-90 共包括 9 个分量表：躯体化（反映身体不适感）、强迫症状（指明知没有必要但无法摆脱的无意义想法或冲动）、人际关系敏感（人际不自在和自卑感）、抑郁（苦闷情感与生活质量降低）、焦虑（烦躁与紧张）、敌对（愤怒与攻击倾向）、恐怖（对特定场所或物体的恐惧）、偏执（猜疑和被动体验）以及精神病性（各种幻觉、妄想等精神症状）。此外，还有一个反映饮食睡眠情况的附加项目。</p>
    <p data-i18n="scl90_intro_p3">本量表采用 5 级评分制：1=没有，2=很轻，3=中等，4=偏重，5=严重。总分越高表明心理问题越严重。一般认为总分超过 160 分或阳性项目数超过 43 项时，需要进一步检查。每个因子分在 2 分以上提示可能存在该领域的心理问题，建议寻求专业心理咨询师的帮助。</p>
    <p data-i18n="scl90_intro_p4">本测试仅供自我探索参考，不能替代专业心理诊断。如果您对测试结果有疑问或感到困扰，建议咨询专业的心理咨询师或精神科医生。</p>
  </div>

  <!-- Result Interpretation -->
  <div class="test-content-section">
    <h2 data-i18n="scl90_result_title">SCL-90 结果解读指南</h2>
    <p data-i18n="scl90_result_p1">SCL-90 的评估结果通常从总分、阳性项目数和因子分三个维度进行分析。总分反映整体心理健康状况，范围在 90-450 分之间；阳性项目数指评分在 2 分及以上的项目数量；因子分则是各维度得分的平均值。</p>
    <p data-i18n="scl90_result_p2">一般来说，总分低于 160 分、阳性项目数少于 43 项、各因子分均低于 2 分，可认为心理健康状况良好。若总分在 160-200 分之间，或某些因子分在 2-3 分之间，提示存在轻度心理问题，建议关注自身情绪状态，适当调节生活方式。若总分超过 200 分或因子分超过 3 分，则可能提示中重度心理问题，建议及时寻求专业帮助。</p>
    <p data-i18n="scl90_result_p3">需要注意的是，SCL-90 的结果受多种因素影响，包括当时的情绪状态、生活环境变化等。因此，测试结果应作为参考而非诊断依据。如果持续感到心理困扰，建议进行多次测评并咨询专业人士。</p>
  </div>
""",
    "phq9": """
  <!-- Test Description -->
  <div class="test-content-section">
    <h2 data-i18n="phq9_intro_title">关于 PHQ-9 抑郁自评量表</h2>
    <p data-i18n="phq9_intro_p1">PHQ-9（Patient Health Questionnaire-9，患者健康问卷-9项）是由 Spitzer 等人基于 DSM-IV 诊断标准开发的抑郁症筛查工具。它涵盖了抑郁症诊断标准中的 9 个核心症状，包括兴趣减退、情绪低落、睡眠障碍、疲劳乏力、食欲改变、自我评价过低、注意力难以集中、行动迟缓以及自杀意念。</p>
    <p data-i18n="phq9_intro_p2">PHQ-9 自 2001 年发布以来，已被翻译成多种语言，在全球范围内得到了广泛应用和验证。多项研究表明，PHQ-9 具有良好的信度和效度，能够快速、准确地筛查出可能存在抑郁问题的个体。它被美国预防服务工作组（USPSTF）推荐为抑郁症筛查的首选工具之一。</p>
    <p data-i18n="phq9_intro_p3">本测试采用 4 级评分：0=完全没有，1=有几天，2=一半以上的天数，3=几乎每天。总分范围 0-27 分，分数越高表示抑郁症状越严重。PHQ-9 不仅能筛查抑郁，其总分变化还可以用于评估治疗效果。</p>
    <p data-i18n="phq9_intro_p4">本测试仅供自我探索参考，不能替代专业诊断。如果您在测试中发现了问题或有自杀念头，请立即联系专业人士或拨打心理援助热线。</p>
  </div>

  <!-- Result Interpretation -->
  <div class="test-content-section">
    <h2 data-i18n="phq9_result_title">PHQ-9 结果解读指南</h2>
    <p data-i18n="phq9_result_p1">PHQ-9 的评分标准如下：0-4 分为无明显抑郁；5-9 分为轻度抑郁；10-14 分为中度抑郁；15-19 分为中重度抑郁；20-27 分为重度抑郁。研究表明，评分≥10 分可以作为进一步临床评估的阈值。</p>
    <p data-i18n="phq9_result_p2">轻度抑郁（5-9分）可能表现为偶尔的情绪低落、兴趣下降，通常通过自我调节、运动、社交等方式可以缓解。中度抑郁（10-14分）建议寻求心理咨询师的帮助，进行专业的认知行为治疗或接受必要的支持。</p>
    <p data-i18n="phq9_result_p3">中重度及重度抑郁（≥15分）可能需要药物治疗配合心理治疗。如果您在这个分数段，请务必认真对待，及时寻求专业帮助。抑郁是可以治疗的，许多人在获得适当治疗后都能恢复健康。</p>
    <p data-i18n="phq9_result_p4">请记住，PHQ-9 只是一个筛查工具，最终诊断需要由专业医生通过面谈和评估来确定。测试结果仅供参考，不应作为自我诊断的唯一依据。</p>
  </div>
""",
    "gad7": """
  <!-- Test Description -->
  <div class="test-content-section">
    <h2 data-i18n="gad7_intro_title">关于 GAD-7 焦虑自评量表</h2>
    <p data-i18n="gad7_intro_p1">GAD-7（Generalized Anxiety Disorder-7，广泛性焦虑量表-7项）是由 Spitzer 等人开发的焦虑障碍筛查工具。它基于 DSM-IV 中广泛性焦虑障碍的诊断标准，包括 7 个核心症状： nervosidade/ansiedade（紧张不安）、não conseguir relaxar（无法放松）、muito nervoso（非常紧张）、medo de algo horrível acontecer（害怕可怕的事情发生）、inquietude/agitação（坐立不安）、dificuldade para relaxar（难以放松）以及 dificuldade para se concentrar（难以集中注意力）。</p>
    <p data-i18n="gad7_intro_p2">GAD-7 已被广泛研究并证明具有良好的心理测量特性。它的开发目的是为临床医生提供一个快速、简便的焦虑筛查工具。研究显示，GAD-7 对广泛性焦虑障碍的筛查敏感度约为 82%，特异度约为 79%，是一个可靠的初筛工具。</p>
    <p data-i18n="gad7_intro_p3">本测试采用 4 级评分：0=完全没有，1=有几天，2=一半以上的天数，3=几乎每天。总分范围 0-21 分，分数越高表示焦虑症状越严重。GAD-7 不仅适用于广泛性焦虑障碍的筛查，也可用于其他焦虑障碍的初步评估。</p>
    <p data-i18n="gad7_intro_p4">本测试仅供自我探索参考，不能替代专业诊断。如果您感到焦虑严重影响日常生活，建议寻求专业心理咨询师的帮助。</p>
  </div>

  <!-- Result Interpretation -->
  <div class="test-content-section">
    <h2 data-i18n="gad7_result_title">GAD-7 结果解读指南</h2>
    <p data-i18n="gad7_result_p1">GAD-7 的评分标准如下：0-4 分为无明显焦虑；5-9 分为轻度焦虑；10-14 分为中度焦虑；15-21 分为重度焦虑。通常认为评分≥10 分提示可能存在焦虑障碍，需要进一步评估。</p>
    <p data-i18n="gad7_result_p2">轻度焦虑（5-9分）可能是暂时性的情绪反应，通常与特定的压力事件相关。通过调整生活方式、进行放松训练、保持规律运动等措施，很多情况下可以得到缓解。</p>
    <p data-i18n="gad7_result_p3">中度焦虑（10-14分）建议进行专业的心理评估和干预。认知行为疗法（CBT）对焦虑障碍有明确的疗效，必要时也可以考虑药物治疗。焦虑是可以治疗的，不必过度担忧。</p>
    <p data-i18n="gad7_result_p4">重度焦虑（≥15分）需要高度重视，建议尽快寻求专业帮助。持续的严重焦虑可能影响身体健康和日常生活质量。请记住，寻求帮助是勇敢的表现，专业的支持可以帮助您走出困境。</p>
  </div>
""",
    "mbti": """
  <!-- Test Description -->
  <div class="test-content-section">
    <h2 data-i18n="mbti_intro_title">关于 MBTI 人格类型测试</h2>
    <p data-i18n="mbti_intro_p1">MBTI（Myers-Briggs Type Indicator，迈尔斯-布里格斯类型指标）是根据心理学家卡尔·荣格的心理学类型理论发展而来的人格测评工具。由 Katharine Cook Briggs 和她的女儿 Isabel Briggs Myers 在 20 世纪 40 年代编制，是目前全球最流行的人格测评工具之一。</p>
    <p data-i18n="mbti_intro_p2">MBTI 从四个维度将人格分为 16 种类型：能量来源（外向 E vs 内向 I）、信息获取（实感 S vs 直觉 N）、决策方式（思考 T vs 情感 F）以及生活态度（判断 J vs 感知 P）。每个维度代表一个人偏好的认知风格，组合起来形成独特的人格类型。</p>
    <p data-i18n="mbti_intro_p3">了解自己是 MBTI 测试的核心目的。不同人格类型的人在沟通方式、决策模式、压力反应等方面存在差异。MBTI 帮助人们认识自己的优势和挑战，改善人际关系，选择适合的职业方向，并促进个人成长。</p>
    <p data-i18n="mbti_intro_p4">请注意，MBTI 描述的是偏好而非能力，每个人都在四个维度上有一定的灵活性。结果仅供参考，人格类型不应成为限制自己发展的标签。每个人都有潜能发展自己较弱的功能。</p>
  </div>

  <!-- Result Interpretation -->
  <div class="test-content-section">
    <h2 data-i18n="mbti_result_title">MBTI 人格类型解读</h2>
    <p data-i18n="mbti_result_p1">MBTI 将人格分为 16 种类型，可分为四大类：分析型（NT）、理想主义者（NF）、护卫者（SJ）和传统者（SP）。每种类型都有其独特的优势和潜在的挑战。</p>
    <p data-i18n="mbti_result_p2">分析型（INTJ、INTP、ENTJ、ENTP）善于策略思考和创新，适合科学研究和战略规划工作。理想主义者（INFJ、INFP、ENFJ、ENFP）重视价值观和人际关系，适合教育、咨询和人道主义领域。护卫者（ISTJ、ISFJ、ESTJ、ESFJ）注重秩序和责任，适合管理和执行工作。传统者（ISTP、ISFP、ESTP、ESFP）擅长实际操作和应对突发情况，适合技术和创意领域。</p>
    <p data-i18n="mbti_result_p3">了解自己的 MBTI 类型可以帮助您更好地认识自己，发挥优势，同时有意识地发展自己较弱的功能。但请记住，人格类型只是一个工具，不应该限制您对未来的想象。每个人都有成长和改变的能力。</p>
  </div>
""",
    "stress": """
  <!-- Test Description -->
  <div class="test-content-section">
    <h2 data-i18n="stress_intro_title">关于压力指数测评</h2>
    <p data-i18n="stress_intro_p1">压力是现代社会普遍存在的问题。适度的压力可以激发潜能、提高工作效率，但长期过大的压力会对身心健康造成严重损害。研究表明，持续的高压状态可能导致焦虑、抑郁、心血管疾病、免疫力下降等多种健康问题。</p>
    <p data-i18n="stress_intro_p2">本测试基于 Perceived Stress Scale（PSS，感知压力量表）的设计理念，评估您在过去一个月中感受到的压力程度。压力并非仅仅是外部事件的客观描述，而是个体对压力的主观感受和应对能力的综合评估。同一个事件对不同人可能产生截然不同的压力体验。</p>
    <p data-i18n="stress_intro_p3">了解自身的压力水平是有效管理压力的第一步。本测试帮助您识别当前压力水平，发现可能的压力来源，从而采取针对性的减压措施。无论是工作压力、学习压力还是生活压力，都有科学有效的应对方法。</p>
    <p data-i18n="stress_intro_p4">本测试仅供自我探索参考，不能替代专业诊断。如果您感到压力严重影响了日常生活，建议寻求心理咨询师的帮助，学习专业的压力管理技巧。</p>
  </div>

  <!-- Result Interpretation -->
  <div class="test-content-section">
    <h2 data-i18n="stress_result_title">压力管理建议</h2>
    <p data-i18n="stress_result_p1">压力管理是一个系统性的过程，需要从多个角度入手。以下是一些经过科学验证的减压方法：规律运动（每周 3-5 次，每次 30 分钟以上）、正念冥想（每天 10-15 分钟）、充足的睡眠（每晚 7-8 小时）、健康饮食、社交支持以及时间管理。</p>
    <p data-i18n="stress_result_p2">轻度压力（0-15分）通常可以通过自我调节得到缓解。建议您保持健康的生活方式，学会时间管理，合理安排工作和休息。尝试每天给自己留出一些放松的时间，进行深呼吸、冥想或简单的伸展运动。</p>
    <p data-i18n="stress_result_p3">中度压力（16-25分）可能需要更系统的管理策略。除了上述方法外，建议建立明确的工作边界，学会说"不"，培养兴趣爱好，保持与亲友的联系。考虑学习专业的压力管理课程或参加减压工作坊。</p>
    <p data-i18n="stress_result_p4">重度及极度压力（≥26分）需要认真对待。持续的高压状态可能导致身心健康问题。建议您寻求专业心理咨询师的帮助，学习专业的应对技巧。同时，考虑调整当前的生活或工作模式，寻找压力的根本原因并加以解决。</p>
  </div>
""",
    "sleep": """
  <!-- Test Description -->
  <div class="test-content-section">
    <h2 data-i18n="sleep_intro_title">关于睡眠质量测评（PSQI）</h2>
    <p data-i18n="sleep_intro_p1">睡眠质量对身心健康至关重要。世界卫生组织（WHO）指出，睡眠是维护身体健康的第一要素。良好的睡眠有助于身体修复、记忆巩固、情绪调节和免疫功能维持。相反，长期睡眠质量差可能导致多种健康问题，包括心血管疾病、糖尿病、肥胖和心理健康问题。</p>
    <p data-i18n="sleep_intro_p2">PSQI（Pittsburgh Sleep Quality Index，匹兹堡睡眠质量指数）是由 Buysse 等人于 1989 年开发的睡眠质量评估工具。它从主观睡眠质量、入睡时间、睡眠时间、睡眠效率、睡眠障碍、催眠药物使用和日间功能障碍 7 个方面评估睡眠质量，总分范围为 0-21 分。</p>
    <p data-i18n="sleep_intro_p3">研究表明，PSQI 总分大于 5 分提示睡眠质量差。中国常模显示，约 37.8% 的成年人存在睡眠质量差的问题。不良睡眠不仅影响白天的工作和学习效率，长期还会增加患病风险。</p>
    <p data-i18n="sleep_intro_p4">本测试仅供自我探索参考，不能替代专业诊断。如果您长期存在睡眠问题，建议咨询睡眠专科医生或心理治疗师。</p>
  </div>

  <!-- Result Interpretation -->
  <div class="test-content-section">
    <h2 data-i18n="sleep_result_title">改善睡眠的建议</h2>
    <p data-i18n="sleep_result_p1">改善睡眠质量可以从以下几个方面入手：建立规律的作息时间，每天尽量在同一时间入睡和起床；优化睡眠环境，保持卧室安静、黑暗和凉爽；睡前避免使用电子设备，蓝光会抑制褪黑素分泌；晚餐不宜过饱，睡前避免摄入咖啡因和酒精。</p>
    <p data-i18n="sleep_result_p2">良好睡眠的基础是规律作息。建议每天在固定时间入睡和起床，即使在周末也保持相似的作息。睡前 1 小时开始"睡前仪式"，如阅读、冥想或温水浴，帮助身体进入睡眠状态。</p>
    <p data-i18n="sleep_result_p3">睡前环境也很重要。理想的卧室温度约为 18-22°C，使用遮光窗帘或眼罩阻挡光线，必要时使用耳塞或白噪音机减少噪音干扰。床只用于睡眠和亲密行为，不要在床上工作或看电视。</p>
    <p data-i18n="sleep_result_p4">如果自我调节效果不佳，建议咨询睡眠专科医生。可能需要进一步的睡眠监测或专业的睡眠治疗。记住，良好的睡眠是健康生活的基础，值得投入时间和精力去改善。</p>
  </div>
""",
}

def inject_content(html_path, test_key):
    """Inject content section into test page."""
    with open(html_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the test-header closing div and insert after it
    # Look for the pattern: </div>\n\n  <div class="disclaimer"
    target = '</div>\n\n  <div class="disclaimer"'
    if target not in content:
        target = '</div>\n\n  <div class="disclaimer'
        # Try without \n\n
        target = '</div>\n<div class="disclaimer"'

    if target not in content:
        print(f"  Warning: Could not find insertion point in {html_path}")
        return False

    new_content = content.replace(target, target + CONTENT_INJECT[test_key], 1)

    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(new_content)

    print(f"  ✓ Updated {html_path}")
    return True

def main():
    test_files = {
        "scl90": "scl90.html",
        "phq9": "phq9.html",
        "gad7": "gad7.html",
        "mbti": "mbti.html",
        "stress": "stress.html",
        "sleep": "sleep.html",
    }

    updated = []
    for key, filename in test_files.items():
        filepath = os.path.join(PROJECT_DIR, filename)
        if os.path.exists(filepath):
            print(f"Updating {filename}...")
            if inject_content(filepath, key):
                updated.append(filename)

    if updated:
        print(f"\n✓ Updated {len(updated)} files: {', '.join(updated)}")
        print("\nNext step: Update cache-busting version and commit.")
    else:
        print("\n✗ No files were updated.")

if __name__ == "__main__":
    main()
