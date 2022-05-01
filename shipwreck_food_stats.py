import json
import math
from collections import Counter

with open('shipwreck_food.json') as sw_file:
    sw_data = json.load(sw_file)

def count_chest_item(item, chest):
    item_name = 'minecraft:' + item
    return chest[item_name] if item_name in chest else 0

values = {
    'bread': [5, 6, 11],
    'stew': [6, 7.2, 13.2],
    'carrot': [3, 3.6, 6.6],
    'flesh': [4, 0.8, 4.8]
}

food = {
    'hunger': [],
    'saturation': [],
    'quality': []
}

for chest in sw_data:
    bread = count_chest_item('wheat', chest) // 3
    stew = count_chest_item('suspicious_stew', chest)
    carrot = count_chest_item('carrot', chest)
    flesh = count_chest_item('rotten_flesh', chest)
    hunger = bread * values['bread'][0] + stew * values['stew'][0] + carrot * values['carrot'][0] + flesh * values['flesh'][0]
    saturation = bread * values['bread'][1] + stew * values['stew'][1] + carrot * values['carrot'][1] + flesh * values['flesh'][1]
    quality = bread * values['bread'][2] + stew * values['stew'][2] + carrot * values['carrot'][2] + flesh * values['flesh'][2]
    food['hunger'].append(hunger)
    food['saturation'].append(round(saturation, 2))
    food['quality'].append(round(quality, 2))

def write_histogram():
    global food
    for f in food.keys():
        hist = Counter(food[f])
        with open(f'ship_{f}_data.csv', 'w') as data_file:
            data_file.write(f'{f},frequency\n')
            for x in set(food[f]):
                data_file.write(f'{x},{hist[x]}\n')

def write_stats():
    global food
    for f in food.keys():
        total_food = sum(food[f])
        avg_food = total_food / len(food[f])
        std_dev_food = math.sqrt(sum(map(lambda x: (x-avg_food)**2, food[f])) / len(food[f]))
        print(f'average {f}: {avg_food}')
        print(f'stddev {f}: {std_dev_food}')

write_histogram()
write_stats()
