textbox=None
entry=None
def fib_func():
    print("yes")
    text=entry.get()
    if "-fib " in text:
        text=text.replace("-fib ","")
        try:
            number=int(text)
            a,b = 0,1
            for i in range(number):
                a,b = b,a+b
                textbox.insert('end',"%s "%a)
        except:
            textbox.insert('end',"invalid fib input",'red')


#without main and privilage function a plugin will be invalid
def main(textBox_widget, entry_widget):
    global textbox,entry
    textbox=textBox_widget
    entry=entry_widget
    entry.bind("<F1>",lambda x: fib_func())

#privilage list elements sequence== function arguments sequence
def privilage():
    return("textBox",'entry')