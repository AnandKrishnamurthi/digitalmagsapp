import tkinter as tk
from tkinter import ttk
import os

class page():
    def switch(self):
        self.backtohome = ttk.Button(self, text="Back", command=lambda: self.change_to_page(0))
        self.backtohome.place(x=20,y=20,anchor="nw")
        self.subject_names = []
        for (x, y, file_names) in os.walk("./subjects/"):
            self.subject_names.extend(file_names)
        for i in range(len(self.subject_names)):
            self.subject_names[i] = self.subject_names[i].replace(".txt","")
        
        self.titlelbl = ttk.Label(self, text = "Subjects",font = ("Arial",40,"bold"))
        self.titlelbl.place(x=375,y=50,anchor="center")

        self.frame1 = ttk.Frame(self)
        self.frame1.columnconfigure(index=0, weight=1)
        self.frame1.columnconfigure(index=1, weight=1)
        self.frame1.place(x=375,y=100,anchor="n")
        self.listforbtn = []
        x,y = 0,0
        for i in range(len(self.subject_names)):
            self.listforbtn.append(ttk.Button(self.frame1,style="big.TButton",text=self.subject_names[i].capitalize(),command=lambda name=self.subject_names[i]: self.show_subject_list(name)))
            self.listforbtn[i].grid(row=y,column=x,pady=20,padx=10)
            x+=1
            if x == 2:
                x = 0
                y += 1
        self.addsubjbtn = ttk.Button(self.frame1,style="big.TButton",text="Add List",command=lambda: self.change_to_page(3))
        self.addsubjbtn.grid(row=y,column=x,pady=20,padx=1)