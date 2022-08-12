import tkinter as tk
from tkinter import ttk


class page:
    def switch(self):
        self.backtohome = ttk.Button(
            self, text="Back", command=lambda: self.change_to_page(0)
        )
        self.backtohome.place(x=20, y=20, anchor="nw")

        self.title_label = ttk.Label(self, text="Timer",
                                     font=("Arial", 40, "bold"))
        self.title_label.place(x=375, y=50, anchor="center")

        self.hour = tk.StringVar()
        self.minute = tk.StringVar()
        self.second = tk.StringVar()

        self.hour.set("00")
        self.minute.set("00")
        self.second.set("00")

        self.colon_label1 = ttk.Label(self, text=":",
                                      font=("Arial", 90, "bold"))
        self.colon_label1.place(x=292, y=195, anchor="center")
        self.colon_label2 = ttk.Label(self, text=":",
                                      font=("Arial", 90, "bold"))
        self.colon_label2.place(x=459, y=195, anchor="center")

        self.hourEntry = ttk.Entry(
            self,
            width=2,
            font=("Arial", 100, "bold"),  # text field
            textvariable=self.hour,
        )
        self.hourEntry.place(x=270, y=200, anchor="e")
        self.hour_label = ttk.Label(self, text="(Hours)", font=("Arial", 10))
        self.hour_label.place(x=205, y=125, anchor="center")

        self.minuteEntry = ttk.Entry(
            self,
            width=2,
            font=("Arial", 100, "bold"),  # text field
            textvariable=self.minute,
        )
        self.minuteEntry.place(x=375, y=200, anchor="center")
        self.minute_label = ttk.Label(self, text="(Mintues)",
                                      font=("Arial", 10))
        self.minute_label.place(x=375, y=125, anchor="center")

        self.secondEntry = ttk.Entry(
            self,
            width=2,
            font=("Arial", 100, "bold"),  # text field
            textvariable=self.second,
        )
        self.secondEntry.place(x=480, y=200, anchor="w")
        self.second_label = ttk.Label(self,
                                      text="(Seconds)", font=("Arial", 10))
        self.second_label.place(x=545, y=125, anchor="center")

        self.remindervar = tk.StringVar()
        self.remindervar.set("")
        self.reminder_label = ttk.Label(
            self, textvariable=self.remindervar, font=("Arial", 16, "bold")
        )
        self.reminder_label.place(x=375, y=310, anchor="center")

        self.startbutton = ttk.Button(
            self, text="Start", command=self.timer, style="big.TButton"
        )
        self.startbutton.place(x=320, y=350, anchor="ne")

        self.resetbutton = ttk.Button(
            self, text="Reset", style="big.TButton",
            command=lambda: self.resetTimer()
        )
        self.resetbutton.place(x=375, y=350, anchor="n")

        self.pausebutton = ttk.Button(
            self, text="Pause", style="big.TButton",
            command=lambda: self.pauseTimer()
        )
        self.pausebutton.place(x=430, y=350, anchor="nw")

        
