// this isn't on fucking NPM
const getPotentialDrops = require("prismarine-loottable").getPotentialDrops;
const BASE_PATH = "/Users/tarunbod/Library/Application Support/minecraft/versions/1.16.1/unzipped/data/minecraft/loot_tables/chest/";

function getLootTable(name) {
    return require(BASE_PATH + name + ".json");
}

const lootTable = getLootTable("shipwreck_treasure");
const drops = getPotentialDrops(lootTable);

console.log(JSON.toString(drops));
