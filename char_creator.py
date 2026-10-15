import json
import customtkinter as CTk
import CTkToolTip as CTkTT
from PIL import Image

CTk.set_appearance_mode("dark")


class char_create(CTk.CTk):
    def __init__(self):
        super().__init__()

        self.title("New Character")
        self.geometry("700x700")

        


app = char_create()
app.mainloop()