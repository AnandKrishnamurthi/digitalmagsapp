import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import sv_ttk
import home


class App(ttk.Frame):
    def quit(self):
        global mytkinter
        print("Quitting app")
        mytkinter.quit()

    def __init__(self, parent):
        ttk.Frame.__init__(self)
        self.svtk = sv_ttk
        self.pages = [
            home.tkpage]
        self.appstyles = ttk.Style()
        sv_ttk.use_light_theme()
        self.appstyles.configure('big.TButton', font=(None, 25,"bold"))
        self.appstyles.configure('title.TButton', font=(None, 40,"bold"))
        sv_ttk.use_dark_theme()
        self.appstyles.configure('big.TButton', font=(None, 25,"bold"))
        self.appstyles.configure('title.TButton', font=(None, 40,"bold"))


        self.columnconfigure(index=0, weight=1)
        self.columnconfigure(index=1, weight=1)
        self.columnconfigure(index=2, weight=1)
        self.pages[0].switch(self)

    def change_to_page(self, wanted_page_number):
        for widget in self.winfo_children():
            widget.destroy()
        self.pages[wanted_page_number].switch(self)

    def resizeimage(self,name,x,y):
        self.image = Image.open('./images/' + name + '.png')
        self.image = self.image.resize((x,y), Image.Resampling.LANCZOS)
        return ImageTk.PhotoImage(self.image)

mytkinter = tk.Tk()
mytkinter.title("Anand's Digital App")
tkapp = App(mytkinter)
tkapp.pack(fill="both", expand=True)
mytkinter.geometry("750x500")
mytkinter.mainloop()

