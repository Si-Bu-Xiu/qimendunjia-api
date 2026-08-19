"""
地点与真太阳时处理模块。

本模块负责根据用户输入的出生地，计算当地的真太阳时，并据此调整排盘时间。

核心原理：
    中国统一使用东经120°的北京时间。命理排盘需要日晷实测时间（真太阳时），
    即当地太阳到达正中天（正午12点）的时刻。

    简化手算公式：
        真太阳时 = 北京时间 + 4分钟 × (当地经度 - 120°)

    注：东经为正，西经为负。此公式忽略均时差（约±15分钟），与传统手排命理一致。

使用示例：
    >>> from qimendunjia.location import apply_true_solar_time
    >>> result = apply_true_solar_time(2026, 8, 18, 13, '兰州')
    >>> print(result)
    {
        'original': {'year': 2026, 'month': 8, 'day': 18, 'hour': 13, 'minute': 0},
        'adjusted': {'year': 2026, 'month': 8, 'day': 18, 'hour': 12, 'minute': 16},
        'longitude': 103.8,
        'offset_minutes': -64.0,
        'location_matched': True,
        'note': '已按兰州经度103.8°校准为真太阳时'
    }
"""

from datetime import datetime, timedelta


# 常见城市经纬度表（经度精确到度即可满足手排需求）
# 格式：城市名（含常见别名） -> 东经度数
CITY_LONGITUDE_TABLE = {
    # 直辖市
    '北京': 116.4, '北京市': 116.4,
    '上海': 121.5, '上海市': 121.5,
    '天津': 117.2, '天津市': 117.2,
    '重庆': 106.5, '重庆市': 106.5,

    # 东北
    '哈尔滨': 126.6, '哈尔滨市': 126.6,
    '长春': 125.3, '长春市': 125.3,
    '沈阳': 123.4, '沈阳市': 123.4,
    '大连': 121.6, '大连市': 121.6,

    # 华北
    '石家庄': 114.5, '石家庄市': 114.5,
    '太原': 112.5, '太原市': 112.5,
    '呼和浩特': 111.7, '呼和浩特市': 111.7,
    '郑州': 113.7, '郑州市': 113.7,
    '济南': 117.0, '济南市': 117.0,
    '青岛': 120.4, '青岛市': 120.4,

    # 华东
    '南京': 118.8, '南京市': 118.8,
    '杭州': 120.2, '杭州市': 120.2,
    '宁波': 121.5, '宁波市': 121.5,
    '苏州': 120.6, '苏州市': 120.6,
    '合肥': 117.3, '合肥市': 117.3,
    '南昌': 115.9, '南昌市': 115.9,
    '福州': 119.3, '福州市': 119.3,
    '厦门': 118.1, '厦门市': 118.1,
    '台北': 121.5, '台北市': 121.5,
    '高雄': 120.3, '高雄市': 120.3,
    '香港': 114.2, '香港特别行政区': 114.2,
    '澳门': 113.5, '澳门特别行政区': 113.5,

    # 华中
    '武汉': 114.3, '武汉市': 114.3,
    '长沙': 113.0, '长沙市': 113.0,

    # 华南
    '广州': 113.3, '广州市': 113.3,
    '深圳': 114.1, '深圳市': 114.1,
    '南宁': 108.3, '南宁市': 108.3,
    '海口': 110.3, '海口市': 110.3,

    # 西南
    '成都': 104.1, '成都市': 104.1,
    '贵阳': 106.7, '贵阳市': 106.7,
    '昆明': 102.7, '昆明市': 102.7,
    '拉萨': 91.1, '拉萨市': 91.1,

    # 西北
    '西安': 108.9, '西安市': 108.9,
    '兰州': 103.8, '兰州市': 103.8,
    '西宁': 101.8, '西宁市': 101.8,
    '银川': 106.2, '银川市': 106.2,
    '乌鲁木齐': 87.6, '乌鲁木齐市': 87.6,

    # 其他常见城市
    '三亚': 109.5, '三亚市': 109.5,
    '桂林': 110.2, '桂林市': 110.2,
    '昆明': 102.7, '昆明市': 102.7,
    '丽江': 100.2, '丽江市': 100.2,
    '大理': 100.2, '大理市': 100.2,
}


def get_longitude(location):
    """
    根据地点名称查询经度。

    Args:
        location (str): 地点名称，如"北京"、"兰州市"、"浙江省杭州市"等。

    Returns:
        float or None: 地点的东经度数。如果无法识别，返回 None。
    """
    if not location or not isinstance(location, str):
        return None

    location = location.strip()
    if not location:
        return None

    # 直接匹配
    if location in CITY_LONGITUDE_TABLE:
        return CITY_LONGITUDE_TABLE[location]

    # 尝试包含关系：如"浙江省杭州市"中包含"杭州"
    for city, longitude in CITY_LONGITUDE_TABLE.items():
        if city in location:
            return longitude

    # 尝试去掉常见后缀
    suffixes = ['市', '县', '区', '省', '特别行政区']
    for suffix in suffixes:
        if location.endswith(suffix):
            key = location[:-len(suffix)]
            if key in CITY_LONGITUDE_TABLE:
                return CITY_LONGITUDE_TABLE[key]

    return None


def calculate_true_solar_time(year, month, day, hour, minute, longitude):
    """
    根据北京时间和当地经度计算真太阳时。

    Args:
        year (int): 年份
        month (int): 月份
        day (int): 日期
        hour (int): 北京时间小时（0-23）
        minute (int): 北京时间分钟（0-59）
        longitude (float): 当地东经度数

    Returns:
        dict: 包含调整后时间和偏移量的字典
            {
                'year', 'month', 'day', 'hour', 'minute',
                'offset_minutes', 'longitude'
            }
    """
    # 时差（分钟） = (当地经度 - 120) × 4
    offset_minutes = (longitude - 120.0) * 4.0

    # 构造北京时间 datetime
    beijing_time = datetime(year, month, day, hour, minute)

    # 计算真太阳时
    true_time = beijing_time + timedelta(minutes=offset_minutes)

    return {
        'year': true_time.year,
        'month': true_time.month,
        'day': true_time.day,
        'hour': true_time.hour,
        'minute': true_time.minute,
        'offset_minutes': round(offset_minutes, 1),
        'longitude': longitude
    }


def apply_true_solar_time(year, month, day, hour, location=''):
    """
    根据地点应用真太阳时校准。

    如果地点为空或无法识别，返回原始时间，并附带说明。

    Args:
        year (int): 年份
        month (int): 月份
        day (int): 日期
        hour (int): 北京时间小时（0-23）
        location (str, optional): 地点名称

    Returns:
        dict: {
            'original': {'year', 'month', 'day', 'hour', 'minute'},
            'adjusted': {'year', 'month', 'day', 'hour', 'minute',
                         'offset_minutes', 'longitude'},
            'location_matched': bool,
            'note': str
        }
    """
    original = {
        'year': year,
        'month': month,
        'day': day,
        'hour': hour,
        'minute': 0
    }

    longitude = get_longitude(location)

    if longitude is None:
        return {
            'original': original,
            'adjusted': dict(original, offset_minutes=0, longitude=120.0),
            'location_matched': False,
            'note': '未识别地点，默认使用东经120°北京时间排盘'
        }

    adjusted = calculate_true_solar_time(year, month, day, hour, 0, longitude)

    # 生成说明文字
    if adjusted['offset_minutes'] == 0:
        note = f'地点接近东经120°，无需时差校准'
    elif adjusted['offset_minutes'] > 0:
        note = f'已按{location}经度{longitude}°校准为真太阳时（比北京早{adjusted["offset_minutes"]}分钟）'
    else:
        note = f'已按{location}经度{longitude}°校准为真太阳时（比北京晚{abs(adjusted["offset_minutes"])}分钟）'

    return {
        'original': original,
        'adjusted': adjusted,
        'location_matched': True,
        'note': note
    }


def get_shichen_from_hour(hour, minute=0):
    """
    根据小时和分钟获取传统时辰名称。

    时辰划分：
        子时：23:00-00:59
        丑时：01:00-02:59
        ...
        亥时：21:00-22:59

    注意：23:00-23:59 属于次日的子时。

    Args:
        hour (int): 小时
        minute (int): 分钟

    Returns:
        str: 时辰名称，如"子时"、"午时"
    """
    from .core import DIZHI

    # 23:00 之后算次日子时
    if hour == 23:
        return DIZHI[0] + '时'

    zhi_index = (hour + 1) // 2 % 12
    return DIZHI[zhi_index] + '时'


if __name__ == '__main__':
    # 简单自测
    print(apply_true_solar_time(2026, 8, 18, 13, '兰州'))
    print(apply_true_solar_time(2026, 8, 18, 14, '哈尔滨'))
    print(apply_true_solar_time(2026, 8, 18, 11, '杭州'))
    print(apply_true_solar_time(2026, 8, 18, 11, '成都'))
    print(apply_true_solar_time(2026, 8, 18, 11, ''))
