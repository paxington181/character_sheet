import json

character = dict(
                player_name = "Testi McTesterson",
                char_name = "Barbi McBarian",
                char_class = [("barbarian", 1, None), ("fighter", 3, "battle master")], 
                xp = "2700",
                species = "human",
                background = "acolyte",
                stats = dict(str = 15, dex = 13, con = 14, int = 8, wis = 12, cha = 10),
                save_prof = ("strength", "constitution"),
                max_hp = 14,
                current_hp = 14,
                skills = ["insight", "religion", "animal handling", "athletics"],
                tools = ["calligrapher's supplies"],
                proficiencies = ["simple weapons", "martial weapons", "light armor", "medium armor", "shield"],
                feats = ["magic initiate"],
                languages = ["common", "goblin"],
                prepared_spells = dict(magic_initiate = ["wis", "druid", dict(cantrips = ["druidcraft", "elementalism"], one = ["animal friendship"])]),
                used_slots = dict(),
                equipment = dict(weapons = [("greataxe", 1), ("handaxe", 4)], other = [("calligrapher's supplies", 1), ("prayer book", 1), ("holy symbol", 1), ("parchment", 10)]),
                money = dict(platinum = 0, electrum = 0, gold = 23, silver = 0, copper = 0),
                heroic_inspiration = True,
                character_appearance = "Just an ugly little dude.  Like a squat little ball of angry muscle and bad attitude.",
                alignment = "chaotic good"
                )

with open("characters/Barbi McBarian.json", "w", encoding = "utf-8") as f:
    json.dump(character, f, indent = 4)