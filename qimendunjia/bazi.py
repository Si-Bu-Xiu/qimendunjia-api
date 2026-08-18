import sxtwl
from .core import TIANGAN, DIZHI


SHI_SHEN = {
    '甲': {'甲': '比肩', '乙': '劫财', '丙': '食神', '丁': '伤官', '戊': '偏财',
           '己': '正财', '庚': '七杀', '辛': '正官', '壬': '偏印', '癸': '正印'},
    '乙': {'甲': '劫财', '乙': '比肩', '丙': '伤官', '丁': '食神', '戊': '正财',
           '己': '偏财', '庚': '正官', '辛': '七杀', '壬': '正印', '癸': '偏印'},
    '丙': {'甲': '偏印', '乙': '正印', '丙': '比肩', '丁': '劫财', '戊': '食神',
           '己': '伤官', '庚': '偏财', '辛': '正财', '壬': '七杀', '癸': '正官'},
    '丁': {'甲': '正印', '乙': '偏印', '丙': '劫财', '丁': '比肩', '戊': '伤官',
           '己': '食神', '庚': '正财', '辛': '偏财', '壬': '正官', '癸': '七杀'},
    '戊': {'甲': '七杀', '乙': '正官', '丙': '正印', '丁': '偏印', '戊': '比肩',
           '己': '劫财', '庚': '食神', '辛': '伤官', '壬': '偏财', '癸': '正财'},
    '己': {'甲': '正官', '乙': '七杀', '丙': '偏印', '丁': '正印', '戊': '劫财',
           '己': '比肩', '庚': '伤官', '辛': '食神', '壬': '正财', '癸': '偏财'},
    '庚': {'甲': '偏财', '乙': '正财', '丙': '七杀', '丁': '正官', '戊': '偏印',
           '己': '正印', '庚': '比肩', '辛': '劫财', '壬': '食神', '癸': '伤官'},
    '辛': {'甲': '正财', '乙': '偏财', '丙': '正官', '丁': '七杀', '戊': '正印',
           '己': '偏印', '庚': '劫财', '辛': '比肩', '壬': '伤官', '癸': '食神'},
    '壬': {'甲': '食神', '乙': '伤官', '丙': '偏财', '丁': '正财', '戊': '七杀',
           '己': '正官', '庚': '偏印', '辛': '正印', '壬': '比肩', '癸': '劫财'},
    '癸': {'甲': '伤官', '乙': '食神', '丙': '正财', '丁': '偏财', '戊': '正官',
           '己': '七杀', '庚': '正印', '辛': '偏印', '壬': '劫财', '癸': '比肩'},
}


CANG_GAN = {
    '子': ['癸'],
    '丑': ['己', '癸', '辛'],
    '寅': ['甲', '丙', '戊'],
    '卯': ['乙'],
    '辰': ['戊', '乙', '癸'],
    '巳': ['丙', '庚', '戊'],
    '午': ['丁', '己'],
    '未': ['己', '丁', '乙'],
    '申': ['庚', '壬', '戊'],
    '酉': ['辛'],
    '戌': ['戊', '辛', '丁'],
    '亥': ['壬', '甲'],
}


SHI_ER_SHEN = {
    '甲': ['长生', '沐浴', '冠带', '临官', '帝旺', '衰', '病', '死', '墓', '绝', '胎', '养'],
    '乙': ['养', '胎', '绝', '墓', '死', '病', '衰', '帝旺', '临官', '冠带', '沐浴', '长生'],
    '丙': ['临官', '帝旺', '衰', '病', '死', '墓', '绝', '胎', '养', '长生', '沐浴', '冠带'],
    '丁': ['冠带', '临官', '帝旺', '衰', '病', '死', '墓', '绝', '胎', '养', '长生', '沐浴'],
    '戊': ['临官', '帝旺', '衰', '病', '死', '墓', '绝', '胎', '养', '长生', '沐浴', '冠带'],
    '己': ['冠带', '临官', '帝旺', '衰', '病', '死', '墓', '绝', '胎', '养', '长生', '沐浴'],
    '庚': ['死', '墓', '绝', '胎', '养', '长生', '沐浴', '冠带', '临官', '帝旺', '衰', '病'],
    '辛': ['病', '死', '墓', '绝', '胎', '养', '长生', '沐浴', '冠带', '临官', '帝旺', '衰'],
    '壬': ['墓', '绝', '胎', '养', '长生', '沐浴', '冠带', '临官', '帝旺', '衰', '病', '死'],
    '癸': ['绝', '胎', '养', '长生', '沐浴', '冠带', '临官', '帝旺', '衰', '病', '死', '墓'],
}


SHI_ER_SHEN_GAN_START = {
    '甲': '亥', '乙': '午', '丙': '寅', '丁': '酉', '戊': '寅',
    '己': '酉', '庚': '巳', '辛': '子', '壬': '申', '癸': '卯',
}


WU_XING = {
    '甲': '木', '乙': '木', '丙': '火', '丁': '火', '戊': '土',
    '己': '土', '庚': '金', '辛': '金', '壬': '水', '癸': '水',
}


WU_XING_SHENG = {'木': '火', '火': '土', '土': '金', '金': '水', '水': '木'}
WU_XING_KE = {'木': '土', '土': '水', '水': '火', '火': '金', '金': '木'}


DAY_MASTER_TYPE = {'甲': '阳', '丙': '阳', '戊': '阳', '庚': '阳', '壬': '阳',
                   '乙': '阴', '丁': '阴', '己': '阴', '辛': '阴', '癸': '阴'}


def gz_to_str(gz):
    return TIANGAN[gz.tg] + DIZHI[gz.dz]


def get_bazi_ganzhi(year, month, day, hour):
    d = sxtwl.fromSolar(year, month, day)
    year_gz = gz_to_str(d.getYearGZ())
    month_gz = gz_to_str(d.getMonthGZ())
    day_gz = gz_to_str(d.getDayGZ())
    hour_gz = gz_to_str(d.getHourGZ(hour))
    return {
        'year': year_gz,
        'month': month_gz,
        'day': day_gz,
        'hour': hour_gz
    }


def get_shishen(day_gan, target_gan):
    return SHI_SHEN[day_gan][target_gan]


def get_cang_gan(zhi):
    return CANG_GAN[zhi]


def get_shishen_for_canggan(day_gan, cang_gan_list):
    return [get_shishen(day_gan, cg) for cg in cang_gan_list]


def get_day_master(day_gz):
    return day_gz[0]


def get_day_master_type(day_gan):
    return DAY_MASTER_TYPE[day_gan]


def get_wuxing(gan):
    return WU_XING[gan]


def get_xunshou(day_gz):
    gan_index = TIANGAN.index(day_gz[0])
    xun_start = (gan_index // 10) * 10
    return TIANGAN[xun_start] + DIZHI[0]


def get_kongwang(day_gz):
    gan_index = TIANGAN.index(day_gz[0])
    xun_start_gan_index = (gan_index // 10) * 10
    kong_gan_start = xun_start_gan_index + 10
    kong1 = DIZHI[(kong_gan_start) % 12]
    kong2 = DIZHI[(kong_gan_start + 1) % 12]
    return [kong1, kong2]


def calculate_daxun(year_gz, gender):
    year_gan = year_gz[0]
    year_type = DAY_MASTER_TYPE[year_gan]

    if (year_type == '阳' and gender == '男') or (year_type == '阴' and gender == '女'):
        shunni = '顺'
    else:
        shunni = '逆'

    start_age = 3

    daxun = []
    gan = year_gz[0]
    zhi = year_gz[1]

    for i in range(8):
        gan_idx = TIANGAN.index(gan)
        zhi_idx = DIZHI.index(zhi)

        if shunni == '顺':
            gan = TIANGAN[(gan_idx + 1) % 10]
            zhi = DIZHI[(zhi_idx + 1) % 12]
        else:
            gan = TIANGAN[(gan_idx - 1) % 10]
            zhi = DIZHI[(zhi_idx - 1) % 12]

        start = start_age + i * 10
        end = start + 9
        daxun.append({
            'age': f"{start}-{end}岁",
            'ganzhi': gan + zhi
        })

    return daxun


def determine_pattern(month_gz, year_gz, hour_gz):
    month_zhi = month_gz[1]
    cang = CANG_GAN[month_zhi]

    year_gan = year_gz[0]
    hour_gan = hour_gz[0]

    if cang[0] == year_gan or cang[0] == hour_gan:
        return cang[0] + '格'
    elif len(cang) > 1 and cang[1] == year_gan or (len(cang) > 1 and cang[1] == hour_gan):
        return cang[1] + '格'
    else:
        return cang[0] + '格'


def determine_yong_ji(day_master, month_gz, day_gan, year_gz, hour_gz):
    day_wuxing = WU_XING[day_master]
    month_zhi = month_gz[1]
    cang_main = CANG_GAN[month_zhi][0]
    month_main_wuxing = WU_XING[cang_main]

    if month_main_wuxing in (WU_XING_SHENG.get(day_wuxing, ''), day_wuxing):
        is_strong = True
    else:
        is_strong = False

    yong = []
    ji = []

    if is_strong:
        for g in [year_gz[0], hour_gz[0]]:
            w = WU_XING[g]
            if w == WU_XING_KE.get(day_wuxing, ''):
                yong.append(g)
            elif w == WU_XING_SHENG.get(day_wuxing, ''):
                ji.append(g)
            elif w == day_wuxing:
                ji.append(g)
            else:
                yong.append(g)
    else:
        for g in [year_gz[0], hour_gz[0]]:
            w = WU_XING[g]
            if w == WU_XING_SHENG.get(day_wuxing, ''):
                yong.append(g)
            elif w == day_wuxing:
                yong.append(g)
            elif w == WU_XING_KE.get(day_wuxing, ''):
                ji.append(g)
            else:
                ji.append(g)

    return {'yong': list(set(yong)), 'ji': list(set(ji)), 'is_strong': is_strong}


BAZHI_GUI_YI = [
    ('甲戊庚', '牛', '羊'),
    ('乙己', '鼠', '猴'),
    ('丙丁', '猪', '鸡'),
    ('壬癸', '兔', '蛇'),
    ('六辛', '虎', '马'),
]


def get_tianyi_gui(day_gan):
    for entry in BAZHI_GUI_YI:
        if day_gan in entry[0] or (day_gan == '辛' and entry[0] == '六辛'):
            return [entry[1], entry[2]]
    return []


def get_yi_ma(zhi_list):
    shenzi = ['申', '子', '辰']
    yinwu = ['寅', '午', '戌']
    sanchou = ['巳', '酉', '丑']
    haimao = ['亥', '卯', '未']

    yi_ma_map = {'申': '寅', '子': '寅', '辰': '寅',
                 '寅': '申', '午': '申', '戌': '申',
                 '巳': '亥', '酉': '亥', '丑': '亥',
                 '亥': '巳', '卯': '巳', '未': '巳'}

    result = []
    for z in zhi_list:
        if z in yi_ma_map:
            result.append(yi_ma_map[z])
    return result


def bazi_paipan(year, month, day, hour, gender='男', location=''):
    gz = get_bazi_ganzhi(year, month, day, hour)
    day_master = get_day_master(gz['day'])

    pillars = []
    for position in ['year', 'month', 'day', 'hour']:
        gz_str = gz[position]
        gan = gz_str[0]
        zhi = gz_str[1]
        cang = CANG_GAN[zhi]
        shishen_list = [get_shishen(day_master, cg) for cg in cang]

        pillar = {
            'position': position,
            'gan': gan,
            'zhi': zhi,
            'shishen': get_shishen(day_master, gan),
            'canggan': cang,
            'canggan_shishen': shishen_list
        }
        pillars.append(pillar)

    pattern = determine_pattern(gz['month'], gz['year'], gz['hour'])
    yong_ji = determine_yong_ji(day_master, gz['month'], day_master, gz['year'], gz['hour'])
    daxun = calculate_daxun(gz['year'], gender)

    all_zhi = [gz['year'][1], gz['month'][1], gz['hour'][1]]
    tianyi = get_tianyi_gui(day_master)
    yi_ma = get_yi_ma(all_zhi)

    result = {
        'method': '子平术（传统主流）',
        'date': {'year': year, 'month': month, 'day': day, 'hour': hour},
        'ganzhi': gz,
        'day_master': day_master,
        'day_master_type': DAY_MASTER_TYPE[day_master],
        'pillars': pillars,
        'pattern': pattern,
        'yong_shen': yong_ji['yong'],
        'ji_shen': yong_ji['ji'],
        'is_strong': yong_ji['is_strong'],
        'daxun': daxun,
        'shishen': [get_shishen(day_master, gz[p][0]) for p in ['year', 'month', 'day', 'hour']],
        'shensha': {
            'tianyi_gui': tianyi,
            'yi_ma': yi_ma
        },
        'gender': gender,
        'location': location
    }

    return result


def xinpai_paipan(year, month, day, hour, gender='男', location=''):
    gz = get_bazi_ganzhi(year, month, day, hour)
    day_master = get_day_master(gz['day'])

    pillars = []
    for position in ['year', 'month', 'day', 'hour']:
        gz_str = gz[position]
        gan = gz_str[0]
        zhi = gz_str[1]
        shishen = get_shishen(day_master, gan)

        pillar = {
            'position': position,
            'gan': gan,
            'zhi': zhi,
            'shishen': shishen
        }
        pillars.append(pillar)

    day_wuxing = WU_XING[day_master]
    month_zhi = gz['month'][1]
    cang_main = CANG_GAN[month_zhi][0]
    month_main_wuxing = WU_XING[cang_main]

    score = 0
    if month_main_wuxing == day_wuxing or month_main_wuxing == WU_XING_SHENG.get(day_wuxing, ''):
        score += 50
    elif month_main_wuxing == WU_XING_KE.get(day_wuxing, '') or month_main_wuxing == WU_XING_SHENG.get(WU_XING_KE.get(day_wuxing, ''), ''):
        score += 0
    else:
        score += 25

    for pos in ['year', 'hour']:
        zhi = gz[pos][1]
        cang = CANG_GAN[zhi]
        for cg in cang:
            cg_wx = WU_XING[cg]
            if cg_wx == day_wuxing or cg_wx == WU_XING_SHENG.get(day_wuxing, ''):
                score += 10
                break

    is_strong = score > 50

    yong = []
    ji = []
    if is_strong:
        for pos in ['year', 'month', 'hour']:
            g = gz[pos][0]
            w = WU_XING[g]
            if w == WU_XING_KE.get(day_wuxing, '') or w == WU_XING_SHENG.get(WU_XING_KE.get(day_wuxing, ''), ''):
                yong.append(g)
            elif w == WU_XING_SHENG.get(day_wuxing, '') or w == day_wuxing:
                ji.append(g)
            else:
                yong.append(g)
    else:
        for pos in ['year', 'month', 'hour']:
            g = gz[pos][0]
            w = WU_XING[g]
            if w == WU_XING_SHENG.get(day_wuxing, '') or w == day_wuxing:
                yong.append(g)
            elif w == WU_XING_KE.get(day_wuxing, '') or w == WU_XING_SHENG.get(WU_XING_KE.get(day_wuxing, ''), ''):
                ji.append(g)
            else:
                ji.append(g)

    kongwang = get_kongwang(gz['day'])

    interactions = []
    positions = ['year', 'month', 'day', 'hour']
    for i in range(3):
        p1, p2 = positions[i], positions[i + 1]
        g1, g2 = gz[p1][0], gz[p2][0]
        w1, w2 = WU_XING[g1], WU_XING[g2]

        if WU_XING_SHENG.get(w1) == w2:
            interactions.append({'from': p1, 'to': p2, 'type': '生', 'symbol': '→'})
        elif WU_XING_KE.get(w1) == w2:
            interactions.append({'from': p1, 'to': p2, 'type': '克', 'symbol': '×'})
        elif WU_XING_SHENG.get(w2) == w1:
            interactions.append({'from': p2, 'to': p1, 'type': '生', 'symbol': '←'})
        elif WU_XING_KE.get(w2) == w1:
            interactions.append({'from': p2, 'to': p1, 'type': '克', 'symbol': '×'})

    daxun = calculate_daxun(gz['year'], gender)

    result = {
        'method': '新派命理',
        'date': {'year': year, 'month': month, 'day': day, 'hour': hour},
        'ganzhi': gz,
        'day_master': day_master,
        'day_master_type': DAY_MASTER_TYPE[day_master],
        'pillars': pillars,
        'score': score,
        'is_strong': is_strong,
        'yong_shen': list(set(yong)),
        'ji_shen': list(set(ji)),
        'kongwang': kongwang,
        'interactions': interactions,
        'daxun': daxun,
        'gender': gender,
        'location': location
    }

    return result


ZIWEI_STARS = [
    '紫微', '天机', '太阳', '武曲', '天同', '廉贞',
    '天府', '太阴', '贪狼', '巨门', '天相', '天梁', '七杀', '破军'
]

ZIWEI_FU_STARS = [
    '文昌', '文曲', '左辅', '右弼', '天魁', '天钺',
    '擎羊', '陀罗', '火星', '铃星', '地空', '地劫'
]

ZIWEI_HUA = {
    '甲': {'化禄': '廉贞', '化权': '破军', '化科': '武曲', '化忌': '太阳'},
    '乙': {'化禄': '天机', '化权': '天梁', '化科': '紫微', '化忌': '太阴'},
    '丙': {'化禄': '天同', '化权': '天机', '化科': '文昌', '化忌': '廉贞'},
    '丁': {'化禄': '太阴', '化权': '天同', '化科': '天机', '化忌': '巨门'},
    '戊': {'化禄': '贪狼', '化权': '太阴', '化科': '右弼', '化忌': '天机'},
    '己': {'化禄': '武曲', '化权': '贪狼', '化科': '天梁', '化忌': '文曲'},
    '庚': {'化禄': '太阳', '化权': '武曲', '化科': '天同', '化忌': '天相'},
    '辛': {'化禄': '巨门', '化权': '太阳', '化科': '文曲', '化忌': '文昌'},
    '壬': {'化禄': '天梁', '化权': '紫微', '化科': '左辅', '化忌': '武曲'},
    '癸': {'化禄': '破军', '化权': '巨门', '化科': '太阴', '化忌': '贪狼'},
}

ZIWEI_WUXING_TABLE = {
    ('甲', '子丑'): '水二', ('甲', '寅卯'): '金四', ('甲', '辰巳'): '金四',
    ('甲', '午未'): '火六', ('甲', '申酉'): '火六', ('甲', '戌亥'): '木三',
    ('乙', '子丑'): '水二', ('乙', '寅卯'): '金四', ('乙', '辰巳'): '金四',
    ('乙', '午未'): '火六', ('乙', '申酉'): '火六', ('乙', '戌亥'): '木三',
    ('丙', '子丑'): '水二', ('丙', '寅卯'): '水二', ('丙', '辰巳'): '土五',
    ('丙', '午未'): '土五', ('丙', '申酉'): '木三', ('丙', '戌亥'): '木三',
    ('丁', '子丑'): '水二', ('丁', '寅卯'): '水二', ('丁', '辰巳'): '土五',
    ('丁', '午未'): '土五', ('丁', '申酉'): '木三', ('丁', '戌亥'): '木三',
    ('戊', '子丑'): '火六', ('戊', '寅卯'): '火六', ('戊', '辰巳'): '木三',
    ('戊', '午未'): '木三', ('戊', '申酉'): '金四', ('戊', '戌亥'): '金四',
    ('己', '子丑'): '火六', ('己', '寅卯'): '火六', ('己', '辰巳'): '木三',
    ('己', '午未'): '木三', ('己', '申酉'): '金四', ('己', '戌亥'): '金四',
    ('庚', '子丑'): '土五', ('庚', '寅卯'): '土五', ('庚', '辰巳'): '水二',
    ('庚', '午未'): '水二', ('庚', '申酉'): '火六', ('庚', '戌亥'): '火六',
    ('辛', '子丑'): '土五', ('辛', '寅卯'): '土五', ('辛', '辰巳'): '水二',
    ('辛', '午未'): '水二', ('辛', '申酉'): '火六', ('辛', '戌亥'): '火六',
    ('壬', '子丑'): '木三', ('壬', '寅卯'): '木三', ('壬', '辰巳'): '火六',
    ('壬', '午未'): '火六', ('壬', '申酉'): '土五', ('壬', '戌亥'): '土五',
    ('癸', '子丑'): '木三', ('癸', '寅卯'): '木三', ('癸', '辰巳'): '火六',
    ('癸', '午未'): '火六', ('癸', '申酉'): '土五', ('癸', '戌亥'): '土五',
}

PALACE_NAMES_ZIWEI = ['命宫', '兄弟宫', '夫妻宫', '子女宫', '财帛宫', '疾厄宫',
                       '迁移宫', '交友宫', '官禄宫', '田宅宫', '福德宫', '父母宫']

ZHI_NUM = {'寅': 1, '卯': 2, '辰': 3, '巳': 4, '午': 5, '未': 6,
           '申': 7, '酉': 8, '戌': 9, '亥': 10, '子': 11, '丑': 12}

NUM_ZHI = {1: '寅', 2: '卯', 3: '辰', 4: '巳', 5: '午', 6: '未',
           7: '申', 8: '酉', 9: '戌', 10: '亥', 11: '子', 12: '丑'}

ZIWEI_AGE_START = {'水二': 2, '木三': 3, '金四': 4, '土五': 5, '火六': 6}


def _get_lunar_date(year, month, day, hour):
    d = sxtwl.fromSolar(year, month, day)
    lunar_year = d.getLunarYear()
    lunar_month = d.getLunarMonth()
    lunar_day = d.getLunarDay()

    hour_zhi_idx = hour // 2
    if hour == 23 or hour == 0:
        hour_zhi_idx = 0
    lunar_hour = DIZHI[hour_zhi_idx]

    return lunar_year, lunar_month, lunar_day, lunar_hour


def _mingong_shengong(lunar_month, lunar_hour_zhi):
    month_num = lunar_month
    hour_num = ZHI_NUM[lunar_hour_zhi]

    mingong_num = 1 + (month_num - 1) - (hour_num - 1)
    if mingong_num <= 0:
        mingong_num += 12

    shengong_num = 1 + (month_num - 1) + (hour_num - 1)
    if shengong_num > 12:
        shengong_num -= 12

    return NUM_ZHI[mingong_num], NUM_ZHI[shengong_num]


def _get_palace_tiangan(year_gan, mingong_zhi):
    wu_tun = {'甲': '丙', '己': '丙', '乙': '戊', '庚': '戊',
              '丙': '庚', '辛': '庚', '丁': '壬', '壬': '壬',
              '戊': '甲', '癸': '甲'}
    start_gan = wu_tun.get(year_gan, '甲')

    mingong_idx = ZHI_NUM[mingong_zhi]
    start_zhi_idx = 1

    diff = (mingong_idx - start_zhi_idx) % 12
    gan_idx = (TIANGAN.index(start_gan) + diff) % 10
    return TIANGAN[gan_idx]


def _get_wuxing局(mingong_ganzhi):
    gan = mingong_ganzhi[0]
    zhi = mingong_ganzhi[1]

    if zhi in ['子', '丑']:
        group = '子丑'
    elif zhi in ['寅', '卯']:
        group = '寅卯'
    elif zhi in ['辰', '巳']:
        group = '辰巳'
    elif zhi in ['午', '未']:
        group = '午未'
    elif zhi in ['申', '酉']:
        group = '申酉'
    else:
        group = '戌亥'

    return ZIWEI_WUXING_TABLE.get((gan, group), '木三')


def _布主星(lunar_day, wuxing局, mingong_zhi):
    stars_in_palace = {}

    start_num = ZHI_NUM[mingong_zhi]

    ziwei_pos = 0
    if wuxing局 == '水二':
        ziwei_pos = (lunar_day % 12)
        if ziwei_pos == 0:
            ziwei_pos = 12
    elif wuxing局 == '木三':
        ziwei_pos = ((lunar_day - 1) % 12) + 1
    elif wuxing局 == '金四':
        ziwei_pos = (lunar_day % 12)
        if ziwei_pos == 0:
            ziwei_pos = 12
    elif wuxing局 == '土五':
        ziwei_pos = ((lunar_day - 2) % 12) + 1
    elif wuxing局 == '火六':
        ziwei_pos = ((lunar_day + 1) % 12)
        if ziwei_pos == 0:
            ziwei_pos = 12

    ziwei_gong = NUM_ZHI[ziwei_pos]
    stars_in_palace[ziwei_gong] = ['紫微']

    galaxy1 = ['紫微', '天机', '太阳', '武曲', '天同', '廉贞']
    skip1 = [1, 2, 1, 1, 3]
    pos = ziwei_pos
    for i in range(1, len(galaxy1)):
        pos = pos + skip1[i - 1]
        while pos > 12:
            pos -= 12
        gong = NUM_ZHI[pos]
        if gong not in stars_in_palace:
            stars_in_palace[gong] = []
        stars_in_palace[gong].append(galaxy1[i])

    tianfu_opposite = {'子': '午', '午': '子', '丑': '未', '未': '丑',
                       '寅': '申', '申': '寅', '卯': '酉', '酉': '卯',
                       '辰': '戌', '戌': '辰', '巳': '亥', '亥': '巳'}

    tianfu_gong = tianfu_opposite[ziwei_gong]
    stars_in_palace[tianfu_gong] = ['天府']

    galaxy2 = ['天府', '太阴', '贪狼', '巨门', '天相', '天梁', '七杀', '破军']
    skip2 = [1, 1, 1, 1, 1, 1, 4]
    pos = ZHI_NUM[tianfu_gong]
    for i in range(1, len(galaxy2)):
        pos = pos + skip2[i - 1]
        while pos > 12:
            pos -= 12
        gong = NUM_ZHI[pos]
        if gong not in stars_in_palace:
            stars_in_palace[gong] = []
        stars_in_palace[gong].append(galaxy2[i])

    return stars_in_palace


def _布辅星(lunar_year, lunar_month, lunar_day, lunar_hour_zhi):
    fu_stars = {}

    left_fu_pos = (ZHI_NUM['辰'] + lunar_month - 1) % 12
    if left_fu_pos == 0:
        left_fu_pos = 12
    left_fu_gong = NUM_ZHI[left_fu_pos]
    fu_stars[left_fu_gong] = ['左辅']

    right_bi_pos = (ZHI_NUM['戌'] - lunar_month + 1) % 12
    if right_bi_pos == 0:
        right_bi_pos = 12
    right_bi_gong = NUM_ZHI[right_bi_pos]
    if right_bi_gong not in fu_stars:
        fu_stars[right_bi_gong] = []
    fu_stars[right_bi_gong].append('右弼')

    wenchang_pos = (ZHI_NUM['戌'] - ZHI_NUM[lunar_hour_zhi] + 1) % 12
    if wenchang_pos == 0:
        wenchang_pos = 12
    wenchang_gong = NUM_ZHI[wenchang_pos]
    if wenchang_gong not in fu_stars:
        fu_stars[wenchang_gong] = []
    fu_stars[wenchang_gong].append('文昌')

    wenqu_pos = (ZHI_NUM['辰'] + ZHI_NUM[lunar_hour_zhi] - 1) % 12
    if wenqu_pos == 0:
        wenqu_pos = 12
    wenqu_gong = NUM_ZHI[wenqu_pos]
    if wenqu_gong not in fu_stars:
        fu_stars[wenqu_gong] = []
    fu_stars[wenqu_gong].append('文曲')

    tiankui_map = {'甲': '丑', '乙': '子', '丙': '亥', '丁': '酉', '戊': '丑',
                   '己': '子', '庚': '丑', '辛': '午', '壬': '卯', '癸': '巳'}
    tiankui_gong = tiankui_map.get(lunar_year, '丑')
    if tiankui_gong not in fu_stars:
        fu_stars[tiankui_gong] = []
    fu_stars[tiankui_gong].append('天魁')

    tianyue_map = {'甲': '未', '乙': '申', '丙': '酉', '丁': '亥', '戊': '未',
                   '己': '申', '庚': '未', '辛': '寅', '壬': '辰', '癸': '卯'}
    tianyue_gong = tianyue_map.get(lunar_year, '未')
    if tianyue_gong not in fu_stars:
        fu_stars[tianyue_gong] = []
    fu_stars[tianyue_gong].append('天钺')

    return fu_stars


def _布四化(lunar_year_gan, stars_in_palace):
    hua = ZIWEI_HUA.get(lunar_year_gan, {})
    result = {}
    for gong, stars in stars_in_palace.items():
        for star in stars:
            for type_, hua_star in hua.items():
                if star == hua_star:
                    if gong not in result:
                        result[gong] = []
                    result[gong].append(type_)
    return result


def _长生十二神(wuxing局, mingong_zhi):
    changsheng_start = {
        '水二': '申', '木三': '亥', '金四': '巳', '火六': '寅', '土五': '申'
    }
    start_zhi = changsheng_start.get(wuxing局, '申')
    start_num = ZHI_NUM[start_zhi]

    shen_list = ['长生', '沐浴', '冠带', '临官', '帝旺', '衰', '病', '死', '墓', '绝', '胎', '养']
    result = {}

    mingong_num = ZHI_NUM[mingong_zhi]
    offset = (start_num - mingong_num) % 12

    for i in range(12):
        gong_num = (mingong_num + i) % 12
        if gong_num == 0:
            gong_num = 12
        gong = NUM_ZHI[gong_num]
        shen_idx = (i + offset) % 12
        result[gong] = shen_list[shen_idx]

    return result


def _大限(wuxing局, mingong_zhi, gender, lunar_year_gan):
    start_age = ZIWEI_AGE_START.get(wuxing局, 3)
    year_type = DAY_MASTER_TYPE.get(lunar_year_gan, '阳')

    if (year_type == '阳' and gender == '男') or (year_type == '阴' and gender == '女'):
        shunni = '顺'
    else:
        shunni = '逆'

    daxun = []
    mingong_num = ZHI_NUM[mingong_zhi]

    for i in range(12):
        if shunni == '顺':
            gong_num = (mingong_num + i) % 12
            if gong_num == 0:
                gong_num = 12
        else:
            gong_num = (mingong_num - i) % 12
            if gong_num == 0:
                gong_num = 12

        gong = NUM_ZHI[gong_num]
        palace_name = PALACE_NAMES_ZIWEI[i]
        start = start_age + i * 10
        end = start + 9
        daxun.append({
            'palace': palace_name,
            'age': f"{start}-{end}岁",
            'zhi': gong
        })

    return daxun


def ziwei_paipan(year, month, day, hour, gender='男', location=''):
    lunar_year, lunar_month, lunar_day, lunar_hour = _get_lunar_date(year, month, day, hour)

    d = sxtwl.fromSolar(year, month, day)
    year_gz = gz_to_str(d.getYearGZ())
    year_gan = year_gz[0]

    mingong_zhi, shengong_zhi = _mingong_shengong(lunar_month, lunar_hour)

    stars_in_palace = _布主星(lunar_day, '木三', mingong_zhi)

    mingong_gan = _get_palace_tiangan(year_gan, mingong_zhi)
    mingong_ganzhi = mingong_gan + mingong_zhi

    wuxing局 = _get_wuxing局(mingong_ganzhi)

    stars_in_palace = _布主星(lunar_day, wuxing局, mingong_zhi)

    fu_stars = _布辅星(year_gan, lunar_month, lunar_day, lunar_hour)

    for gong, fu_list in fu_stars.items():
        if gong not in stars_in_palace:
            stars_in_palace[gong] = []
        stars_in_palace[gong].extend(fu_list)

    hua_info = _布四化(year_gan, stars_in_palace)

    changsheng = _长生十二神(wuxing局, mingong_zhi)

    daxun = _大限(wuxing局, mingong_zhi, gender, year_gan)

    palaces = []
    for i in range(12):
        gong_num = ZHI_NUM[mingong_zhi]
        palace_zhi = NUM_ZHI[(gong_num + i) % 12] if (gong_num + i) % 12 != 0 else NUM_ZHI[12]

        palace_tian_gan = _get_palace_tiangan(year_gan, palace_zhi)
        palace_gz = palace_tian_gan + palace_zhi

        palace_data = {
            'name': PALACE_NAMES_ZIWEI[i],
            'zhi': palace_zhi,
            'ganzhi': palace_gz,
            'stars': stars_in_palace.get(palace_zhi, []),
            'hua': hua_info.get(palace_zhi, []),
            'changsheng': changsheng.get(palace_zhi, ''),
        }

        if palace_zhi == mingong_zhi:
            palace_data['is_mingong'] = True
        if palace_zhi == shengong_zhi:
            palace_data['is_shengong'] = True

        corresponding_daxun = [dx for dx in daxun if dx['palace'] == PALACE_NAMES_ZIWEI[i]]
        if corresponding_daxun:
            palace_data['daxun_age'] = corresponding_daxun[0]['age']

        palaces.append(palace_data)

    result = {
        'method': '紫微斗数',
        'date': {'year': year, 'month': month, 'day': day, 'hour': hour},
        'lunar': {'year': lunar_year, 'month': lunar_month, 'day': lunar_day, 'hour': lunar_hour},
        'mingong': mingong_zhi,
        'shengong': shengong_zhi,
        'wuxing局': wuxing局,
        'mingong_ganzhi': mingong_ganzhi,
        'palaces': palaces,
        'daxun': daxun,
        'gender': gender,
        'location': location
    }

    return result
