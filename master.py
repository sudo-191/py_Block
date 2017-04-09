import tkinter as tk
import os
from tkinter import scrolledtext as stext
class gui():
    def __init__(self, master=None):
        self.plugins_path= os.getcwd()+"\\plugins\\" #path of plugins folder. it is in current working path.
        os.sys.path.append(self.plugins_path)
        
        #widgets
        self.master=master 
        self.master.title("Master")
        #self.master.resizable(0,0)
        self.mainframe=tk.LabelFrame(master, text="main Window") #main window frame

        self.textBox=stext.ScrolledText(self.mainframe) #textbox
        self.textBox.config(width=40,font="consolas 9")
        self.textBox.tag_config("red",foreground="darkred")
        self.textBox.tag_config("blue",foreground="blue")
        self.textBox.tag_config("green",foreground="green")
        self.textBox.tag_config("default",foreground="black")
        self.entry=tk.Entry(self.mainframe,width=35,font="consolas 11") #entry box
        self.entry.focus()
        #grid mainframe
        self.mainframe.grid(padx=2,pady=2)
        #packing widget in mainframe
        self.textBox.pack(padx=5,pady=5)
        self.entry.pack(padx=5,pady=5,side="left")
        #list of all widgets. for plugin privilage purpose
        self.widgets={"textBox":self.textBox,"entry":self.entry,"window":self.master}
        
        
        self.plugin_loader()
        
    #insert text in textbox
    def textBoxInsert(self,texts="",tag="default"):
        self.textBox.insert('end',texts,tag)
    
    #load plugin
    def plugin_loader(self):
        self.textBoxInsert(texts=">>plugin is loading\n",tag="blue") #notification about loading
        self.plugins=os.listdir(self.plugins_path) #list of all plugins
        for plugin in self.plugins:
            if(plugin[-3:]==".py" or plugin[-3:]==".pyd"):
                try:
                    plugin_load=__import__("%s"%plugin[:-3])
                    privilages=self.privilage(plugin_load.privilage()) #getting privilage list from loaded plugin
                    if privilages!=-1:
                        try:
                            plugin_load.main(*privilages) #argument passing to main function of loaded plugin
                            self.textBoxInsert(texts=">>%s is loaded\n"%plugin,tag="green") #if valid
                        except Exception as e:
                            self.textBoxInsert(texts=">>%s.main() something wrong\n"%plugin,tag="red") #else
                            self.textBoxInsert(texts=">>ERROR: %s\n"%e,tag="red")
                            
                    else:
                        self.textBoxInsert(texts=">>%s has invalid priviliage\n"%plugin,tag="red") #-1 one
                except Exception as e:
                    self.textBoxInsert(texts=">>%s is not a valid plugin\n"%plugin,tag="red") #error in plugin or no main or privilage function
                    self.textBoxInsert(texts=">>ERROR: %s\n"%e,tag="red")
    
    #return widgets reference from widgets dictionary
    def privilage(self,privilages):
        widgets=[] #widget reference list to pass in main function
        if 0<len(privilages)<3:
            for i in privilages:
                widgets.append(self.widgets[i]) #retrieving value from the widget dictionary, which contain widgets.
            return widgets
        else:
            return -1


root=tk.Tk()
window=gui(root)
root.mainloop()