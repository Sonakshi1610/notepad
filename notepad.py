from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os

def newFile():
    global file
    root.title("untitiled - Notepad")
    file=None
    TextArea.delete(1.0, END)

def openFile():
    global file
    file = askopenfilename(defaultextension=".txt",
                           filetypes=[("All Files", "*.*"),
                                      ("Text Documents",
                                      "*.txt")])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file)+" - Notepad")
        TextArea.delete(1.0,END)
        f = open(file, "r")
        TextArea.insert(1.0,f.read())
        f.close()


def saveFile():
    global file
    if file == None:
        file = asksaveasfilename(initialfile= "untitled.txt", defaultextension=".txt",
                           filetypes=[("All Files", "*.*"),
                                      ("Text Documents",
                                      "*.txt")])
        if file=="":
            file = None

        else:
            #Save as a new file
            f = open(file, "w")
            f.write(TextArea.get(1.0, END))
            f.close()

            root.title(os.path.basename(file) + " - Notepad")
    else:
        # Save the file
        f = open(file, "w")
        f.write(TextArea.get(1.0, END))
        f.close()

def quitApp():
    root.destroy()

def cut():
    TextArea.event_generate(("<<Cut>>"))

def copy():
    TextArea.event_generate(("<<Copy>>"))

def paste():
    TextArea.event_generate(("<<Paste>>"))

def about():
    showinfo("Notepad", "Notepad is a text editor, i.e., an app specialized in editing plain text.\
It can edit text files (bearing the '.txt' filename extension) and compatible formats, such as batch files, INI files, \
and log files. It is designed by Sonakshi Gupta")

if __name__ == "__main__":
    root = Tk()
    root.title("untitiled - Notepad")
    root.geometry("600x650")

    #Add textarea
    TextArea = Text(root, font="lucida 13 ")
    file = None
    TextArea.pack(expand=True, fill=BOTH )

    #Lets create a menubar
    MenuBar = Menu(root)
# FILE MENU STARTS
    FileMenu = Menu(MenuBar, tearoff=0)
    # to open new file
    FileMenu.add_command(label="new", command=newFile)

    #to Open already existing file
    FileMenu.add_command(label="Open", command=openFile)

    # to save current file

    FileMenu.add_command(label="Save", command=saveFile)
    FileMenu.add_separator()
    FileMenu.add_command(label="Exit", command=quitApp)
    MenuBar.add_cascade(label = "File", menu=FileMenu)
# FILE MENU ENDS

#EDIT MENU STARTS
    EditMenu = Menu(MenuBar, tearoff=0)
    # to give a feature of cut, copy and paste
    EditMenu.add_command(label="Cut", command=cut)
    EditMenu.add_command(label="copy", command=copy)
    EditMenu.add_command(label="paste", command=paste)

    MenuBar.add_cascade(label="Edit", menu=EditMenu)

# EDIT MENU ENDS

# HELP MENU STARTS
    HelpMenu = Menu(MenuBar, tearoff=0)
    HelpMenu.add_command(label = "About Us", command=about)
    MenuBar.add_cascade(label="Help", menu=HelpMenu)



# HELP MENU ENDS


    root.config(menu=MenuBar)

#Adding scrollbar
    Scroll = Scrollbar(TextArea)
    Scroll.pack(side=RIGHT, fill=Y)
    Scroll.config(command=TextArea.yview)
    TextArea.config(yscrollcommand=Scroll.set)

    root.mainloop()
