from qimendunjia.core import *

print("=== 奇门遁甲排盘测试 ===")
print()

year, month, day, hour = 2024, 6, 1, 0

year_gz, month_gz, day_gz = get_ganzhi(year, month, day)
shichen = get_shichen(year, month, day, hour)

print(f"日期: {year}年{month}月{day}日 {hour:02d}:00")
print(f"年柱: {year_gz}")
print(f"月柱: {month_gz}")
print(f"日柱: {day_gz}")
print(f"时柱: {shichen}")
print()

jieqi = get_jieqi_for_date(year, month, day)
is_yang = is_yang_dun(year, month, day)
dun_number = get_dun_number(year, month, day)

print(f"节气: {jieqi}")
print(f"遁局: {'阳遁' if is_yang else '阴遁'}{dun_number}局")
print(f"方向: {'顺飞' if is_yang else '逆飞'}")
print()

dipan = calculate_dipan(is_yang, dun_number)
print("地盘排布:")
for i, palace in enumerate(NINE_PALACES):
    print(f"  {palace}: {dipan[i]}")
print()

xunshou = get_xunshou(day_gz)
print(f"旬首: {xunshou}")

zifu_star, zishi_gate, zifu_pos = get_zifu_and_zishi(day_gz, dipan)
print(f"值符: {zifu_star}星 落{NINE_PALACES[zifu_pos]}")
print(f"值使: {zishi_gate}门")
print()

shigan = get_shigan(hour, day_gz)
print(f"时干: {shigan}")
print()

tianpan, tianpan_stars = calculate_tianpan(zifu_star, shigan, is_yang, dipan)
print("天盘排布:")
for i, palace in enumerate(NINE_PALACES):
    print(f"  {palace}: 天盘干={tianpan[i]}, 星={tianpan_stars[i]}")
print()

renpan = calculate_renpan(zishi_gate, hour, day_gz, is_yang, dipan)
print("人盘排布:")
for i, palace in enumerate(NINE_PALACES):
    print(f"  {palace}: {renpan[i]}")
print()

shenpan = calculate_shenpan(zifu_pos, is_yang)
print("神盘排布:")
for i, palace in enumerate(NINE_PALACES):
    print(f"  {palace}: {shenpan[i]}")