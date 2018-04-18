# The gui of the application

# Gui library
from tkinter import Tk, Label, Button

# Class that contains all the gui elements
class Main_Frame:
    def __init__(self, master):
        self.master = master
        master.title("Weather Station")

        self.label = Label(master, text="This is the Weather Station!")
        self.label.pack()

        self.greet_button = Button(master, text="Test", command=self.greet)
        self.greet_button.pack()

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()

    def greet(self):
        print("Test")

root = Tk()
my_gui = Main_Frame(root)
root.attributes("-fullscreen", True)
root.mainloop()
