from pathlib import Path

base_dir = Path(__file__).resolve().parent

login_info_path = base_dir / Path(r'db\login_info.txt')

freq_web_list = ['即刻', '1/日', '2/日', '3/日', '4/日', 'q2h', 'q6h', 'q8h', 'q12h', '每晚', '其他']
way_web_list = ['静脉滴注', '静脉泵入', '静脉推注', '肌肉注射', '静脉注射', '皮下注射', '球后注射',
                '结膜下注射', '眼内注射', '直肠给药', '雾化吸入', '肠道准备',
                '口服', '外用', '滴鼻', '滴耳', '滴眼', '鞘内注射', '腹膜透析', '皮试']
dose_unit_web_list = ['克', '毫克', '万单位', '滴', 'ml', '片', '支', '粒', '瓶', '包', '袋']

freq_dict = {'ONCE': '即刻',
             'QD': '1/日',
             'BID': '2/日',
             'TID': '3/日',
             'QID': '4/日',
             'Q2H': 'q2h',
             'Q6H': 'q6h',
             'Q8H': 'q8h',
             'Q12H': 'q2h',
             'QN': '每晚',
             '(空白)': '其他'}
way_dict = {'口服': '口服',
            '血液透析 ': '腹膜透析',
            '外用': '外用',
            '肌肉注射': '肌肉注射',
            '吸入': '雾化吸入',
            '涂眼睑内': '外用',
            '滴眼': '滴眼',
            '皮下注射(不带费用、耗材）': '皮下注射',
            '静脉注射(麻醉科专用)': '静脉注射',
            '塞肛': '外用',
            '含服': '口服',
            '局麻用': '肌肉注射',
            '喷喉': '外用'}
dose_unit_dict = {'丸': '粒', 'ug': '粒', '吸': '粒', 'ml': 'ml', '片': '片', 'g': '克', '粒': '粒', 'mg': '毫克'}