import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk


class page():
    def switch(self):
        self.number_of_times_del_clicked = 0 #when page created, number of times delete clicked is set to 0
        self.backtosubjects = ttk.Button(self, text="Back", command=lambda: self.change_to_page(2))
        self.backtosubjects.place(x=20,y=20,anchor="nw")

        self.titlelbl = ttk.Label(self, text = self.current_subject.capitalize(), font=("Arial",40,"bold"))
        self.titlelbl.place(x=375,y=15,anchor="n")

        self.text_box = tk.Text(self,height=17,width=70,wrap='word',relief="groove",borderwidth=2, font=("None",16))
        self.text_box.insert('end', self.file_contents) #insert all saved data from the relevant text file into the text box
        self.text_box.place(x=375,y=80,anchor="n")

        self.updatebtn = ttk.Button(self,style="big.TButton",text="Enter",command=lambda: self.update_subject_list(self.current_subject, self.text_box.get('1.0', 'end')))
        self.updatebtn.place(x=375,y=400,anchor="n")

        self.deleteimg = self.resizeimage('trash', 24, 24)
        self.deleteBtn = ttk.Button(self,text="Delete", compound="right", image = self.deleteimg, command=lambda: self.delete_subject_file(self.current_subject))
        self.deleteBtn.place(x=720,y=400,anchor="ne")
