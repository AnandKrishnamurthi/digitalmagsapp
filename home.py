import tkinter as tk
from tkinter import ttk
import webbrowser
from PIL import Image, ImageTk


class page:
    def switch(self):
        self.title_label = ttk.Label(
            self, text="Work Assist App", font=("Arial", 40, "bold")
        )
        self.title_label.place(x=375, y=50, anchor="center")

        # Left side
        self.welcomeimg = self.resizeimage("title", 185, 100)
        self.welcomeimg_label = ttk.Label(self, image=self.welcomeimg)
        self.welcomeimg_label.place(x=30, y=100)

        self.gmailicon = self.resizeimage("gmail", 32, 32)
        self.gmailbutton = ttk.Button(
            self,
            compound="right",
            text="Gmail ",
            image=self.gmailicon,
            command=lambda: webbrowser.open_new_tab("https://gmail.com/"),
        )
        self.gmailbutton.place(x=30, y=210, width=210, height=45)

        self.driveicon = self.resizeimage("drive", 32, 32)
        self.drivebutton = ttk.Button(
            self,
            compound="right",
            text="Google Drive ",
            image=self.driveicon,
            command=lambda:
                webbrowser.open_new_tab("https://drive.google.com/"),
        )
        self.drivebutton.place(x=30, y=270, width=210, height=45)

        self.classroomicon = self.resizeimage("classroom", 50, 32)
        self.classroombutton = ttk.Button(
            self,
            compound="right",
            text="Google Classroom ",
            image=self.classroomicon,
            command=lambda:
                webbrowser.open_new_tab("https://classroom.google.com/"),
        )
        self.classroombutton.place(x=30, y=330, width=210, height=45)

        self.teamsicon = self.resizeimage("teams", 32, 32)
        self.teamsbutton = ttk.Button(
            self,
            compound="right",
            text="Microsoft Teams ",
            image=self.teamsicon,
            command=lambda: webbrowser.open_new_tab("https://teams.com/"),
        )
        self.teamsbutton.place(x=30, y=390, width=210, height=45)

        # Right side

        self.subjectsbutton = ttk.Button(
            self,
            text="Subjects List",
            style="big.TButton",
            command=lambda: self.change_to_page(2),
        )
        self.subjectsbutton.place(x=280, y=110, width=420, height=70)
        self.timerbutton = ttk.Button(
            self,
            text="Work Timer",
            style="big.TButton",
            command=lambda: self.change_to_page(1),
        )
        self.timerbutton.place(x=280, y=205, width=420, height=70)
        self.togglethemebutton = ttk.Button(
            self,
            text="Toggle Theme",
            style="big.TButton",
            command=lambda: self.svtk.toggle_theme(),
        )  # toggle theme function
        self.togglethemebutton.place(x=280, y=300, width=420, height=70)
        self.quitbutton = ttk.Button(
            self, text="Quit", style="big.TButton", command=lambda: self.quit()
        )
        self.quitbutton.place(x=280, y=395, width=420, height=70)
