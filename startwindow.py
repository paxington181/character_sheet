import json
import customtkinter as CTk
import CTkToolTip as CTkTT
from PIL import Image

class new_load(CTk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.new = CTk.CTkButton(self, text = "New", width = 95, command = None)
        self.new.pack(side = "left")
        self.load = CTk.CTkButton(self, text = "Load", width = 95, command = None)
        self.load.pack(side = "right")


class load_window(CTk.CTk):
    def __init__(self):
        super().__init__()

        self.title("D&D 2024 Character Sheet Manager")
        self.geometry("200x400")

        self.buttons_frame = new_load(self)
        self.buttons_frame.pack(side = "bottom")


app = load_window()
app.mainloop()