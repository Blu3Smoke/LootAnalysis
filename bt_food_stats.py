import json
import math
from collections import Counter

with open('buried_treasure.json') as sw_file:
    sw_data = json.load(sw_file)

def count_chest_item(item, chest):
    item_name = 'minecraft:' + item
    return chest[item_name] if item_name in chest else 0

values = {
    'cod': [5, 6, 11],
    'salmon': [6, 9.6, 15.6]
}

food = {
    'hunger': [],
    'saturation': [],
    'quality': []
}

for chest in sw_data:
    cod = count_chest_item('cooked_cod', chest)
    salmon = count_chest_item('cooked_salmon', chest)
    food['hunger'].append(cod * values['cod'][0] + salmon * values['salmon'][0])
    food['saturation'].append(cod * values['cod'][1] + salmon * values['salmon'][1])
    food['quality'].append(cod * values['cod'][2] + salmon * values['salmon'][2])

def write_histogram():
    global food
    for f in food.keys():
        hist = Counter(food[f])
        with open((f'bt_{f}_data.csv'), 'w') as data_file:
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
