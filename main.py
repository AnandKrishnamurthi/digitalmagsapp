import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import os
import sv_ttk
import home, timer, subjects, createsubject, customsubjectpage

class App(ttk.Frame):
    def quit(self):
        global mytkinter
        print("Quitting app")
        mytkinter.quit()

    def __init__(self, parent):
        ttk.Frame.__init__(self)
        self.svtk = sv_ttk
        self.pages = [
            home.page,
            timer.page,
            subjects.page,
            createsubject.page,
            customsubjectpage.page]
        self.appstyles = ttk.Style()
        sv_ttk.use_light_theme()
        self.appstyles.configure('big.TButton', font=(None, 25))
        sv_ttk.use_dark_theme()
        self.appstyles.configure('big.TButton', font=(None, 25))

        self.pages[0].switch(self)

    def change_to_page(self, wanted_page_number):
        for widget in self.winfo_children():
            widget.destroy()
        self.pages[wanted_page_number].switch(self)

    def resizeimage(self,name,x,y):
        self.image = Image.open('./images/' + name + '.png')
        self.image = self.image.resize((x,y), Image.Resampling.LANCZOS)
        return ImageTk.PhotoImage(self.image)

    def show_subject_list(self,subname):
        self.current_subject = subname
        f = open("./subjects/"+subname.lower() + ".txt", "r")
        self.file_contents = ""
        for line in f:
            self.file_contents += line
        f.close()
        self.change_to_page(4)
        
    def create_subject_file(self, subname):
        self.temp = []
        for (x, y, file_names) in os.walk("./subjects/"):
            self.temp.extend(file_names)
        for i in self.temp:
            if subname.lower() in i:
                print("Subject already exists")
                raise ValueError("Subject already exists")
                
        print("Creating subject file for " + subname)
        f = open("./subjects/"+subname.lower() + ".txt", "w+")
        f.close()
        self.change_to_page(2)


    def update_subject_list(self, subname, contents):
        f = open("./subjects/"+subname.lower() + ".txt", "w")
        f.write(contents)
        f.close()
        print(subname, "updated")
        self.change_to_page(2)


    def delete_subject_file(self, subname):
        self.number_of_times_del_clicked += 1
        if(self.number_of_times_del_clicked >= 2):
            os.remove("./subjects/"+subname.lower() + ".txt")
            print(subname, "deleted")
            self.change_to_page(2)
            self.number_of_times_del_clicked = 0
        else:
            self.deleteimg = self.resizeimage('trash', 24, 24)
            self.deleteBtn = ttk.Button(self,text="Confirm?", compound="right", image = self.deleteimg, command=lambda: self.delete_subject_file(self.current_subject))
            self.deleteBtn.place(x=720,y=400,anchor="ne")

mytkinter = tk.Tk()
mytkinter.title("Anand's Digital App")
tkapp = App(mytkinter)
tkapp.pack(fill="both", expand=True)
mytkinter.geometry("750x500")
mytkinter.mainloop()

