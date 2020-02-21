import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

#creating frame
frame = tk.Tk()
frame.geometry("600x400")

#event funtion
def progress():
    'to update progress'
    for i in range(1001):
        #update progress value
        pbar["value"] = i
        lbl["text"] = i
        pbar.update()
    else:
        messagebox.showinfo("INFO","Loop Completed")

lbl = tk.Label(frame,text='Progrss Value')
#creating progress bar
pbar = ttk.Progressbar(frame, orient= "horizontal",\
     length=400,mode = "determinate")
    
#setting max value
pbar["maximum"] = 1000
btn = tk.Button(frame, text="START", command=progress)

#adding controls on frame
lbl.pack()
pbar.pack()
btn.pack()

frame.mainloop()