from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename,asksaveasfilename
import os
def new():
    global File
    root.title("Untitled-Notepad")
    File=None
    TextArea.delete(1.0,END)
def Open():
    global File
    File=askopenfilename(defaultextension=".txt",
                         filetype=[("All Files","*.*"),
                                   ("Text Document","*.txt")])
    if File == "":
        File=None
    else:
        root.title(os.path.basename(File)+ "-Notepad")
        TextArea.delete(1.0,END)
        f=open(File,"r")
        TextArea.insert(1.0,f.read())
        f.close()
def save():
    global File
    if File == None:
        File=asksaveasfilename(initialfile="Untitled.txt",defaultextension=".txt",
                               filetype=[("All File","*.*"),("Text Document","*.txt")])
        if File == "":
            File=None
        else:
            # save as a new file
            f=open(File,"w")
            f.write(TextArea.get(1.0,END))
            f.close()

            root.title(os.path.basename(File + "-Notepad"))
            print("file save")
    else:
        # save the file
        f=open(File,"w")
        f.write(TextArea.get(1.0,END))
        f.close()
def exitapp():
    root.destroy()
def cut():
    TextArea.event_generate(("<<Cut>>"))
def copy():
    TextArea.event_generate(("<<Copy>>"))
def paste():
    TextArea.event_generate(("<<Paste>>"))
def about():
    showinfo("Notepad","This Notepad is created by MkAgarwal")
if __name__ == '__main__':
    root=Tk()
    root.title("Untitled - Notepad")
    root.wm_iconbitmap("notepad.ico")
    root.geometry("645x567")

    # adding textarea
    TextArea=Text(root,font="lucida 15")
    TextArea.pack(fill=BOTH,expand=True)
    File=None

    # adding scrollbar in textarea
    scroll=Scrollbar(TextArea)
    scroll.pack(side=RIGHT,fill=Y)
    TextArea.config(yscrollcommand=scroll.set)
    scroll.config(command=TextArea.yview)

    # Adding Menubar

    Menubar=Menu(root)
    fileMenu=Menu(Menubar,tearoff=0)
    fileMenu.add_command(label='New',command=new)
    fileMenu.add_command(label='Open',command=Open)
    fileMenu.add_command(label='Save',command=save)
    fileMenu.add_separator()
    fileMenu.add_command(label='Exit',command=exitapp)
    Menubar.add_cascade(label='File',menu=fileMenu)

    # Adding editMenu

    EditMenu=Menu(Menubar,tearoff=0)
    EditMenu.add_command(label="Cut",command=cut)
    EditMenu.add_command(label="Copy",command=copy)
    EditMenu.add_command(label="Paste",command=paste)
    Menubar.add_cascade(label="Edit",menu=EditMenu)

    # adding about menu

    AboutMenu=Menu(Menubar,tearoff=0)
    AboutMenu.add_command(label='About Notepad',command=about)
    Menubar.add_cascade(label="About",menu=AboutMenu)
    root.config(menu=Menubar)


    root.mainloop()