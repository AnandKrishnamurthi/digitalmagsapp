import tkinter as tk
from tkinter import ttk
import time #time library allows wait time
import os #used to get file names
# Tkinter pages
import home
import timer
import subjects
import createsubject
import customsubjectpage
# External
from PIL import Image, ImageTk #putting images into app
import sv_ttk #d/l mode
from playsound import playsound #plays sound

"""
User will need to download external libraries from PIP
pip install playsound
pip install pillow
pip install sv_ttk
(On mac)- pip install PyObjC
"""


class App(ttk.Frame):
    #closes app
    def quit(self):
        global mytkinter
        print("Quitting app")
        mytkinter.quit()

    def __init__(self, parent):
        ttk.Frame.__init__(self)
        self.svtk = sv_ttk #allows themes in class
        #pages to be used that require d/l mode
        self.pages = [
            home.page,
            timer.page,
            subjects.page,
            createsubject.page,
            customsubjectpage.page]
        #to make buttons bigger
        self.appstyles = ttk.Style()
        sv_ttk.use_light_theme()
        self.appstyles.configure('big.TButton', font=(None, 25)) #makes font bigger
        sv_ttk.use_dark_theme()
        self.appstyles.configure('big.TButton', font=(None, 25))
        self.timerpaused = False
        self.pages[0].switch(self) #start at page 0 - home page

        #current page is destroyed, requested page is switched to
    def change_to_page(self, wanted_page_number):
        for widget in self.winfo_children():
            widget.destroy()
        self.pages[wanted_page_number].switch(self) #creates next page

        #changing image sizes
    def resizeimage(self,name,x,y):
        self.image = Image.open('./images/' + name + '.png')
        self.image = self.image.resize((x,y), Image.Resampling.LANCZOS)
        return ImageTk.PhotoImage(self.image)

        #shows the name of the subject, reads corresponding file and returns contents
    def show_subject_list(self,subname):
        self.current_subject = subname
        f = open("./subjects/"+subname.lower() + ".txt", "r") #opens subject file
        self.file_contents = ""
        for line in f:
            self.file_contents += line #saves each line in the file
        f.close()
        self.change_to_page(4) #changes to note writing page
        
        #creates the text file in the subject folder for 'subname'
    def create_subject_file(self, subname):
        try:
            self.temp = []
            for (x, y, file_names) in os.walk("./subjects/"): #gets the name of each file in the subjects folder
                self.temp.extend(file_names)
            for i in self.temp:
                if subname.lower() in i: #checks for existing file with the same name
                    print("Subject already exists")
                    raise ValueError("Subject already exists") #raises value error if there is a file with the same name
                    
            print("Creating subject file for " + subname)
            f = open("./subjects/"+subname.lower() + ".txt", "w+") #creates and empty text file named after the subject
            f.close()
            self.change_to_page(2) #goes back to the subject page
        except:
            print("Error creating subject file, try a normal subject name")

    def update_subject_list(self, subname, contents): #gets subject name and written contents of the file
        f = open("./subjects/"+subname.lower() + ".txt", "w") #opens corresponding file in write mode
        f.write(contents) #writes
        f.close() #closes file
        print(subname, "updated")
        self.change_to_page(2) #goes back to subject list page

    #function for deletion of subject files
    def delete_subject_file(self, subname):
        self.number_of_times_del_clicked += 1 #when delete button clicked, it will add 1
        if(self.number_of_times_del_clicked >= 2): #detects when delete clicked 2 or more times
            os.remove("./subjects/"+subname.lower() + ".txt") #removes file
            print(subname, "deleted")
            self.change_to_page(2) #goes back to subject page
            self.number_of_times_del_clicked = 0 #resets amount of times clicked
        else: #if button clicked the first time, will make new button with "Confirm?" text instead of delete
            self.deleteimg = self.resizeimage('trash', 24, 24)
            self.deleteBtn = ttk.Button(self,text="Confirm?", compound="right", image = self.deleteimg, command=lambda: self.delete_subject_file(self.current_subject))
            self.deleteBtn.place(x=720,y=400,anchor="ne")

    def resetTimer(self):
        self.userexit = True
        self.temp = 0
        self.timerpaused = False
        self.change_to_page(1)

    def pauseTimer(self):
        self.timerpaused = True
        self.remindervar.set("Paused")

    
    def timer(self):
        global mytkinter
        if(self.timerpaused == False):
            try:
                if int(self.hour.get()) < 0:
                    raise TypeError
                if int(self.minute.get()) < 0:
                    raise TypeError
                if int(self.second.get()) < 0:
                    raise TypeError
                self.userexit = False
                self.temp = int(self.hour.get())*3600 + int(self.minute.get())*60 + int(self.second.get())
            except TypeError as e:
                print("Time can not be negative")
                self.temp = -1
                self.remindervar.set("Time can not be negative")
            except Exception as e:
                print("Invalid value(s) for timer!")
                self.temp = -1
                self.remindervar.set("Invalid value(s) for timer!")
        else:
            self.timerpaused = False            
        while self.temp > -1:
            self.remindervar.set("Remember to take a break every 60 mintues!")
            self.mins,self.secs = divmod(self.temp,60)
            self.hours=0
            if self.mins >60:
                self.hours, self.mins = divmod(self.mins, 60)
            self.hour.set("{0:2d}".format(self.hours))
            self.minute.set("{0:2d}".format(self.mins))
            self.second.set("{0:2d}".format(self.secs))
            for i in range(10):
                mytkinter.update()
                time.sleep(0.1)
            if (self.temp == 0 and self.userexit == False):
                self.remindervar.set("Timer finished!")
                print("Timer done", "app frozen while playing sound")
                playsound('timer.mp3')
                self.change_to_page(0)
            elif(self.temp == 0 and self.userexit == True):
                print("Timer exited early")
            self.temp -= 1
            if self.timerpaused == True:
                break
mytkinter = tk.Tk()
mytkinter.title("Anand's Digital App")
tkapp = App(mytkinter)
tkapp.pack(fill="both", expand=True)
mytkinter.geometry("750x500")
mytkinter.mainloop()

