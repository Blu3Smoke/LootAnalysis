import json
from collections import Counter

with open('shipwreck.json') as sw_file:
    sw_data = json.load(sw_file)
with open('buried_treasure.json') as bt_file:
    bt_data = json.load(bt_file)

def count_diamond(data):
    diamond_list = []
    max_diamond = 0
    for chest in data:
        diamond = chest['minecraft:diamond'] if 'minecraft:diamond' in chest else 0
        max_diamond = max(max_diamond, diamond)
        diamond_list.append(diamond)
    return diamond_list, max_diamond

sw_diamond, sw_max = count_diamond(sw_data)
bt_diamond, bt_max = count_diamond(bt_data)

def write_histogram():
    global sw_diamond, bt_diamond, sw_max, bt_max
    sw_hist = Counter(sw_diamond)
    bt_hist = Counter(bt_diamond)
    with open('diamond_data.csv', 'w') as data_file:
        data_file.write('diamond,shipwreck,buried_treasure\n')
        for i in range(max(sw_max, bt_max) + 1):
            data_file.write(f'{i},{sw_hist[i]},{bt_hist[i]}\n')

def write_stats():
    global sw_diamond, bt_diamond, sw_max, bt_max
    total_sw = sum(sw_diamond)
    total_bt = sum(bt_diamond)
    avg_sw = total_sw / len(sw_diamond)
    avg_bt = total_bt / len(bt_diamond)
    print("Shipwreck:")
    print("  Total:", total_sw)
    print("  Avg:", avg_sw)
    print("Buried Treasure:")
    print("  Total:", total_bt)
    print("  Avg:", avg_bt)

write_histogram();
write_stats()
