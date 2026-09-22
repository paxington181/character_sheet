import json

barbarian = dict(primary_ability = "strength", hit_dice = "1d12", saves = ["str", "con"], weapon_prof = ["simple", "martial"], armor_prof = ["light", "medium", "shield"],
                 start_equip = dict(A = ["greataxe", "handaxe", "handaxe", "handaxe", "handaxe", ("GP", 15)], B = [("GP", 75)]),
                 lvl_1 = dict(features = ["rage", "unarmored defense", "weapon mastery"], rages = 2, rage_damage = 2, weap_mast = 2),
                 lvl_2 = dict(features = ["danger sense", "reckless attack"], rages = 2, rage_damage = 2, weap_mast = 2),
                 lvl_3 = dict(features = ["barbarian subclass", "primal knowledge"], rages = 3, rage_damage = 2, weap_mast = 2),
                 lvl_4 = dict(features = ["ability score improvement"], rages = 3, rage_damage = 2, weap_mast = 3),
                 lvl_5 = dict(features = ["extra attack", "fast movement"], rages = 3, rage_damage = 2, weap_mast = 3),
                 lvl_6 = dict(features = ["subclass feature"], rages = 4, rage_damage = 2, weap_mast = 3),
                 lvl_7 = dict(features = ["feral instinct", "instinctive pounce"], rages = 4, rage_damage = 2, weap_mast = 3),
                 lvl_8 = dict(features = ["ability score improvement"], rages = 4, rage_damage = 2, weap_mast = 3),
                 lvl_9 = dict(features = ["brutal strike"], rages = 4, rage_damage = 3, weap_mast = 3),
                 lvl_10 = dict(features = ["subclass feature"], rages = 4, rage_damage = 3, weap_mast = 4),
                 lvl_11 = dict(features = ["relentless rage"], rages = 4, rage_damage = 3, weap_mast = 4),
                 lvl_12 = dict(features = ["ability score improvement"], rages = 5, rage_damage = 3, weap_mast = 4),
                 lvl_13 = dict(features = ["improved brutal strike"], rages = 5, rage_damage = 3, weap_mast = 4),
                 lvl_14 = dict(features = ["subclass feature"], rages = 5, rage_damage = 3, weap_mast = 4),
                 lvl_15 = dict(features = ["persistent rage"], rages = 5, rage_damage = 3, weap_mast = 4),
                 lvl_16 = dict(features = ["ability score improvement"], rages = 5, rage_damage = 4, weap_mast = 4),
                 lvl_17 = dict(features = ["improved brutal strike"], rages = 6, rage_damage = 4, weap_mast = 4),
                 lvl_18 = dict(features = ["indomitable might"], rages = 6, rage_damage = 4, weap_mast = 4),
                 lvl_19 = dict(features = ["epic boon"], rages = 6, rage_damage = 4, weap_mast = 4),
                 lvl_20 = dict(features = ["primal champion"], rages = 6, rage_damage = 4, weap_mast = 4)
                 )
with open("barbarian.json", "w", encoding = "utf-8") as f:
    json.dump(barbarian, f, indent = 4)