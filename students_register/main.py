from customtkinter import CTk
import customtkinter as ctk
from frames.mainFram import MainFram
from database.db import create_table
from utils.conponets import center_window


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")  
class App(CTk):
    def __init__(self):
        super().__init__()
    
        self.title("Student registe")
        self.resizable(False, False)
        center_window(self,1000,600)
        self.frame = MainFram(self)
        self.frame.pack()


if __name__ == "__main__":
    create_table()
    app = App()
    app.mainloop()