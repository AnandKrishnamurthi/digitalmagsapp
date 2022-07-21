import tkinter as tk
from tkinter import ttk


class page():
    def switch(self):
        self.titlelbl = ttk.Label(self, text = "Timer",font = ("Arial",40,"bold"))
        self.titlelbl.place(x=375,y=50,anchor="center")