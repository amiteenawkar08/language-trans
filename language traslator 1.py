from tkinter import *
from tkk import*
root= Tk()
root.geometry="500x500"
root.configure(background= "Lavender")

label=Label(root,text="Language Traslator App ",bg="Light Blue",font=("Goudy Old Style",15,"bold"))
label.place(relx=0.5,rely=0.1, anchor=CENTER)

label=Label(root,text="Enter Text" ,bg="Light Blue",font=("Goudy Old Style",15,"bold"))
label.place(relx=0.5,rely=0.5,anchor=CENTER)

textarea=Textarea(root,bd=0,bg="Light Blue",font=("Goudy Old Style",15,"bold",12,12))
label.place(relx=0.9,rely=0.8,anchor=CENTER)

root.mainloop()





