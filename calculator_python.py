import tkinter as tk#tkinter modules as tk anothername
from tkinter import *#all the libraries,modules are imported
import tkinter.messagebox#seperate submodule messagebox gives functions for giving various user messages
from tkinter.constants import SUNKEN#import a specific constant

win = tk.Tk()#create the main window of application
win.title('Calculator')#given the title of window

frame = tk.Frame(win, bg="skyblue", padx=10)
frame.pack()#create a frame widget with skyblue colour above main window

entry = tk.Entry(frame, relief=SUNKEN, borderwidth=3, width=30)#Entry widget placed inside frame widget,a single line text input field
entry.grid(row=0, column=0, columnspan=3, ipady=2, pady=2)

def click(num):
    entry.insert(tk.END, num)

def equal():
    try:
        res = str(eval(entry.get()))
        entry.delete(0, tk.END)
        entry.insert(0, res)
    except:
        tk.messagebox.showinfo("Error", "Syntax Error")

win.mainloop()