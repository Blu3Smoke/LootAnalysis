import json
import math
from collections import Counter

with open('shipwreck_food.json') as sw_file:
    sw_data = json.load(sw_file)
with open('buried_treasure.json') as bt_file:
    bt_data = json.load(bt_file)

def count_tnt(data):
    tnt_list = []
    max_tnt = 0
    for chest in data:
        tnt = chest['minecraft:tnt'] if 'minecraft:tnt' in chest else 0
        max_tnt = max(max_tnt, tnt)
        tnt_list.append(tnt)
    return tnt_list, max_tnt

sw_tnt, sw_max = count_tnt(sw_data)
bt_tnt, bt_max = count_tnt(bt_data)

def write_histogram():
    global sw_tnt, bt_tnt, sw_max, bt_max
    sw_hist = Counter(sw_tnt)
    bt_hist = Counter(bt_tnt)
    with open('tnt_data.csv', 'w') as data_file:
        data_file.write('tnt,shipwreck,buried_treasure\n')
        for i in range(max(sw_max, bt_max) + 1):
            data_file.write(f'{i},{sw_hist[i]},{bt_hist[i]}\n')

def write_stats():
    global sw_tnt, bt_tnt, sw_max, bt_max
    total_sw = sum(sw_tnt)
    total_bt = sum(bt_tnt)
    avg_sw = total_sw / len(sw_tnt)
    avg_bt = total_bt / len(bt_tnt)
    stddev_sw = math.sqrt(sum(map(lambda x: (x-avg_sw)**2, sw_tnt)) / len(sw_tnt))
    stddev_bt = math.sqrt(sum(map(lambda x: (x-avg_bt)**2, bt_tnt)) / len(bt_tnt))
    print("Shipwreck:")
    print("  Total:", total_sw)
    print("  Avg:", avg_sw)
    print("  stddev:", stddev_sw)
    print("Buried Treasure:")
    print("  Total:", total_bt)
    print("  Avg:", avg_bt)
    print("  stddev:", stddev_bt)

write_histogram()
write_stats()
