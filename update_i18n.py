#!/usr/bin/env python3
import re

i18n_path = "C:/Users/Sen/WorkBuddy/2026-09-09-20-09-37/mindtest-shop/js/i18n.js"
with open(i18n_path, 'r', encoding='utf-8') as f:
    content = f.read()

# First, remove the incorrectly placed PHQ-9 English content from Chinese section
bad_phq9_en_chunk = """
    // PHQ-9 Content
    'phq9_intro_title': 'About the PHQ-9 Depression Screening',
    'phq9_intro_p1': 'The PHQ-9 (Patient Health Questionnaire-9) was developed by Spitzer et al. based on DSM-IV diagnostic criteria. It covers 9 core symptoms of depression, including reduced interest, low mood, sleep disturbances, fatigue, appetite changes, low self-esteem, difficulty concentrating, psychomotor retardation, and suicidal ideation.',
    'phq9_intro_p2': 'Since its publication in 2001, PHQ-9 has been translated into multiple languages and widely used and validated globally. Multiple studies have shown that PHQ-9 has good reliability and validity, and can quickly and accurately screen individuals who may have depression. It is recommended by the US Preventive Services Task Force (USPSTF) as one of the preferred tools for depression screening.',
    'phq9_intro_p3': 'This test uses a 4-point rating: 0=not at all, 1=several days, 2=more than half the days, 3=nearly every day. Total score ranges from 0-27, with higher scores indicating more severe depression symptoms. PHQ-9 can not only screen for depression, but changes in total score can also be used to assess treatment effectiveness.',
    'phq9_intro_p4': 'This test is for self-exploration reference only and does not replace professional diagnosis. If you find problems or have suicidal thoughts in the test, please contact a professional immediately or call a psychological assistance hotline.',
    'phq9_result_title': 'PHQ-9 Result Interpretation Guide',
    'phq9_result_p1': 'The PHQ-9 scoring criteria are as follows: 0-4 points indicate no significant depression; 5-9 points indicate mild depression; 10-14 points indicate moderate depression; 15-19 points indicate moderately severe depression; 20-27 points indicate severe depression. Studies show that a score ≥10 can serve as a threshold for further clinical assessment.',
    'phq9_result_p2': 'Mild depression (5-9 points) may manifest as occasional low mood or decreased interest, which can usually be relieved through self-regulation, exercise, and social activities. Moderate depression (10-14 points) suggests seeking help from a counselor for professional cognitive behavioral therapy or necessary support.',
    'phq9_result_p3': 'Moderate to severe and severe depression (≥15 points) may require medication combined with psychotherapy. If you are in this score range, please take it seriously and seek professional help promptly. Depression is treatable, and many people recover with appropriate treatment.',
    'phq9_result_p4': 'Please remember that PHQ-9 is only a screening tool, and final diagnosis needs to be determined by a professional doctor through interview and assessment. Test results are for reference only and should not be the sole basis for self-diagnosis.',
"""

if bad_phq9_en_chunk in content:
    content = content.replace(bad_phq9_en_chunk, '\n', 1)
    print("✓ Removed incorrectly placed PHQ-9 English from Chinese section")
else:
    print("✗ Could not find PHQ-9 English chunk to remove")

# Now add GAD-7 Chinese after phq9_result_p4 in Chinese section
gad7_zh = """    // GAD-7 Content
    'gad7_intro_title': '关于 GAD-7 焦虑自评量表',
    'gad7_intro_p1': 'GAD-7（Generalized Anxiety Disorder-7，广泛性焦虑量表-7项）是由 Spitzer 等人开发的焦虑障碍筛查工具。它基于 DSM-IV 中广泛性焦虑障碍的诊断标准，包括 7 个核心症状：紧张不安、无法放松、非常紧张、害怕可怕的事情发生、坐立不安、难以放松以及难以集中注意力。',
    'gad7_intro_p2': 'GAD-7 已被广泛研究并证明具有良好的心理测量特性。它的开发目的是为临床医生提供一个快速、简便的焦虑筛查工具。研究显示，GAD-7 对广泛性焦虑障碍的筛查敏感度约为 82%，特异度约为 79%，是一个可靠的初筛工具。',
    'gad7_intro_p3': '本测试采用 4 级评分：0=完全没有，1=有几天，2=一半以上的天数，3=几乎每天。总分范围 0-21 分，分数越高表示焦虑症状越严重。GAD-7 不仅适用于广泛性焦虑障碍的筛查，也可用于其他焦虑障碍的初步评估。',
    'gad7_intro_p4': '本测试仅供自我探索参考，不能替代专业诊断。如果您感到焦虑严重影响日常生活，建议寻求专业心理咨询师的帮助。',
    'gad7_result_title': 'GAD-7 结果解读指南',
    'gad7_result_p1': 'GAD-7 的评分标准如下：0-4 分为无明显焦虑；5-9 分为轻度焦虑；10-14 分为中度焦虑；15-21 分为重度焦虑。通常认为评分≥10 分提示可能存在焦虑障碍，需要进一步评估。',
    'gad7_result_p2': '轻度焦虑（5-9分）可能是暂时性的情绪反应，通常与特定的压力事件相关。通过调整生活方式、进行放松训练、保持规律运动等措施，很多情况下可以得到缓解。',
    'gad7_result_p3': '中度焦虑（10-14分）建议进行专业的心理评估和干预。认知行为疗法（CBT）对焦虑障碍有明确的疗效，必要时也可以考虑药物治疗。焦虑是可以治疗的，不必过度担忧。',
    'gad7_result_p4': '重度焦虑（≥15分）需要高度重视，建议尽快寻求专业帮助。持续的严重焦虑可能影响身体健康和日常生活质量。请记住，寻求帮助是勇敢的表现，专业的支持可以帮助您走出困境。',
"""

zh_marker = "'phq9_result_p4': '请记住，PHQ-9 只是一个筛查工具，最终诊断需要由专业医生通过面谈和评估来确定。测试结果仅供参考，不应作为自我诊断的唯一依据。',"
if zh_marker in content:
    content = content.replace(zh_marker, zh_marker + "\n" + gad7_zh, 1)
    print("✓ Added GAD-7 Chinese translations")
else:
    print("✗ Could not find insertion point for GAD-7 Chinese")

# Now add GAD-7 English after phq9_result_p4 in English section
gad7_en = """    // GAD-7 Content
    'gad7_intro_title': 'About the GAD-7 Anxiety Scale',
    'gad7_intro_p1': 'The GAD-7 (Generalized Anxiety Disorder-7) was developed by Spitzer et al. as an anxiety disorder screening tool. Based on DSM-IV criteria for generalized anxiety disorder, it includes 7 core symptoms: feeling nervous/anxious, inability to relax, feeling so restless it is hard to sit still, being easily annoyed or irritable, feeling afraid as if something awful might happen, having difficulty relaxing, and having difficulty concentrating.',
    'gad7_intro_p2': 'GAD-7 has been extensively studied and proven to have good psychometric properties. Its development aimed to provide clinicians with a quick and convenient anxiety screening tool. Research shows that GAD-7 has a sensitivity of approximately 82% and specificity of approximately 79% for screening generalized anxiety disorder, making it a reliable initial screening tool.',
    'gad7_intro_p3': 'This test uses a 4-point rating: 0=not at all, 1=several days, 2=more than half the days, 3=nearly every day. Total score ranges from 0-21, with higher scores indicating more severe anxiety symptoms. GAD-7 is applicable not only to generalized anxiety disorder screening but also to preliminary assessment of other anxiety disorders.',
    'gad7_intro_p4': 'This test is for self-exploration reference only and does not replace professional diagnosis. If you feel anxiety severely affects your daily life, please seek help from a professional counselor.',
    'gad7_result_title': 'GAD-7 Result Interpretation Guide',
    'gad7_result_p1': 'The GAD-7 scoring criteria are as follows: 0-4 points indicate no significant anxiety; 5-9 points indicate mild anxiety; 10-14 points indicate moderate anxiety; 15-21 points indicate severe anxiety. Generally, a score >=10 suggests possible anxiety disorder requiring further assessment.',
    'gad7_result_p2': 'Mild anxiety (5-9 points) may be a temporary emotional response, often related to specific stress events. Through lifestyle adjustments, relaxation training, regular exercise, and other measures, it can often be alleviated.',
    'gad7_result_p3': 'Moderate anxiety (10-14 points) suggests seeking professional psychological assessment and intervention. Cognitive Behavioral Therapy (CBT) has proven efficacy for anxiety disorders, and medication may also be considered if necessary. Anxiety is treatable, so there is no need for excessive worry.',
    'gad7_result_p4': 'Severe anxiety (>=15 points) requires serious attention, and prompt professional help is recommended. Persistent severe anxiety may affect physical health and quality of daily life. Please remember that seeking help is a brave act, and professional support can help you overcome difficulties.',
"""

en_marker = "'phq9_result_p4': 'Please remember that PHQ-9 is only a screening tool, and final diagnosis needs to be determined by a professional doctor through interview and assessment. Test results are for reference only and should not be the sole basis for self-diagnosis.',"
if en_marker in content:
    content = content.replace(en_marker, en_marker + "\n" + gad7_en, 1)
    print("✓ Added GAD-7 English translations")
else:
    print("✗ Could not find insertion point for GAD-7 English")

# Also add Stress and Sleep content translations
stress_zh = """    // Stress Content
    'stress_intro_title': '关于压力指数测评',
    'stress_intro_p1': '压力是现代人普遍面临的问题。适度的压力可以激发潜能、提高效率，但长期过大的压力会对身心健康造成严重损害。本测试基于感知压力量表（PSS）的设计理念，帮助您评估近一个月的压力水平。',
    'stress_intro_p2': '压力反应因人而异，同一事件对不同人可能产生截然不同的压力体验。了解自身的压力水平和应对方式，是有效管理压力的第一步。',
    'stress_intro_p3': '本测试包含 10 道题目，采用 5 级评分：0=从不，1=偶尔，2=有时，3=经常，4=总是。总分范围 0-40 分，分数越高表示压力水平越高。',
    'stress_intro_p4': '本测试仅供自我探索参考，不能替代专业诊断。如果您感到压力严重影响日常生活，建议寻求专业心理咨询师的帮助。',
    'stress_result_title': '压力指数结果解读',
    'stress_result_p1': '压力指数评分标准：0-15 分为轻度压力，16-25 分为中度压力，26-40 分为重度压力。轻度压力通常可以通过自我调节缓解，中重度压力建议寻求专业帮助。',
    'stress_result_p2': '轻度压力（0-15分）：这是正常的压力反应，通常与特定的生活事件相关。建议保持健康的生活方式，学会放松技巧，如深呼吸、冥想、瑜伽等。',
    'stress_result_p3': '中度压力（16-25分）：建议您开始关注压力管理，学习专业的减压技巧。可以考虑进行心理咨询，学习认知行为疗法（CBT）等有效方法。',
    'stress_result_p4': '重度压力（>=26分）：建议您尽快寻求专业帮助。持续的严重压力可能导致焦虑、抑郁、心血管疾病等多种健康问题。请记住，寻求帮助是勇敢的表现。',
"""

stress_en = """    // Stress Content
    'stress_intro_title': 'About Stress Index Assessment',
    'stress_intro_p1': 'Stress is a common problem in modern life. Moderate stress can stimulate potential and improve efficiency, but long-term excessive stress can cause serious damage to physical and mental health. This test is based on the design concept of the Perceived Stress Scale (PSS) to help you assess your stress level in the past month.',
    'stress_intro_p2': 'Stress responses vary from person to person. The same event may produce completely different stress experiences for different people. Understanding your own stress level and coping methods is the first step to effectively managing stress.',
    'stress_intro_p3': 'This test contains 10 questions with a 5-point rating: 0=never, 1=rarely, 2=sometimes, 3=often, 4=very often. Total score ranges from 0-40, with higher scores indicating higher stress levels.',
    'stress_intro_p4': 'This test is for self-exploration reference only and does not replace professional diagnosis. If you feel stress seriously affects your daily life, please seek help from a professional counselor.',
    'stress_result_title': 'Stress Index Result Interpretation',
    'stress_result_p1': 'Stress index scoring criteria: 0-15 points indicates mild stress, 16-25 points indicates moderate stress, 26-40 points indicates severe stress. Mild stress can usually be relieved through self-regulation, while moderate to severe stress is recommended to seek professional help.',
    'stress_result_p2': 'Mild stress (0-15 points): This is a normal stress response, usually related to specific life events. It is recommended to maintain a healthy lifestyle and learn relaxation techniques such as deep breathing, meditation, yoga, etc.',
    'stress_result_p3': 'Moderate stress (16-25 points): It is recommended that you start paying attention to stress management and learn professional stress reduction techniques. You may consider psychological counseling and learn effective methods such as Cognitive Behavioral Therapy (CBT).',
    'stress_result_p4': 'Severe stress (>=26 points): It is recommended that you seek professional help as soon as possible. Persistent severe stress may lead to various health problems such as anxiety, depression, and cardiovascular diseases. Please remember that seeking help is a brave act.',
"""

sleep_zh = """    // Sleep Content
    'sleep_intro_title': '关于睡眠质量测评（PSQI）',
    'sleep_intro_p1': '睡眠质量对身心健康至关重要。世界卫生组织（WHO）指出，睡眠是维护身体健康的第一要素。良好的睡眠有助于身体修复、记忆巩固、情绪调节和免疫功能维持。相反，长期睡眠质量差可能导致多种健康问题，包括心血管疾病、糖尿病、肥胖和心理健康问题。',
    'sleep_intro_p2': 'PSQI（Pittsburgh Sleep Quality Index，匹兹堡睡眠质量指数）是由 Buysse 等人于 1989 年开发的睡眠质量评估工具。它从主观睡眠质量、入睡时间、睡眠时间、睡眠效率、睡眠障碍、催眠药物使用和日间功能障碍 7 个方面评估睡眠质量，总分范围为 0-21 分。',
    'sleep_intro_p3': '研究表明，PSQI 总分大于 5 分提示睡眠质量差。中国常模显示，约 37.8% 的成年人存在睡眠质量差的问题。不良睡眠不仅影响白天的工作和学习效率，长期还会增加患病风险。',
    'sleep_intro_p4': '本测试仅供自我探索参考，不能替代专业诊断。如果您长期存在睡眠问题，建议咨询睡眠专科医生或心理治疗师。',
    'sleep_result_title': '睡眠质量结果解读',
    'sleep_result_p1': 'PSQI 评分标准：0-5 分为睡眠质量好，6-10 分为轻度睡眠问题，11-15 分为中度睡眠问题，16-21 分为重度睡眠问题。总分>=5 分提示睡眠质量差，需要关注。',
    'sleep_result_p2': '轻度睡眠问题（6-10分）：建议调整睡眠习惯，如固定作息时间、避免睡前使用电子设备、保持卧室安静黑暗等。可以通过改善睡眠卫生来缓解。',
    'sleep_result_p3': '中度睡眠问题（11-15分）：建议寻求专业帮助，进行睡眠认知行为疗法（CBT-I）。同时注意排除潜在的生理或心理因素，如焦虑、抑郁、睡眠呼吸暂停等。',
    'sleep_result_p4': '重度睡眠问题（>=16分）：建议尽快就医，进行专业的睡眠监测和评估。严重的睡眠障碍可能需要药物治疗配合行为干预。请记住，良好的睡眠是健康的基础。',
"""

sleep_en = """    // Sleep Content
    'sleep_intro_title': 'About Sleep Quality Assessment (PSQI)',
    'sleep_intro_p1': 'Sleep quality is crucial for physical and mental health. The World Health Organization (WHO) states that sleep is the first element in maintaining physical health. Good sleep helps with body repair, memory consolidation, emotion regulation, and immune function maintenance. Conversely, poor sleep quality over a long period may lead to various health problems, including cardiovascular diseases, diabetes, obesity, and mental health issues.',
    'sleep_intro_p2': 'The PSQI (Pittsburgh Sleep Quality Index) was developed by Buysse et al. in 1989 as a sleep quality assessment tool. It evaluates sleep quality from 7 aspects: subjective sleep quality, sleep latency, sleep duration, sleep efficiency, sleep disturbances, use of sleep medications, and daytime dysfunction. The total score ranges from 0-21.',
    'sleep_intro_p3': 'Studies show that a PSQI total score greater than 5 indicates poor sleep quality. Chinese norm data shows that approximately 37.8% of adults have poor sleep quality. Poor sleep not only affects daytime work and learning efficiency, but also increases the risk of disease over time.',
    'sleep_intro_p4': 'This test is for self-exploration reference only and does not replace professional diagnosis. If you have long-term sleep problems, please consult a sleep specialist or psychotherapist.',
    'sleep_result_title': 'Sleep Quality Result Interpretation',
    'sleep_result_p1': 'PSQI scoring criteria: 0-5 points indicates good sleep quality, 6-10 points indicates mild sleep problems, 11-15 points indicates moderate sleep problems, 16-21 points indicates severe sleep problems. A total score >=5 indicates poor sleep quality and needs attention.',
    'sleep_result_p2': 'Mild sleep problems (6-10 points): It is recommended to adjust sleep habits, such as fixed sleep schedule, avoiding electronic devices before bed, keeping the bedroom quiet and dark, etc. Can be relieved by improving sleep hygiene.',
    'sleep_result_p3': 'Moderate sleep problems (11-15 points): It is recommended to seek professional help and undergo sleep cognitive behavioral therapy (CBT-I). At the same time, pay attention to ruling out potential physiological or psychological factors, such as anxiety, depression, sleep apnea, etc.',
    'sleep_result_p4': 'Severe sleep problems (>=16 points): It is recommended to seek medical attention as soon as possible for professional sleep monitoring and assessment. Severe sleep disorders may require medication combined with behavioral intervention. Please remember that good sleep is the foundation of health.',
"""

# Add Stress and Sleep Chinese after GAD-7 in Chinese section
zh_gad7_end = "'gad7_result_p4': '重度焦虑（>=15分）需要高度重视，建议尽快寻求专业帮助。持续的严重焦虑可能影响身体健康和日常生活质量。请记住，寻求帮助是勇敢的表现，专业的支持可以帮助您走出困境。',"
if zh_gad7_end in content:
    content = content.replace(zh_gad7_end, zh_gad7_end + "\n" + stress_zh, 1)
    print("✓ Added Stress Chinese translations")
else:
    print("✗ Could not find insertion point for Stress Chinese")

if zh_gad7_end in content:
    content = content.replace(zh_gad7_end, zh_gad7_end + "\n" + sleep_zh, 1)
    print("✓ Added Sleep Chinese translations")
else:
    print("✗ Could not find insertion point for Sleep Chinese")

# Add Stress and Sleep English after GAD-7 in English section
en_gad7_end = "'gad7_result_p4': 'Severe anxiety (>=15 points) requires serious attention, and prompt professional help is recommended. Persistent severe anxiety may affect physical health and quality of daily life. Please remember that seeking help is a brave act, and professional support can help you overcome difficulties.',"
if en_gad7_end in content:
    content = content.replace(en_gad7_end, en_gad7_end + "\n" + stress_en, 1)
    print("✓ Added Stress English translations")
else:
    print("✗ Could not find insertion point for Stress English")

if en_gad7_end in content:
    content = content.replace(en_gad7_end, en_gad7_end + "\n" + sleep_en, 1)
    print("✓ Added Sleep English translations")
else:
    print("✗ Could not find insertion point for Sleep English")

# Add result level keys for GAD-7, Stress, Sleep
level_keys_zh = """    // Result levels
    'scl90_level_normal': '正常',
    'scl90_level_mild': '轻度',
    'scl90_level_moderate': '中度',
    'scl90_level_severe': '重度',
    'phq9_level_none': '无明显抑郁',
    'phq9_level_mild': '轻度抑郁',
    'phq9_level_moderate': '中度抑郁',
    'phq9_level_mod_severe': '中重度抑郁',
    'phq9_level_severe': '重度抑郁',
    'gad7_level_none': '无明显焦虑',
    'gad7_level_mild': '轻度焦虑',
    'gad7_level_moderate': '中度焦虑',
    'gad7_level_severe': '重度焦虑',
    'stress_level_minimal': '轻度压力',
    'stress_level_mild': '中度压力',
    'stress_level_moderate': '重度压力',
    'stress_level_severe': '极重压力',
    'stress_level_extreme': '极度压力',
    'sleep_level_good': '睡眠质量好',
    'sleep_level_mild': '轻度睡眠问题',
    'sleep_level_moderate': '中度睡眠问题',
    'sleep_level_severe': '重度睡眠问题',
"""

level_keys_en = """    // Result levels
    'scl90_level_normal': 'Normal',
    'scl90_level_mild': 'Mild',
    'scl90_level_moderate': 'Moderate',
    'scl90_level_severe': 'Severe',
    'phq9_level_none': 'No Depression',
    'phq9_level_mild': 'Mild Depression',
    'phq9_level_moderate': 'Moderate Depression',
    'phq9_level_mod_severe': 'Moderately Severe Depression',
    'phq9_level_severe': 'Severe Depression',
    'gad7_level_none': 'No Significant Anxiety',
    'gad7_level_mild': 'Mild Anxiety',
    'gad7_level_moderate': 'Moderate Anxiety',
    'gad7_level_severe': 'Severe Anxiety',
    'stress_level_minimal': 'Mild Stress',
    'stress_level_mild': 'Moderate Stress',
    'stress_level_moderate': 'Severe Stress',
    'stress_level_severe': 'Very Severe Stress',
    'stress_level_extreme': 'Extreme Stress',
    'sleep_level_good': 'Good Sleep Quality',
    'sleep_level_mild': 'Mild Sleep Problem',
    'sleep_level_moderate': 'Moderate Sleep Problem',
    'sleep_level_severe': 'Severe Sleep Problem',
"""

# Find and replace result levels section in Chinese
zh_levels_marker = "    // Result levels\n    'scl90_level_normal': '正常',"
if zh_levels_marker in content:
    content = content.replace(zh_levels_marker, level_keys_zh, 1)
    print("✓ Updated Chinese result level keys")
else:
    print("✗ Could not find Chinese result levels marker")

# Find and replace result levels section in English
en_levels_marker = "    // Result levels\n    'scl90_level_normal': 'Normal',"
if en_levels_marker in content:
    content = content.replace(en_levels_marker, level_keys_en, 1)
    print("✓ Updated English result level keys")
else:
    print("✗ Could not find English result levels marker")

with open(i18n_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("\n✓ Updated i18n.js with all new translation keys")
