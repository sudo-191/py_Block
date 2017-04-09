textbox=None
entry=None
def reverse():
    text=entry.get()
    if "-rev " in text:
        text=text.replace("-rev ","")
        l=len(text)
        output=""
        for i in range(l-1,-1,-1):
            output+=text[i]
        textbox.insert('end',"\n"+output)

#without main and privilage function a plugin will be invalid
def main(textBox_widget, entry_widget):
    global textbox,entry
    textbox=textBox_widget
    entry=entry_widget
    entry.bind("<Return>",lambda x: reverse())

#privilage list elements sequence== function arguments sequence
def privilage():
    return("textBox",'entry')