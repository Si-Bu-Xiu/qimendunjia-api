from .core import *


def feipan_zirun(year, month, day, hour):
    result = {
        'method': '飞盘置闰法',
        'date': {'year': year, 'month': month, 'day': day, 'hour': hour},
        'ganzhi': {},
        'dun_info': {},
        'palaces': []
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

    for i, palace in enumerate(NINE_PALACES):
        palace_data = {
            'name': palace,
            'dipan': dipan[i],
            'tianpan': tianpan[i],
            'tianpan_star': tianpan_stars[i],
            'renpan': renpan[i],
            'shenpan': shenpan[i]
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

    return result