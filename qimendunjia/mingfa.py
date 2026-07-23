from .core import *


def mingfa_qimen(year, month, day, hour):
    result = {
        'method': '鸣法奇门排盘（龙伏山人体系）',
        'date': {'year': year, 'month': month, 'day': day, 'hour': hour},
        'ganzhi': {},
        'dun_info': {},
        'palaces': [],
        'anqian': [],
        'yingqi': []
    }

    year_gz, month_gz, day_gz = get_ganzhi(year, month, day)
    shichen = get_shichen(year, month, day, hour)
    
    result['ganzhi'] = {
        'year': year_gz,
        'month': month_gz,
        'day': day_gz,
        'hour': shichen
    }

    is_yang = is_yang_dun(year, month, day)
    dun_number = get_dun_number(year, month, day)
    
    result['dun_info'] = {
        'type': '阳遁' if is_yang else '阴遁',
        'number': dun_number,
        'direction': '顺飞' if is_yang else '逆飞'
    }

    dipan = calculate_dipan(is_yang, dun_number)

    zifu_star, zishi_gate, zifu_pos = get_zifu_and_zishi(day_gz, dipan)

    shigan = get_shigan(hour, day_gz)

    tianpan, tianpan_stars = calculate_tianpan(zifu_star, shigan, is_yang, dipan)

    renpan = calculate_renpan(zishi_gate, hour, day_gz, is_yang, dipan)

    shenpan = calculate_shenpan(zifu_pos, is_yang)

    anqian = calculate_anqian(zifu_star, is_yang, dipan)

    yingqi = calculate_yingqi(hour, day_gz, is_yang)

    jin_tui_shen = calculate_jin_tui_shen(zifu_star, zishi_gate, is_yang)

    for i, palace in enumerate(NINE_PALACES):
        palace_data = {
            'name': palace,
            'dipan': dipan[i],
            'tianpan': tianpan[i],
            'tianpan_star': tianpan_stars[i],
            'renpan': renpan[i],
            'shenpan': shenpan[i],
            'anqian': anqian[i],
            'yingqi': yingqi[i]
        }
        
        if i == zifu_pos:
            palace_data['is_zifu'] = True
        if renpan[i] == zishi_gate:
            palace_data['is_zishi'] = True
        
        result['palaces'].append(palace_data)

    result['zifu'] = {
        'star': zifu_star,
        'palace': NINE_PALACES[zifu_pos]
    }
    
    result['zishi'] = {
        'gate': zishi_gate,
        'palace': NINE_PALACES[renpan.index(zishi_gate)] if zishi_gate in renpan else ''
    }

    result['jin_tui_shen'] = jin_tui_shen

    return result


def calculate_jin_tui_shen(zifu_star, zishi_gate, is_yang):
    jin_shen = []
    tui_shen = []
    
    jin_gate_pairs = [('休', '生'), ('生', '伤'), ('伤', '杜'), ('杜', '景'), 
                      ('景', '死'), ('死', '惊'), ('惊', '开'), ('开', '休')]
    tui_gate_pairs = [('休', '开'), ('开', '惊'), ('惊', '死'), ('死', '景'),
                      ('景', '杜'), ('杜', '伤'), ('伤', '生'), ('生', '休')]
    
    jin_star_pairs = [('天蓬', '天芮'), ('天芮', '天冲'), ('天冲', '天辅'), 
                      ('天辅', '天禽'), ('天禽', '天心'), ('天心', '天柱'), 
                      ('天柱', '天任'), ('天任', '天英'), ('天英', '天蓬')]
    
    if is_yang:
        for pair in jin_gate_pairs:
            if zishi_gate == pair[0]:
                jin_shen.append(f"门进神: {pair[0]}->{pair[1]}")
        
        for pair in jin_star_pairs:
            if zifu_star == pair[0]:
                jin_shen.append(f"星进神: {pair[0]}->{pair[1]}")
    else:
        for pair in tui_gate_pairs:
            if zishi_gate == pair[0]:
                tui_shen.append(f"门退神: {pair[0]}->{pair[1]}")
        
        for pair in jin_star_pairs:
            if zifu_star == pair[1]:
                tui_shen.append(f"星退神: {pair[1]}->{pair[0]}")
    
    return {
        'jin_shen': jin_shen,
        'tui_shen': tui_shen
    }