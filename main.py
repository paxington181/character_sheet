import json
import customtkinter as CTk
import CTkToolTip as CTkTT
from PIL import Image

class spells_frame(CTk.CTkFrame):
    def __init__(self, master, char_stats, caster_stats, proficiency_bonus, caster_level, prepared_spells, char_level):
        super().__init__(master)

class inventory_frame(CTk.CTkFrame):
    def __init__(self, master, char_stats, equipment):
        super().__init__(master)

class money_frame(CTk.CTkFrame):
    def __init__(self, master, money):
        super().__init__(master)

class other_abilities(CTk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

class class_abilities(CTk.CTkFrame):
    def __init__(self, master, char_level, char_class, class_level):
        super().__init__(master)

class feats_frame(CTk.CTkFrame):
    def __init__(self, master, feats):
        super().__init__(master)

class stat_frame(CTk.CTkFrame):
    def __init__(self, master, char_stats, save_proficencies, skills):
        super().__init__(master)        

class class_frame(CTk.CTkFrame):
    def __init__(self, master, char_class, char_subclass, species, class_level, background, char_name, play_name):
        super().__init__(master)

class system_frame(CTk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.save_char = None
        self.load_char = None

class Main(CTk.CTk):
    def __init__(self):
        super().__init__()

        self.title("D&D 2024 Character Sheet")
        self.geometry("100x100")

        self.char_name = None
        self.char_class = None
        self.char_subclass = None
        self.species = None
        self.size = None
        self.background = None
        self.char_level = 0
        self.experience = 0
        self.class_level = [1]
        self.max_hp = 0
        self.current_hp = 0
        self.temp_hp = 0
        self.hit_dice = ["1d12"]
        self.proficiency_bonus = 2
        self.save_proficencies = []
        self.char_stats = None
        self.skills = None
        self.feats = ["magic initiate"]
        self.caster_stats = ["wis"]
        self.caster_level = 1
        self.prepared_spells = []
        self.equipment = []
        self.heroic_insp = True

        self.load = CTk.CTkButton(self, text = "Load Character", command = self.load_character)
        self.load.pack()

    def set_filetoload():
        pass

    def load_character(self):
        with open("characters/Barbi McBarian.json", "r", encoding = "utf-8") as file:
            character = json.load(file)
        self.skills = character["skills"]
        self.char_name = character["char_name"]
        self.char_class = character["char_class"]["barbarian"]
        self.char_subclass = character["char_class"]
        self.species = character["species"]
        self.background = character["background"]
        print(self.char_name)
        print(self.char_subclass)
        print(self.species)
        print(self.background)
        

sheet = Main()
sheet.mainloop()