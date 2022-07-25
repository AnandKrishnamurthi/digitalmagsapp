import tkinter as tk
from tkinter import ttk
import os

class page():
    def switch(self):
        #back to home button
        self.backtohome = ttk.Button(self, text="Back", command=lambda: self.change_to_page(0))
        self.backtohome.place(x=20,y=20,anchor="nw")
        #gets the name of each file
        self.subject_names = []
        for (x, y, file_names) in os.walk("./subjects/"):
            self.subject_names.extend(file_names)
        #removes the .txt for display from the file name
        for i in range(len(self.subject_names)):
            self.subject_names[i] = self.subject_names[i].replace(".txt","")
        
        self.title_label = ttk.Label(self, text = "Subjects",font = ("Arial",40,"bold"))
        self.title_label.place(x=375,y=50,anchor="center")

        #makes a frame with two columns for all of the subject buttons
        self.frame1 = ttk.Frame(self)
        self.frame1.columnconfigure(index=0, weight=1)
        self.frame1.columnconfigure(index=1, weight=1)
        
        self.frame1.place(x=375,y=100,anchor="n")
        
        self.listforbuttons = [] #make empty list for subject buttons
        x,y = 0,0
        for i in range(len(self.subject_names)): #for loop runs for the length of the list of all of the subject files
            self.listforbuttons.append(ttk.Button(self.frame1,style="big.TButton",text=self.subject_names[i].capitalize(),command=lambda name=self.subject_names[i]: self.show_subject_list(name)))
            self.listforbuttons[i].grid(row=y,column=x,pady=20,padx=10) #padding for spaces to make it look cleaner
            x+=1 
            if x == 2: #when x goes above 1, reset to place the third item in the first column
                x = 0
                y += 1 #goes down by 1 when x goes above 1
        self.addsubj_button = ttk.Button(self.frame1,style="big.TButton",text="Add Subject",command=lambda: self.change_to_page(3))
        self.addsubj_button.grid(row=y,column=x,pady=20,padx=1) #keeps the add subject button at the end
