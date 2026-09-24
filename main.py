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
    def __init__(self, master, char_class, char_subclass, species, class_level):
        super().__init__(master)

class Main(CTk.CTk):
    def __init__(self):
        super().__init__()

        self.title("D&D 2024 Character Sheet")
        self.geometry("100x100")

        self.char_class = ["barbarian"]
        self.char_subclass = None
        self.species = "human"
        self.size = "medium"
        self.background = "acolyte"
        self.char_level = 1
        self.experience = 0
        self.class_level = [1]
        self.max_hp = 13
        self.current_hp = 13
        self.temp_hp = 0
        self.hit_dice = ["1d12"]
        self.proficiency_bonus = 2
        self.save_proficencies = []
        self.char_stats = [15, 14, 13, 12, 10, 8]
        self.skills = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.feats = ["magic initiate"]
        self.caster_stats = ["wis"]
        self.caster_level = 1
        self.prepared_spells = []
        self.equipment = []
        self.heroic_insp = True

sheet = Main()
sheet.mainloop()