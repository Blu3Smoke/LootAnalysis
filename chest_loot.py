import json
import random

# Unzip the 1.16.1 jar inside your .minecraft/versions folder, and
# put the contents in a folder "unzipped" there. Then change
# the MC_DIR variable below to your .minecraft folder path
MC_DIR = "/Users/bluesmoke/Library/Application Support/minecraft"
BASE_PATH = f"{MC_DIR}/versions/1.16.1/unzipped/data/minecraft/loot_tables/chests/";

def get_loot_table(name):
    with open(BASE_PATH + name + ".json") as lt:
        return json.load(lt)

def find_idx(weights, num):
    for idx, weight in enumerate(weights):
        if num <= weight:
            return idx
    return -1

def generate_loot(loot_table):
    result = {}
    for pool in loot_table['pools']:
        rolls = 0
        if type(pool['rolls']) == int:
            rolls = pool['rolls']
        else:
            min_rolls, max_rolls = pool['rolls']['min'], pool['rolls']['max']
            rolls = random.randint(min_rolls, max_rolls)
        w = 0
        weights = [w := w + (e['weight'] if 'weight' in e else 1) for e in pool['entries']]
        for i in range(rolls):
            entry = pool['entries'][find_idx(weights, random.randint(1, w))]
            item_count = 1
            if "functions" in entry:
                for function in entry["functions"]:
                    if function["function"] == "minecraft:set_count":
                        count = function['count']
                        min_count, max_count = count['min'], count['max']
                        item_count = random.randint(min_count, max_count)
                        break
            if entry['name'] in result:
                result[entry['name']] += item_count
            else:
                result[entry['name']] = item_count
    return result

ship = get_loot_table("shipwreck_treasure")
ship_food = get_loot_table("shipwreck_supply")
bt = get_loot_table("buried_treasure")

ship_total = []
ship_food_total = []
bt_total = []
for i in range(1_000_000):
    ship_total.append(generate_loot(ship))
    ship_food_total.append(generate_loot(ship_food))
    bt_total.append(generate_loot(bt))
    if i % 10_000 == 0:
        print(i)

with open('shipwreck.json', 'w') as sf:
    json.dump(ship_total, sf)
with open('shipwreck_food.json', 'w') as sff:
    json.dump(ship_food_total, sff)
with open('shipwreck_food.json', 'w') as bf:
    json.dump(bt_total, bf)
