import sxtwl

TIANGAN = ['甲', '乙', '丙', '丁', '戊', '己', '庚', '辛', '壬', '癸']
DIZHI = ['子', '丑', '寅', '卯', '辰', '巳', '午', '未', '申', '酉', '戌', '亥']

QIYI = ['戊', '己', '庚', '辛', '壬', '癸', '丁', '丙', '乙']

NINE_PALACES = ['坎一', '坤二', '震三', '巽四', '中五', '乾六', '兑七', '艮八', '离九']
PALACE_NAMES = ['坎', '坤', '震', '巽', '中', '乾', '兑', '艮', '离']
PALACE_POSITIONS = {
    '坎一': 0, '坤二': 1, '震三': 2, '巽四': 3, '中五': 4,
    '乾六': 5, '兑七': 6, '艮八': 7, '离九': 8
}

STARS = ['天蓬', '天芮', '天冲', '天辅', '天禽', '天心', '天柱', '天任', '天英']
GATES = ['休', '生', '伤', '杜', '景', '死', '惊', '开']
GODS = ['值符', '螣蛇', '太阴', '六合', '白虎', '玄武', '九地', '九天']

XUN_HEAD = {'甲子': 0, '甲戌': 1, '甲申': 2, '甲午': 3, '甲辰': 4, '甲寅': 5}
XUN_HEAD_LIST = ['甲子', '甲戌', '甲申', '甲午', '甲辰', '甲寅']
XUN_HEAD_GAN = {'甲子': '戊', '甲戌': '己', '甲申': '庚', '甲午': '辛', '甲辰': '壬', '甲寅': '癸'}

JIETIAN = {
    0: '冬至', 1: '小寒', 2: '大寒', 3: '立春', 4: '雨水', 5: '惊蛰',
    6: '春分', 7: '清明', 8: '谷雨', 9: '立夏', 10: '小满', 11: '芒种',
    12: '夏至', 13: '小暑', 14: '大暑', 15: '立秋', 16: '处暑', 17: '白露',
    18: '秋分', 19: '寒露', 20: '霜降', 21: '立冬', 22: '小雪', 23: '大雪'
}

YANG_JIE = ['冬至', '小寒', '大寒', '立春', '雨水', '惊蛰', '春分', '清明', '谷雨', '立夏', '小满', '芒种']
YIN_JIE = ['夏至', '小暑', '大暑', '立秋', '处暑', '白露', '秋分', '寒露', '霜降', '立冬', '小雪', '大雪']


def gz_to_str(gz):
    return TIANGAN[gz.tg] + DIZHI[gz.dz]


def get_ganzhi(year, month, day):
    d = sxtwl.fromSolar(year, month, day)
    return gz_to_str(d.getYearGZ()), gz_to_str(d.getMonthGZ()), gz_to_str(d.getDayGZ())


def get_shichen(year, month, day, hour):
    d = sxtwl.fromSolar(year, month, day)
    return gz_to_str(d.getHourGZ(hour))


def get_jieqi_for_date(year, month, day):
    d = sxtwl.fromSolar(year, month, day)
    jq_code = d.getJieQi()
    if jq_code == 255:
        return find_closest_jieqi(year, month, day)
    return JIETIAN.get(jq_code, '')


def find_closest_jieqi(year, month, day):
    jq_list = sxtwl.getJieQiByYear(year)
    target_date = (year, month, day)
    
    for jq in jq_list:
        d = sxtwl.JD2DD(jq.jd)
        jq_date = (d.getYear(), d.getMonth(), d.getDay())
        if jq_date >= target_date:
            return JIETIAN.get(jq.jqIndex, '')
    
    return ''


def is_yang_dun(year, month, day):
    jieqi = get_jieqi_for_date(year, month, day)
    return jieqi in YANG_JIE


def get_dun_number(year, month, day):
    jieqi = get_jieqi_for_date(year, month, day)
    
    if jieqi in YANG_JIE:
        index = YANG_JIE.index(jieqi)
    else:
        index = YIN_JIE.index(jieqi)
    
    group = index // 3
    return group + 1


def get_xunshou(day_gz):
    gan_index = TIANGAN.index(day_gz[0])
    xun_index = gan_index % 6
    return XUN_HEAD_LIST[xun_index]


def calculate_dipan(is_yang, dun_number):
    dipan = [''] * 9
    start_index = (dun_number - 1) % 9
    
    for i in range(9):
        if is_yang:
            pos = (start_index + i) % 9
        else:
            pos = (start_index - i) % 9
        dipan[pos] = QIYI[i]
    
    return dipan


def get_zifu_and_zishi(day_gz, dipan):
    xunshou = get_xunshou(day_gz)
    xun_gan = XUN_HEAD_GAN[xunshou]
    
    xunshou_pos = -1
    for i, gan in enumerate(dipan):
        if gan == xun_gan:
            xunshou_pos = i
            break
    
    if xunshou_pos == -1:
        xunshou_pos = 0
    
    zifu_star = STARS[xunshou_pos]
    zishi_gate = GATES[xunshou_pos]
    
    return zifu_star, zishi_gate, xunshou_pos


def get_shigan(hour, day_gz):
    day_gan_index = TIANGAN.index(day_gz[0])
    shi_index = (day_gan_index * 2 + hour // 2) % 10
    return TIANGAN[shi_index]


def fei_positions_normal(start_pos, count, is_yang):
    positions = []
    current = start_pos
    
    for _ in range(count):
        positions.append(current)
        if is_yang:
            current = (current + 1) % 9
        else:
            current = (current - 1) % 9
    
    return positions


def calculate_tianpan(zifu_star, shigan, is_yang, dipan):
    gan_to_find = shigan if shigan != '甲' else '戊'
    
    tianpan = [''] * 9
    tianpan_stars = [''] * 9
    
    shigan_pos = -1
    for i, gan in enumerate(dipan):
        if gan == gan_to_find:
            shigan_pos = i
            break
    
    if shigan_pos == -1:
        shigan_pos = 0
    
    zifu_index = STARS.index(zifu_star)
    
    star_positions = []
    if is_yang:
        for i in range(9):
            pos = (shigan_pos + i - zifu_index) % 9
            star_positions.append(pos)
    else:
        for i in range(9):
            pos = (shigan_pos - i + zifu_index) % 9
            star_positions.append(pos)
    
    for i, star in enumerate(STARS):
        pos = star_positions[i]
        tianpan_stars[pos] = star
    
    for i, star in enumerate(STARS):
        pos = star_positions[i]
        original_pos = STARS.index(star)
        tianpan[pos] = dipan[original_pos]
    
    return tianpan, tianpan_stars


def calculate_renpan(zishi_gate, hour, day_gz, is_yang, dipan):
    xunshou = get_xunshou(day_gz)
    xun_gan = XUN_HEAD_GAN[xunshou]
    
    xunshou_pos = -1
    for i, gan in enumerate(dipan):
        if gan == xun_gan:
            xunshou_pos = i
            break
    
    if xunshou_pos == -1:
        xunshou_pos = 0
    
    shi_index = hour // 2
    if hour % 2 == 1:
        shi_index = (shi_index + 1) % 12
    
    renpan = [''] * 9
    
    if is_yang:
        start_pos = (xunshou_pos + shi_index) % 9
    else:
        start_pos = (xunshou_pos - shi_index) % 9
    
    zishi_index = GATES.index(zishi_gate)
    
    for i, gate in enumerate(GATES):
        if is_yang:
            pos = (start_pos + i - zishi_index) % 9
        else:
            pos = (start_pos - i + zishi_index) % 9
        renpan[pos] = gate
    
    return renpan


def calculate_shenpan(zifu_pos, is_yang):
    shenpan = [''] * 9
    
    positions = fei_positions_normal(zifu_pos, 8, is_yang)
    
    for i, god in enumerate(GODS):
        shenpan[positions[i]] = god
    
    shenpan[4] = shenpan[1]
    
    return shenpan


def calculate_anqian(zifu_star, is_yang, dipan):
    zifu_index = STARS.index(zifu_star)
    xun_index = zifu_index // 2
    xunshou = XUN_HEAD_LIST[xun_index]
    
    anqian = [''] * 9
    start_gan = TIANGAN[(xun_index * 2) % 10]
    
    positions = fei_positions_normal(0, 9, is_yang)
    
    for i in range(9):
        pos = positions[i]
        gan_index = (TIANGAN.index(start_gan) + i) % 10
        anqian[pos] = TIANGAN[gan_index] + DIZHI[(xun_index * 2 + i) % 12]
    
    return anqian


def get_xunshou_by_index(index):
    return XUN_HEAD_LIST[index]


def calculate_yingqi(hour, day_gz, is_yang):
    shi_index = hour // 2
    
    yingqi = []
    for i in range(9):
        if is_yang:
            dizhi_index = (shi_index + i) % 12
        else:
            dizhi_index = (shi_index - i) % 12
        yingqi.append(DIZHI[dizhi_index])
    
    return yingqi