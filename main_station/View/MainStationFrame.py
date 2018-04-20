# The gui of the application

# Gui library
from tkinter import Tk, Label, Button
# Container to store variables that need to be accessed
import Model.Container as cnt
# For updating the view
import View.WindowUpdater as wdu

# Class that contains all the gui elements
class Main_Frame:
    def __init__(self, master):
        self.master = master
        master.title("Weather Station")

        cnt.time_label = Label(master, text="Time", font=("Helvetica", 45), bg = 'black', fg='white')
        cnt.time_label.place(relx=.5, rely=.3, anchor='center')
        #cnt.time_label.pack()

        cnt.temp_label = Label(master, text="Temp", font=("Helvetica", 45), bg = 'black', fg='white')
        cnt.temp_label.place(relx=.5, rely=.5, anchor='center')
        #cnt.temp_label.pack()

        cnt.humi_label = Label(master, text="Humi", font=("Helvetica", 45), bg = 'black', fg='white')
        cnt.humi_label.place(relx=.5, rely=.7, anchor='center')
        #cnt.humi_label.pack()

# Creating Tkinter view
root = Tk()
cnt.gui = Main_Frame(root)
root.attributes("-fullscreen", True)

root.configure(background='black')

# Connecting view to update function
wdu.update_window(root)
