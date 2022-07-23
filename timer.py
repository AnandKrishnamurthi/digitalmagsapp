import tkinter as tk
from tkinter import ttk


class page():
    def switch(self):
        self.backtohome = ttk.Button(self, text="Back", command=lambda: self.change_to_page(0))
        self.backtohome.place(x=20,y=20,anchor="nw")
        
        self.titlelbl = ttk.Label(self, text = "Timer",font = ("Arial",40,"bold"))
        self.titlelbl.place(x=375,y=50,anchor="center")

        self.hour=tk.StringVar()
        self.minute=tk.StringVar()
        self.second=tk.StringVar()

        self.hour.set("00")
        self.minute.set("00")
        self.second.set("00")

        self.colonlbl1 = ttk.Label(self, text = ":",font = ("Arial",90,"bold"))
        self.colonlbl1.place(x=292,y=195,anchor="center")
        self.colonlbl2 = ttk.Label(self, text = ":",font = ("Arial",90,"bold"))
        self.colonlbl2.place(x=459,y=195,anchor="center")

        self.hourEntry= ttk.Entry(self, width=2, font=("Arial",100,"bold"),
                        textvariable=self.hour)
        self.hourEntry.place(x=270,y=200,anchor="e")
        self.hourhintlbl = ttk.Label(self, text = "(Hours)",font = ("Arial",10))
        self.hourhintlbl.place(x=205,y=125,anchor="center")
        
        self.minuteEntry= ttk.Entry(self, width=2, font=("Arial",100,"bold"),
                        textvariable=self.minute)
        self.minuteEntry.place(x=375,y=200,anchor="center")
        self.hourhintlbl = ttk.Label(self, text = "(Mintues)",font = ("Arial",10))
        self.hourhintlbl.place(x=375,y=125,anchor="center")

        self.secondEntry= ttk.Entry(self, width=2, font=("Arial",100,"bold"),
                    textvariable=self.second)
        self.secondEntry.place(x=480,y=200,anchor="w")
        self.hourhintlbl = ttk.Label(self, text = "(Seconds)",font = ("Arial",10))
        self.hourhintlbl.place(x=545,y=125,anchor="center")

        self.reminderlbl = ttk.Label(self, text = "Remember to take a break every 60 mintues!",font = ("Arial",16,"bold"))
        self.reminderlbl.place(x=375,y=310,anchor="center")

        self.startbtn = ttk.Button(self, text='Start',
                    command= self.timer, style="big.TButton")
        self.startbtn.place(x = 365,y = 350,anchor="ne")

        self.resetbtn = ttk.Button(
            self, text="Reset", style="big.TButton",
            command=lambda: self.resetTimer())
        self.resetbtn.place(x = 385,y = 350,anchor="nw")
