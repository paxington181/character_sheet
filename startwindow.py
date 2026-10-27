import json
import customtkinter as CTk
import CTkToolTip as CTkTT
from PIL import Image

CTk.set_appearance_mode("dark")

class new_load(CTk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.new = CTk.CTkButton(self, text = "New", width = 97, command = None)
        self.new.pack(side = "left")
        self.load = CTk.CTkButton(self, text = "Load", width = 97, command = None)
        self.load.pack(side = "right")

    def load_character(self):
            with open("characters/Barbi McBarian.json", "r", encoding = "utf-8") as file:
            character = json.load(file)


class load_window(CTk.CTk):
    def __init__(self):
        super().__init__()

        self.title("D&D CSM")
        self.geometry("200x400")

        self.buttons_frame = new_load(self)
        self.buttons_frame.pack(side = "bottom")


app = load_window()
app.mainloop()