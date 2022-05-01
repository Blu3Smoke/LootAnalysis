import json
from collections import Counter

with open('shipwreck.json') as sw_file:
    sw_data = json.load(sw_file)
with open('buried_treasure.json') as bt_file:
    bt_data = json.load(bt_file)

def count_gold(data):
    gold_list = []
    max_gold = 0
    for chest in data:
        gold = chest['minecraft:gold_ingot'] if 'minecraft:gold_ingot' in chest else 0
        gold += chest['minecraft:gold_nugget'] // 9 if 'minecraft:gold_nugget' in chest else 0
        max_gold = max(max_gold, gold)
        gold_list.append(gold)
    return gold_list, max_gold

sw_gold, sw_max = count_gold(sw_data)
bt_gold, bt_max = count_gold(bt_data)

def write_histogram():
    global sw_gold, bt_gold, sw_max, bt_max
    sw_hist = Counter(sw_gold)
    bt_hist = Counter(bt_gold)
    with open('gold_data.csv', 'w') as data_file:
        data_file.write('gold,shipwreck,buried_treasure\n')
        for i in range(max(sw_max, bt_max) + 1):
            data_file.write(f'{i},{sw_hist[i]},{bt_hist[i]}\n')

def write_stats():
    global sw_gold, bt_gold, sw_max, bt_max
    total_sw = sum(sw_gold)
    total_bt = sum(bt_gold)
    avg_sw = total_sw / len(sw_gold)
    avg_bt = total_bt / len(bt_gold)
    print("Shipwreck:")
    print("  Total:", total_sw)
    print("  Avg:", avg_sw)
    print("Buried Treasure:")
    print("  Total:", total_bt)
    print("  Avg:", avg_bt)

write_histogram()
write_stats()
