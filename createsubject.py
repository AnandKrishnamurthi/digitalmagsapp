import tkinter as tk
from tkinter import ttk


class page():
    def switch(self):
        self.backtosubjects = ttk.Button(self, text="Back", command=lambda: self.change_to_page(2))
        self.backtosubjects.place(x=20,y=20,anchor="nw")

        self.title_label = ttk.Label(self, text = "Add Subject",font = ("Arial",40,"bold"))
        self.title_label.place(x=375,y=50,anchor="center")
        
        self.subject_label = ttk.Label(self, text = "Subject:",font = ("Arial",20,"bold"))
        self.subject_label.place(x=275,y=150,anchor="center")

        self.subject_name = ttk.Entry(self)
        self.subject_name.place(x=475,y=150,anchor="center")

        self.addsubj_button = ttk.Button(self,style="big.TButton",text="Add Subject",command=lambda: self.create_subject_file(self.subject_name.get()))
        self.addsubj_button.place(x=375,y=250,anchor="center")
                
