import tkinter as tk
def main(window,textBox):
    button=tk.Button(window,text="clear")
    button.config(command=lambda: textBox.delete(1.0,'end'))
    button.grid(row=1,column=0,sticky="n")
def privilage():
    return ["window","textBox"]
