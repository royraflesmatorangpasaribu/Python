import tkinter
from tkinter import messagebox

def tombolOK():
    messagebox.showinfo('Response','The OK button was successfully clicked bhubu')
    
def tombolCancel():
    messagebox.showinfo('Response','Cancel button successfully clicked')

def main():
    root = tkinter.Tk()
    notifikasi = tkinter.Label(root, text = "Welcome, Please click the button!!")
    button1 = tkinter.Button(root, text = "OK", command = tombolOK)
    button2 = tkinter.Button(root, text = "Cancel",  fg="red", command = tombolCancel)
    notifikasi.pack()
    button1.pack()
    button2.pack()

    root.mainloop()

main()
