from cryptography.fernet import Fernet
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog

global filepath
global Key
global keypath

def Generate():
    keypath = filedialog.askopenfilename()
    key = Fernet.generate_key()
    try:
        with open(keypath, "wb") as filekey:
            filekey.write(key)
    except FileNotFoundError:
        messagebox.showerror("Error", "no file was selected, try again")
        return
    messagebox.showinfo("", "Key generated successfully!")

def Encrypt():
    messagebox.showinfo("", "select a key")
    keypath = filedialog.askopenfilename()
    try:
        with open(keypath, "rb") as filekey:
            key = filekey.read()
    except FileNotFoundError:
        messagebox.showerror("Error", "no file was selected, try again")
        return
    try:
        global fernet
        fernet = Fernet(key)
    except ValueError:
        messagebox.showerror("Error", "This is not a key file, try again")
        return
    messagebox.showinfo("", "select one or more files to encrypt")
    filepath = filedialog.askopenfilenames()
    for x in filepath:
        with open(x, "rb") as file:
            original = file.read()
        global encrypted
        encrypted = fernet.encrypt(original)
        with open(x, "wb") as encrypted_file:
            encrypted_file.write(encrypted)
    if not filepath:
        messagebox.showerror("Error", "no file was selected, try again")
    else:
        messagebox.showinfo("", "files encrypted successfully!")

def Decrypt():
    messagebox.showinfo("", "select a key")
    keypath = filedialog.askopenfilename()
    try:
        with open(keypath, "rb") as filekey:
            key = filekey.read()
    except FileNotFoundError:
        messagebox.showerror("Error", "no file was selected, try again")
        return
    try:
        global fernet
        fernet = Fernet(key)
    except ValueError:
        messagebox.showerror("Error", "This is not a key file, try again")
        return
    messagebox.showinfo("", "select one or more files to decrypt")
    filepath = filedialog.askopenfilenames()
    for x in filepath:
        with open(x, "rb") as enc_file:
            encrypted = enc_file.read()
        decrypted = fernet.decrypt(encrypted)
        with open(x, "wb") as dec_file:
            dec_file.write(decrypted)
    if not filepath:
        messagebox.showerror("Error", "no file was selected, try again")
    else:
        messagebox.showinfo("", "files decrypted successfully!")

top = Tk()
top.geometry("400x300")
B = Button(top, text="Generate Key", command=Generate)
B.place(x=50, y=50)
ebutton = Button(top, text="encrypt", command=Encrypt)
ebutton.place(x=50, y=150)
ebutton = Button(top, text="decrypt", command=Decrypt)
ebutton.place(x=200, y=150)
top.mainloop()
