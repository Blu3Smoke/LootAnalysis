import json
from collections import Counter

with open('shipwreck.json') as sw_file:
    sw_data = json.load(sw_file)
with open('buried_treasure.json') as bt_file:
    bt_data = json.load(bt_file)

def count_iron(data):
    iron_list = []
    max_iron = 0
    for chest in data:
        iron = chest['minecraft:iron_ingot'] if 'minecraft:iron_ingot' in chest else 0
        iron += chest['minecraft:iron_nugget'] // 9 if 'minecraft:iron_nugget' in chest else 0
        max_iron = max(max_iron, iron)
        iron_list.append(iron)
    return iron_list, max_iron

sw_iron, sw_max = count_iron(sw_data)
bt_iron, bt_max = count_iron(bt_data)

def write_histogram():
    global sw_iron, bt_iron, sw_max, bt_max
    sw_hist = Counter(sw_iron)
    bt_hist = Counter(bt_iron)
    with open('data.csv', 'w') as data_file:
        data_file.write('iron,shipwreck,buried_treasure\n')
        for i in range(max(sw_max, bt_max) + 1):
            data_file.write(f'{i},{sw_hist[i]},{bt_hist[i]}\n')

def write_stats():
    global sw_iron, bt_iron, sw_max, bt_max
    total_sw = sum(sw_iron)
    total_bt = sum(bt_iron)
    avg_sw = total_sw / len(sw_iron)
    avg_bt = total_bt / len(bt_iron)
    print("Shipwreck:")
    print("  Total:", total_sw)
    print("  Avg:", avg_sw)
    print("Buried Treasure:")
    print("  Total:", total_bt)
    print("  Avg:", avg_bt)

write_stats()
