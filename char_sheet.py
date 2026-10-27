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

class char_sheet(CTk.CTk):
    def __init__(self, character):
        super().__init__()

        self.title("D&D 2024 Character Sheet")
        self.geometry("100x100")

        self.player_name = character["player_name"]
        self.char_name = None
        self.char_class = None
        self.char_subclass = None
        self.species = None
        self.size = None
        self.background = None
        self.char_level = 0
        self.experience = 0
        self.class_level = []
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


    def process_class(self, char_classes):
        for i in char_classes:
            print(i)
        

sheet = char_sheet()
sheet.mainloop()