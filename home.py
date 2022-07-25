import tkinter as tk
from tkinter import ttk
import webbrowser
from PIL import Image, ImageTk


class page():
    def switch(self):
        self.titlelbl = ttk.Label(self, text = "Title",font = ("Arial",40,"bold"))
        self.titlelbl.place(x=375,y=50,anchor="center")

        # Left side ------------------------------------------------------------
        self.welcomeimg = self.resizeimage('title', 210, 100)
        self.welcomeimglbl = ttk.Label(self, image = self.welcomeimg)
        self.welcomeimglbl.place(x=30,y=100)

        self.gmailicon = self.resizeimage('gmail', 32, 32)
        self.gmailbtn = ttk.Button(
            self, compound="right",
            text='Gmail ', image=self.gmailicon,
            command=lambda: webbrowser.open_new_tab("https://gmail.com/"))
        self.gmailbtn.place(x=30,y=210,width=210,height=45)
        
        self.driveicon = self.resizeimage('drive', 32, 32)
        self.drivebtn = ttk.Button(
            self, compound="right", 
            text='Google drive ', image=self.driveicon,
            command=lambda: webbrowser.open_new_tab("https://drive.google.com/"))
        self.drivebtn.place(x=30,y=270,width=210,height=45)
        
        self.classroomicon = self.resizeimage('classroom', 32, 32)
        self.classroombtn = ttk.Button(
            self, compound="right", 
            text='Google classroom ', image=self.classroomicon,
            command=lambda: webbrowser.open_new_tab("https://classroom.google.com/"))
        self.classroombtn.place(x=30,y=330,width=210,height=45)
        
        self.teamsicon = self.resizeimage('teams', 32, 32)
        self.teamsbtn = ttk.Button(
            self, compound="right", 
            text='Microsoft teams ', image=self.teamsicon,
            command=lambda: webbrowser.open_new_tab("https://teams.com/"))
        self.teamsbtn.place(x=30,y=390,width=210,height=45)
        
        # Right side

        self.subjectsbutton = ttk.Button(
            self, text="Subjects list",style="big.TButton",
            command=lambda: self.change_to_page(2))
        self.subjectsbutton.place(x=280,y=110,width=420,height=70)
        self.timerbutton = ttk.Button(
            self, text="Work timer",style="big.TButton",
            command=lambda: self.change_to_page(1))
        self.timerbutton.place(x=280,y=205,width=420,height=70)
        self.togglethemebutton = ttk.Button(
            self, text="Toggle theme",style="big.TButton",
            command=lambda: self.svtk.toggle_theme()) #toggle theme function
        self.togglethemebutton.place(x=280,y=300,width=420,height=70)
        self.quitbutton = ttk.Button(
            self, text="Quit", style="big.TButton",
            command=lambda: self.quit())
        self.quitbutton.place(x=280,y=395,width=420,height=70)
