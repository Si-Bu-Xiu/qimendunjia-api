import sxtwl
from .core import TIANGAN, DIZHI
from .location import apply_true_solar_time


# 六十甲子完整序列（用于流年、大运等推算）
GANZHI_60 = [TIANGAN[i % 10] + DIZHI[i % 12] for i in range(60)]


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


# 天干五行与阴阳（严格按子平术.md定义）
TIANGAN_WUXING_YINYANG = {
    '甲': ('木', '阳'), '乙': ('木', '阴'),
    '丙': ('火', '阳'), '丁': ('火', '阴'),
    '戊': ('土', '阳'), '己': ('土', '阴'),
    '庚': ('金', '阳'), '辛': ('金', '阴'),
    '壬': ('水', '阳'), '癸': ('水', '阴'),
}


# 地支五行与阴阳（严格按子平术.md定义）
DIZHI_WUXING_YINYANG = {
    '子': ('水', '阳'), '丑': ('土', '阴'),
    '寅': ('木', '阳'), '卯': ('木', '阴'),
    '辰': ('土', '阳'), '巳': ('火', '阴'),
    '午': ('火', '阳'), '未': ('土', '阴'),
    '申': ('金', '阳'), '酉': ('金', '阴'),
    '戌': ('土', '阳'), '亥': ('水', '阴'),
}


# 六十甲子纳音五行表
NAYIN_WUXING = {
    '甲子': '海中金', '乙丑': '海中金',
    '丙寅': '炉中火', '丁卯': '炉中火',
    '戊辰': '大林木', '己巳': '大林木',
    '庚午': '路旁土', '辛未': '路旁土',
    '壬申': '剑锋金', '癸酉': '剑锋金',
    '甲戌': '山头火', '乙亥': '山头火',
    '丙子': '涧下水', '丁丑': '涧下水',
    '戊寅': '城头土', '己卯': '城头土',
    '庚辰': '白蜡金', '辛巳': '白蜡金',
    '壬午': '杨柳木', '癸未': '杨柳木',
    '甲申': '泉中水', '乙酉': '泉中水',
    '丙戌': '屋上土', '丁亥': '屋上土',
    '戊子': '霹雳火', '己丑': '霹雳火',
    '庚寅': '松柏木', '辛卯': '松柏木',
    '壬辰': '长流水', '癸巳': '长流水',
    '甲午': '沙中金', '乙未': '沙中金',
    '丙申': '山下火', '丁酉': '山下火',
    '戊戌': '平地木', '己亥': '平地木',
    '庚子': '壁上土', '辛丑': '壁上土',
    '壬寅': '金箔金', '癸卯': '金箔金',
    '甲辰': '覆灯火', '乙巳': '覆灯火',
    '丙午': '天河水', '丁未': '天河水',
    '戊申': '大驿土', '己酉': '大驿土',
    '庚戌': '钗钏金', '辛亥': '钗钏金',
    '壬子': '桑柘木', '癸丑': '桑柘木',
    '甲寅': '大溪水', '乙卯': '大溪水',
    '丙辰': '沙中土', '丁巳': '沙中土',
    '戊午': '天上火', '己未': '天上火',
    '庚申': '石榴木', '辛酉': '石榴木',
    '壬戌': '大海水', '癸亥': '大海水',
}


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


def determine_pattern(day_master, month_gz, year_gz, hour_gz):
    """
    判定月令格局。

    子平法以月支本气取格；若月支藏干透出年干或时干，则以透干之十神取格。
    格局名按十神转换：正官、七杀、正印、偏印、正财、偏财、食神、伤官。
    """
    month_zhi = month_gz[1]
    cang = CANG_GAN[month_zhi]

    year_gan = year_gz[0]
    hour_gan = hour_gz[0]

    # 优先看月支藏干是否透出于年/时干
    selected_gan = cang[0]  # 默认取本气
    for cg in cang:
        if cg == year_gan or cg == hour_gan:
            selected_gan = cg
            break

    shishen = get_shishen(day_master, selected_gan)
    # 比肩劫财不入格，退而求其次取月令本气
    if shishen in ('比肩', '劫财'):
        selected_gan = cang[0]
        shishen = get_shishen(day_master, selected_gan)

    return shishen + '格'


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


def get_yi_ma(year_zhi, day_zhi):
    """以年支和日支查驿马"""
    yi_ma_map = {'申': '寅', '子': '寅', '辰': '寅',
                 '寅': '申', '午': '申', '戌': '申',
                 '巳': '亥', '酉': '亥', '丑': '亥',
                 '亥': '巳', '卯': '巳', '未': '巳'}

    year_ma = yi_ma_map.get(year_zhi, '')
    day_ma = yi_ma_map.get(day_zhi, '')
    return {'year_ma': year_ma, 'day_ma': day_ma}


def get_dishi(day_gan, zhi):
    """
    计算日主在某一地支的十二长生状态（地势）。

    阳干顺行，阴干逆行，以长生地支为起点。
    """
    start_zhi = SHI_ER_SHEN_GAN_START[day_gan]
    start_idx = DIZHI.index(start_zhi)
    zhi_idx = DIZHI.index(zhi)

    if DAY_MASTER_TYPE[day_gan] == '阳':
        offset = (zhi_idx - start_idx) % 12
    else:
        offset = (start_idx - zhi_idx) % 12

    return SHI_ER_SHEN[day_gan][offset]


def get_nayin(ganzhi):
    """根据干支组合查询纳音五行。"""
    return NAYIN_WUXING.get(ganzhi, '')


# ============== 年柱神煞 ==============

def get_taisui(year_zhi):
    """太岁，即年支本身。"""
    return year_zhi


def get_suijian(year_zhi):
    """岁建，与太岁同，即年支本身。"""
    return year_zhi


def get_qinglong(year_zhi):
    """
    青龙（年支起十二神煞之一）。

    十二神煞顺序：青龙、明堂、天刑、朱雀、金匮、天德、白虎、玉堂、天牢、玄武、司命、勾陈。
    起法：以年支起青龙，按十二地支顺排。
    """
    qinglong_start = {'子': '辰', '丑': '卯', '寅': '寅', '卯': '丑',
                      '辰': '子', '巳': '亥', '午': '戌', '未': '酉',
                      '申': '申', '酉': '未', '戌': '午', '亥': '巳'}
    return qinglong_start.get(year_zhi, '')


def get_mingtang(year_zhi):
    """
    明堂（年支起十二神煞之二）。

    青龙顺排下一位即为明堂。
    """
    qinglong = get_qinglong(year_zhi)
    if not qinglong:
        return ''
    idx = DIZHI.index(qinglong)
    return DIZHI[(idx + 1) % 12]


# ============== 月柱神煞 ==============

def get_tiande(month_zhi):
    """
    天德贵人（以月支查）。

    寅月丁、卯月申、辰月壬、巳月辛、午月甲、未月癸、
    申月寅、酉月丙、戌月乙、亥月辛、子月庚、丑月辛。
    """
    tiande_map = {'寅': '丁', '卯': '申', '辰': '壬', '巳': '辛',
                  '午': '甲', '未': '癸', '申': '寅', '酉': '丙',
                  '戌': '乙', '亥': '辛', '子': '庚', '丑': '辛'}
    return tiande_map.get(month_zhi, '')


def get_tiandehe(month_zhi):
    """天德合：与天德相合的天干。"""
    tiande = get_tiande(month_zhi)
    if not tiande:
        return ''
    he_map = {'甲': '己', '己': '甲', '乙': '庚', '庚': '乙',
              '丙': '辛', '辛': '丙', '丁': '壬', '壬': '丁',
              '戊': '癸', '癸': '戊'}
    return he_map.get(tiande, '')


def get_yuede_by_month(month_zhi):
    """
    月德贵人（以月支查）。

    寅午戌月丙，亥卯未月甲，申子辰月壬，巳酉丑月庚。
    """
    yuede_map = {'寅': '丙', '卯': '甲', '辰': '壬',
                 '巳': '庚', '午': '丙', '未': '甲',
                 '申': '壬', '酉': '庚', '戌': '丙',
                 '亥': '甲', '子': '壬', '丑': '庚'}
    return yuede_map.get(month_zhi, '')


def get_yuedehe(month_zhi):
    """月德合：与月德相合的天干。"""
    yuede = get_yuede_by_month(month_zhi)
    if not yuede:
        return ''
    he_map = {'甲': '己', '己': '甲', '乙': '庚', '庚': '乙',
              '丙': '辛', '辛': '丙', '丁': '壬', '壬': '丁',
              '戊': '癸', '癸': '戊'}
    return he_map.get(yuede, '')


# ============== 日柱神煞 ==============

def get_fuxing(day_gan):
    """
    福星贵人（以日干查）。

    甲丙相邀入虎乡，更游鼠穴最高强，戊猴己未丁宜亥，
    乙癸逢牛卯禄昌，庚赶马头辛到巳，壬骑龙背喜非常。
    """
    fuxing_map = {'甲': '寅', '乙': '丑', '丙': '寅', '丁': '亥',
                  '戊': '申', '己': '未', '庚': '午', '辛': '巳',
                  '壬': '辰', '癸': '丑'}
    return fuxing_map.get(day_gan, '')


def get_wenchang(day_gan):
    """
    文昌贵人（以日干查）。

    甲乙巳午报君知，丙戊申宫丁己鸡，庚猪辛鼠壬逢虎，癸人见卯入云梯。
    """
    wenchang_map = {'甲': '巳', '乙': '午', '丙': '申', '丁': '酉',
                    '戊': '申', '己': '酉', '庚': '亥', '辛': '子',
                    '壬': '寅', '癸': '卯'}
    return wenchang_map.get(day_gan, '')


# ============== 时柱神煞 ==============

def get_xuetang(day_gan):
    """
    学堂（以日干五行查长生之地）。

    金命见巳，木命见亥，水命见申，火命见寅，土命见申。
    """
    xuetang_map = {'甲': '亥', '乙': '亥', '丙': '寅', '丁': '寅',
                   '戊': '申', '己': '申', '庚': '巳', '辛': '巳',
                   '壬': '申', '癸': '申'}
    return xuetang_map.get(day_gan, '')


def get_ciguan(day_gan):
    """
    词馆（以日干五行查临官之地）。

    甲乙见寅，丙丁戊己见巳，庚辛见申，壬癸见亥。
    """
    ciguan_map = {'甲': '寅', '乙': '寅', '丙': '巳', '丁': '巳',
                  '戊': '巳', '己': '巳', '庚': '申', '辛': '申',
                  '壬': '亥', '癸': '亥'}
    return ciguan_map.get(day_gan, '')


def get_taohua(day_zhi):
    """以日支查桃花。"""
    taohua_map = {'申': '酉', '子': '酉', '辰': '酉',
                  '寅': '卯', '午': '卯', '戌': '卯',
                  '巳': '午', '酉': '午', '丑': '午',
                  '亥': '子', '卯': '子', '未': '子'}
    return taohua_map.get(day_zhi, '')


def get_huagai(day_zhi):
    """以日支查华盖。"""
    huagai_map = {'申': '辰', '子': '辰', '辰': '辰',
                  '寅': '戌', '午': '戌', '戌': '戌',
                  '巳': '丑', '酉': '丑', '丑': '丑',
                  '亥': '未', '卯': '未', '未': '未'}
    return huagai_map.get(day_zhi, '')


def get_tianxi(year_zhi):
    """以年支查天喜。"""
    tianxi_map = {'子': '酉', '丑': '申', '寅': '未', '卯': '午',
                  '辰': '巳', '巳': '辰', '午': '卯', '未': '寅',
                  '申': '丑', '酉': '子', '戌': '亥', '亥': '戌'}
    return tianxi_map.get(year_zhi, '')


def get_hongluan(year_zhi):
    """以年支查红鸾。"""
    hongluan_map = {'子': '卯', '丑': '寅', '寅': '丑', '卯': '子',
                    '辰': '亥', '巳': '戌', '午': '酉', '未': '申',
                    '申': '未', '酉': '午', '戌': '巳', '亥': '辰'}
    return hongluan_map.get(year_zhi, '')


def get_yuede(day_gan):
    """以日干或年干查月德贵人。"""
    yuede_map = {'甲': '寅', '乙': '申', '丙': '寅', '丁': '申',
                 '戊': '寅', '己': '申', '庚': '寅', '辛': '申',
                 '壬': '寅', '癸': '申'}
    return yuede_map.get(day_gan, '')


def get_yangren(day_gan):
    """以日干查羊刃。"""
    yangren_map = {'甲': '卯', '乙': '寅', '丙': '午', '丁': '巳',
                   '戊': '午', '己': '巳', '庚': '酉', '辛': '申',
                   '壬': '子', '癸': '亥'}
    return yangren_map.get(day_gan, '')


def get_hongyan(day_gan):
    """以日干查红艳煞。"""
    hongyan_map = {'甲': '午', '乙': '申', '丙': '寅', '丁': '未',
                   '戊': '辰', '己': '辰', '庚': '戌', '辛': '酉',
                   '壬': '子', '癸': '申'}
    return hongyan_map.get(day_gan, '')


def get_feiren(day_gan):
    """以日干查飞刃（羊刃对冲）。"""
    yangren = get_yangren(day_gan)
    if not yangren:
        return ''
    # 地支六冲
    chong_map = {'子': '午', '午': '子', '丑': '未', '未': '丑',
                 '寅': '申', '申': '寅', '卯': '酉', '酉': '卯',
                 '辰': '戌', '戌': '辰', '巳': '亥', '亥': '巳'}
    return chong_map.get(yangren, '')


def get_guluan(day_gz):
    """查孤鸾煞（特定日柱）。"""
    guluan_list = ['乙巳', '丁巳', '辛亥', '戊申', '壬寅', '戊午', '壬子', '丙午']
    return day_gz in guluan_list


def get_shiling(day_gz):
    """查十灵日（特定日柱）。"""
    shiling_list = ['甲辰', '乙亥', '丙辰', '丁酉', '戊午', '庚戌', '庚寅', '辛亥', '壬寅', '癸未']
    return day_gz in shiling_list


def get_pillar_shensha(pillar_gan, pillar_zhi, day_gan, day_zhi, year_zhi, year_gan, day_gz, month_zhi, position):
    """
    综合计算某一柱所带的神煞标记。

    按《渊海子平》及传统子平术规则，分柱位补充年、月、日、时四柱专属神煞。

    Args:
        pillar_gan (str): 该柱天干
        pillar_zhi (str): 该柱地支
        day_gan (str): 日干
        day_zhi (str): 日支
        year_zhi (str): 年支
        year_gan (str): 年干
        day_gz (str): 日柱干支
        month_zhi (str): 月支
        position (str): 柱位 'year'/'month'/'day'/'hour'

    Returns:
        list: 该柱所带神煞名称列表
    """
    shensha = []

    # ===== 通用神煞（所有柱位均可查） =====
    # 天乙贵人（日干查）
    tianyi = get_tianyi_gui(day_gan)
    if pillar_zhi in tianyi:
        shensha.append('天乙贵人')

    # 驿马（年支/日支查）
    yi_ma_info = get_yi_ma(year_zhi, day_zhi)
    if pillar_zhi in yi_ma_info.values():
        shensha.append('驿马')

    # 桃花（日支查）
    if pillar_zhi == get_taohua(day_zhi):
        shensha.append('桃花')

    # 华盖（日支查）
    if pillar_zhi == get_huagai(day_zhi):
        shensha.append('华盖')

    # 天喜（年支查）
    if pillar_zhi == get_tianxi(year_zhi):
        shensha.append('天喜')

    # 红鸾（年支查）
    if pillar_zhi == get_hongluan(year_zhi):
        shensha.append('红鸾')

    # 红艳（日干查）
    if pillar_zhi == get_hongyan(day_gan):
        shensha.append('红艳')

    # 羊刃（日干查）
    if pillar_zhi == get_yangren(day_gan):
        shensha.append('羊刃')

    # 飞刃（日干查，羊刃对冲）
    if pillar_zhi == get_feiren(day_gan):
        shensha.append('飞刃')

    # ===== 年柱专属神煞 =====
    if position == 'year':
        if pillar_zhi == get_taisui(year_zhi):
            shensha.append('太岁')
        if pillar_zhi == get_suijian(year_zhi):
            shensha.append('岁建')
        if pillar_zhi == get_qinglong(year_zhi):
            shensha.append('青龙')
        if pillar_zhi == get_mingtang(year_zhi):
            shensha.append('明堂')

    # ===== 月柱专属神煞 =====
    if position == 'month':
        tiande = get_tiande(month_zhi)
        tiandehe = get_tiandehe(month_zhi)
        yuede = get_yuede_by_month(month_zhi)
        yuedehe = get_yuedehe(month_zhi)

        # 天德贵人：月柱天干或年干见天德天干
        if pillar_gan == tiande or year_gan == tiande:
            shensha.append('天德')
        # 天德合：月柱天干或年干见天德合天干
        if pillar_gan == tiandehe or year_gan == tiandehe:
            shensha.append('天德合')
        # 月德贵人：月柱天干或年干见月德天干
        if pillar_gan == yuede or year_gan == yuede:
            shensha.append('月德')
        # 月德合：月柱天干或年干见月德合天干
        if pillar_gan == yuedehe or year_gan == yuedehe:
            shensha.append('月德合')

    # ===== 日柱专属神煞 =====
    if position == 'day':
        # 福星贵人
        if pillar_zhi == get_fuxing(day_gan):
            shensha.append('福星贵人')
        # 文昌贵人
        if pillar_zhi == get_wenchang(day_gan):
            shensha.append('文昌贵人')

    # ===== 时柱专属神煞 =====
    if position == 'hour':
        # 学堂
        if pillar_zhi == get_xuetang(day_gan):
            shensha.append('学堂')
        # 词馆
        if pillar_zhi == get_ciguan(day_gan):
            shensha.append('词馆')

    return shensha


def get_global_shensha(day_gz, year_gan):
    """获取全局性神煞标记（在日柱显示）。"""
    global_shensha = []
    if get_guluan(day_gz):
        global_shensha.append('孤鸾煞')
    if get_shiling(day_gz):
        global_shensha.append('十灵日')
    return global_shensha


def get_ri_gui(day_gz):
    """查日贵：丁酉、丁亥、癸巳、癸卯四日。"""
    return day_gz in ['丁酉', '丁亥', '癸巳', '癸卯']


def get_ri_de(day_gz):
    """查日德：甲寅、戊辰、丙辰、庚辰、壬戌。"""
    return day_gz in ['甲寅', '戊辰', '丙辰', '庚辰', '壬戌']


def get_kuigang(day_gz):
    """查魁罡：壬辰、庚戌、戊戌、庚辰。"""
    return day_gz in ['壬辰', '庚戌', '戊戌', '庚辰']


def get_jinshen(hour_gz):
    """查时上金神：癸酉、己巳、乙丑三时。"""
    return hour_gz in ['癸酉', '己巳', '乙丑']


def get_ri_ren(day_gz):
    """查日刃：戊午、丙午、壬子。"""
    return day_gz in ['戊午', '丙午', '壬子']


def get_yangren_by_gan(day_gan, zhi):
    """判断某地支是否为日干之阳刃。"""
    return zhi == get_yangren(day_gan)


def get_liuqin(shishen, gender='男'):
    """
    根据十神推导六亲关系。

    男命：正财为妻、偏财为父/妾、正印为母、正官为女、七杀为子、
          食神为孙、伤官为孙女/祖母、比肩为兄弟、劫财为姐妹。
    女命：正官为夫、七杀为偏夫、正印为母、偏财为父、食神为男、伤官为女、
          比肩为姐妹、劫财为兄弟。
    """
    if gender == '男':
        liuqin_map = {
            '正财': '妻',
            '偏财': '父',
            '正印': '母',
            '偏印': '祖父',
            '正官': '女',
            '七杀': '子',
            '食神': '孙',
            '伤官': '孙女',
            '比肩': '兄弟',
            '劫财': '姐妹',
        }
    else:
        liuqin_map = {
            '正官': '夫',
            '七杀': '偏夫',
            '正印': '母',
            '偏印': '祖父',
            '正财': '妻财',
            '偏财': '父',
            '食神': '男',
            '伤官': '女',
            '比肩': '姐妹',
            '劫财': '兄弟',
        }
    return liuqin_map.get(shishen, '')


def get_taiyuan(year_gz, month_gz):
    """
    计算胎元。

    胎元 = 月柱天干进一位，地支进三位。
    如月柱为丙寅，则胎元为丁巳。
    """
    gan_idx = TIANGAN.index(month_gz[0])
    zhi_idx = DIZHI.index(month_gz[1])
    taiyuan_gan = TIANGAN[(gan_idx + 1) % 10]
    taiyuan_zhi = DIZHI[(zhi_idx + 3) % 12]
    return taiyuan_gan + taiyuan_zhi


def get_minggong(month_zhi, hour_zhi):
    """
    计算命宫地支。

    子平法：以生月之宫与生时之宫相加，用 14 或 26 减之，余数安命。
    寅=1，卯=2... 子=11，丑=12。

    Args:
        month_zhi (str): 月支
        hour_zhi (str): 时支

    Returns:
        str: 命宫地支
    """
    zhi_num = {'寅': 1, '卯': 2, '辰': 3, '巳': 4, '午': 5, '未': 6,
               '申': 7, '酉': 8, '戌': 9, '亥': 10, '子': 11, '丑': 12}
    num_to_zhi = {v: k for k, v in zhi_num.items()}

    total = zhi_num[month_zhi] + zhi_num[hour_zhi]
    if total <= 14:
        ming_num = 14 - total
    else:
        ming_num = 26 - total

    # 调整到 1-12 范围
    while ming_num <= 0:
        ming_num += 12
    while ming_num > 12:
        ming_num -= 12

    return num_to_zhi.get(ming_num, '寅')


def calculate_liunian(start_year, count=10):
    """
    计算未来若干年的流年干支。

    Args:
        start_year (int): 起始流年年份
        count (int): 返回年数

    Returns:
        list: 每年 [年份, 干支]
    """
    liunian = []
    for y in range(start_year, start_year + count):
        # 用公式计算年干支：(年份 - 3) % 60
        gz_index = (y - 3) % 60
        if gz_index == 0:
            gz_index = 60
        liunian.append({'year': y, 'ganzhi': GANZHI_60[gz_index - 1]})
    return liunian


def bazi_paipan(year, month, day, hour, gender='男', location=''):
    """
    子平术（传统主流）八字排盘。

    Args:
        year (int): 出生年份
        month (int): 出生月份
        day (int): 出生日期
        hour (int): 出生小时（0-23）
        gender (str, optional): 性别，'男' 或 '女'
        location (str, optional): 出生地，用于真太阳时校准

    Returns:
        dict: 子平术排盘结果，包含四柱、藏干、十神、格局、用神忌神、大运、神煞及真太阳时信息
    """
    # 应用真太阳时校准
    time_info = apply_true_solar_time(year, month, day, hour, location)
    adj = time_info['adjusted']
    year, month, day, hour = adj['year'], adj['month'], adj['day'], adj['hour']

    gz = get_bazi_ganzhi(year, month, day, hour)
    day_master = get_day_master(gz['day'])
    day_zhi = gz['day'][1]
    year_gan = gz['year'][0]
    year_zhi = gz['year'][1]

    kongwang_list = get_kongwang(gz['day'])

    pillars = []
    for position in ['year', 'month', 'day', 'hour']:
        gz_str = gz[position]
        gan = gz_str[0]
        zhi = gz_str[1]
        cang = CANG_GAN[zhi]
        cang_shishen = [get_shishen(day_master, cg) for cg in cang]

        gan_wx, gan_yy = TIANGAN_WUXING_YINYANG[gan]
        zhi_wx, zhi_yy = DIZHI_WUXING_YINYANG[zhi]

        if position == 'day':
            main_shishen = '日元'
            liuqin = '自身'
        else:
            main_shishen = get_shishen(day_master, gan)
            liuqin = get_liuqin(main_shishen, gender)

        pillar = {
            'position': position,
            'gan': gan,
            'zhi': zhi,
            'shishen': main_shishen,
            'liuqin': liuqin,
            'gan_wuxing': gan_wx,
            'gan_yinyang': gan_yy,
            'zhi_wuxing': zhi_wx,
            'zhi_yinyang': zhi_yy,
            'canggan': cang,
            'canggan_shishen': cang_shishen,
            'dishi': get_dishi(day_master, zhi),
            'nayin': get_nayin(gz_str),
            'kongwang': zhi in kongwang_list,
            'shensha': get_pillar_shensha(gan, zhi, day_master, day_zhi, year_zhi, year_gan, gz['day'], gz['month'][1], position)
        }
        pillars.append(pillar)

    pattern = determine_pattern(day_master, gz['month'], gz['year'], gz['hour'])
    yong_ji = determine_yong_ji(day_master, gz['month'], day_master, gz['year'], gz['hour'])
    daxun = calculate_daxun(gz['year'], gender)

    # 全局性日柱/时柱神煞
    global_shensha = get_global_shensha(gz['day'], year_gan)
    if get_ri_gui(gz['day']):
        global_shensha.append('日贵')
    if get_ri_de(gz['day']):
        global_shensha.append('日德')
    if get_kuigang(gz['day']):
        global_shensha.append('魁罡')
    if get_ri_ren(gz['day']):
        global_shensha.append('日刃')
    if get_jinshen(gz['hour']):
        global_shensha.append('时上金神')
    if get_yangren_by_gan(day_master, day_zhi):
        global_shensha.append('阳刃')

    # 胎元、命宫、流年
    taiyuan = get_taiyuan(gz['year'], gz['month'])
    minggong = get_minggong(gz['month'][1], gz['hour'][1])
    liunian = calculate_liunian(year, 12)

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
        'kongwang': kongwang_list,
        'global_shensha': global_shensha,
        'taiyuan': taiyuan,
        'minggong': minggong,
        'liunian': liunian,
        'gender': gender,
        'location': location,
        'true_solar_time': time_info
    }

    return result


def xinpai_paipan(year, month, day, hour, gender='男', location=''):
    """
    新派命理八字排盘。

    Args:
        year (int): 出生年份
        month (int): 出生月份
        day (int): 出生日期
        hour (int): 出生小时（0-23）
        gender (str, optional): 性别，'男' 或 '女'
        location (str, optional): 出生地，用于真太阳时校准

    Returns:
        dict: 新派命理排盘结果，包含四柱、十神、旺衰、空亡、作用关系、大运及真太阳时信息
    """
    # 应用真太阳时校准
    time_info = apply_true_solar_time(year, month, day, hour, location)
    adj = time_info['adjusted']
    year, month, day, hour = adj['year'], adj['month'], adj['day'], adj['hour']

    gz = get_bazi_ganzhi(year, month, day, hour)
    day_master = get_day_master(gz['day'])
    day_zhi = gz['day'][1]
    year_gan = gz['year'][0]
    year_zhi = gz['year'][1]

    kongwang = get_kongwang(gz['day'])

    pillars = []
    for position in ['year', 'month', 'day', 'hour']:
        gz_str = gz[position]
        gan = gz_str[0]
        zhi = gz_str[1]
        cang = CANG_GAN[zhi]
        cang_shishen = [get_shishen(day_master, cg) for cg in cang]

        gan_wx, gan_yy = TIANGAN_WUXING_YINYANG[gan]
        zhi_wx, zhi_yy = DIZHI_WUXING_YINYANG[zhi]

        pillar = {
            'position': position,
            'gan': gan,
            'zhi': zhi,
            'shishen': get_shishen(day_master, gan),
            'gan_wuxing': gan_wx,
            'gan_yinyang': gan_yy,
            'zhi_wuxing': zhi_wx,
            'zhi_yinyang': zhi_yy,
            'canggan': cang,
            'canggan_shishen': cang_shishen,
            'dishi': get_dishi(day_master, zhi),
            'nayin': get_nayin(gz_str),
            'is_kongwang': zhi in kongwang,
            'shensha': get_pillar_shensha(gan, zhi, day_master, day_zhi, year_zhi, year_gan, gz['day'], gz['month'][1], position)
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

    interactions = []
    positions = ['year', 'month', 'day', 'hour']
    pos_names = {'year': '年', 'month': '月', 'day': '日', 'hour': '时'}
    for i in range(3):
        p1, p2 = positions[i], positions[i + 1]
        g1, g2 = gz[p1][0], gz[p2][0]
        w1, w2 = WU_XING[g1], WU_XING[g2]

        if WU_XING_SHENG.get(w1) == w2:
            interactions.append({'from': pos_names[p1], 'to': pos_names[p2], 'type': '生', 'symbol': '→'})
        elif WU_XING_KE.get(w1) == w2:
            interactions.append({'from': pos_names[p1], 'to': pos_names[p2], 'type': '克', 'symbol': '×'})
        elif WU_XING_SHENG.get(w2) == w1:
            interactions.append({'from': pos_names[p2], 'to': pos_names[p1], 'type': '生', 'symbol': '←'})
        elif WU_XING_KE.get(w2) == w1:
            interactions.append({'from': pos_names[p2], 'to': pos_names[p1], 'type': '克', 'symbol': '×'})

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
        'location': location,
        'true_solar_time': time_info
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
    """
    紫微斗数排盘。

    Args:
        year (int): 出生年份
        month (int): 出生月份（公历）
        day (int): 出生日期（公历）
        hour (int): 出生小时（0-23）
        gender (str, optional): 性别，'男' 或 '女'
        location (str, optional): 出生地，用于真太阳时校准

    Returns:
        dict: 紫微斗数排盘结果，包含十二宫、主星、辅星、四化、长生、大限及真太阳时信息
    """
    # 应用真太阳时校准
    time_info = apply_true_solar_time(year, month, day, hour, location)
    adj = time_info['adjusted']
    year, month, day, hour = adj['year'], adj['month'], adj['day'], adj['hour']

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
        'location': location,
        'true_solar_time': time_info
    }

    return result
