import customtkinter as ctk

def open_new_window():
    
    new_window = ctk.CTkToplevel(app)
    new_window.title("Secondary Window")
    new_window.geometry("300x200")
    
    
    new_window.attributes("-topmost", True)

    label = ctk.CTkLabel(new_window, text="This is a new window!")
    label.pack(pady=20)


app = ctk.CTk()
app.title("Main Window")
app.geometry("400x300")


open_button = ctk.CTkButton(app, text="Open Window", command=open_new_window)
open_button.pack(pady=40)

app.mainloop()
