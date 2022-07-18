import tkinter as tk
from tkinter import ttk
import webbrowser
from PIL import Image, ImageTk


class tkpage():
    def switch(self):
        # Left side ------------------------------------------------------------
        self.welcomeimg = self.resizeimage('gmail', 80, 85)
        self.welcomeimglbl = ttk.Label(self, image = self.welcomeimg)
        self.welcomeimglbl.grid(row=1, column=0, pady=10, padx=10)

        self.gmailicon = self.resizeimage('gmail', 32, 32)
        self.gmailbtn = ttk.Button(
            self, compound="right",
            text='Gmail ', image=self.gmailicon,
            command=lambda: webbrowser.open_new_tab("https://gmail.com/"))
        self.gmailbtn.grid(row=2, column=0, pady=5, padx=10,sticky='nesw')
        
        self.driveicon = self.resizeimage('drive', 32, 32)
        self.drivebtn = ttk.Button(
            self, compound="right", 
            text='Google drive ', image=self.driveicon,
            command=lambda: webbrowser.open_new_tab("https://drive.google.com/"))
        self.drivebtn.grid(row=3, column=0, pady=5, padx=10,sticky='nesw')
        
        self.classroomicon = self.resizeimage('classroom', 32, 32)
        self.classroombtn = ttk.Button(
            self, compound="right", 
            text='Google classroom ', image=self.classroomicon,
            command=lambda: webbrowser.open_new_tab("https://classroom.google.com/"))
        self.classroombtn.grid(row=4, column=0, pady=5, padx=10,sticky='nesw')
        
        self.teamsicon = self.resizeimage('teams', 32, 32)
        self.teamsbtn = ttk.Button(
            self, compound="right", 
            text='Microsoft teams ', image=self.teamsicon,
            command=lambda: webbrowser.open_new_tab("https://teams.com/"))
        self.teamsbtn.grid(row=5, column=0, pady=5, padx=10,sticky='nesw')
        
        # Right side ---------------------------------------------------------
        self.titleimg = self.resizeimage('title', 300, 50)
        self.titlelbl = ttk.Label(self, image = self.titleimg)
        self.titlelbl.grid(row=1, column=1, columnspan=2, pady=5, padx=10)

        self.button = ttk.Button(
            self, text="Task list",style="big.TButton",
            command=lambda: self.changePage(1))
        self.button.grid(row=2, column=1, columnspan=2, pady=10 , padx=20,sticky='nesw')
        self.button = ttk.Button(
            self, text="Work timer",style="big.TButton",
            command=lambda: self.changePage(1))
        self.button.grid(row=3, column=1, columnspan=2, pady=10, padx=20,sticky='nesw')
        self.testbtn = ttk.Button(
            self, text="Toggle theme",style="big.TButton",
            command=lambda: self.svtk.toggle_theme())
        self.testbtn.grid(row=4, column=1, columnspan=2, pady=10, padx=20,sticky='nesw')
        self.testbtn = ttk.Button(
            self, text="Quit", style="big.TButton",
            command=lambda: self.quit())
        self.testbtn.grid(row=5, column=1, columnspan=2, pady=10, padx=20,sticky='nesw')
