from tkinter import *
import tkinter as tk
from tkinter import messagebox
import os

def raise_frame(frame):
    frame.tkraise()

def fileChecker():
    file1 = open('Screen.txt', 'r')
    file2 = open('Battery.txt', 'r')
    words1 = str(file1.read().split())
    words2 = str(file2.read().split())
    user = input ("type one word which is the main problem of your phone?")
    if any(word in words1 for word in words1):
        ans1 = input ("is the problem with the screen?")
        if ans1 == "yes":
            import Screen
        elif ans1 == "no":
            print ("plz try to explain again")
            fileChecker()
        else:
            print("error, plz try again")
            fileChecker()
    elif any(word in words1 for word in words1):
        print ("is the problem with the battery?")
        ans2 = input ("is the problem with the battery?")
        if ans2 == "yes":
            import Battery
        elif ans1 == "no":
            print ("plz try to explain again")
            fileChecker()
        else:
            print("error, plz try again")
            fileChecker()
    else:
        print ("did not understand, plz type again")
        fileChecker()

def radioBTN():
    if (check1, state == ACTIVE):
        print ("asd")


root = Tk()
root.title("Dawid's Program")
#root.geometry("1000x300")
root.iconbitmap('icon.ico')


MP = Frame(root)
a1 = Frame(root)
a2 = Frame(root)
b21 = Frame(root)
b22 = Frame(root)
b23 = Frame(root)
a3 = Frame(root)
a4 = Frame(root)

for frame in (MP, a1, a2, b21, b22, b23, a3, a4):
    frame.grid(row=0, column=0, sticky='news')
    MP.config(background='lime')

#MP
Label(MP, text='Main Menu',font="Arial", background='lime').pack()
Button(MP, text='Typical break', background='cyan', command=lambda:raise_frame(a1)).pack(ipadx='100')
Label(MP, text='If you dropped smashed or poured water on your phone please click here', background='lime').pack()
Button(MP, text='Quick Fix', background='cyan', command=lambda:raise_frame(a2)).pack(ipadx='100')
Label(MP, text='If your phone works but there are small problems with it click here', background='lime').pack(anchor='center')
Button(MP, text='Multiple Damages', background='cyan', command=lambda:raise_frame(a3)).pack(ipadx='100')
Label(MP, text='If your phode had more then one accident/reason why it has stoped working then click here', background='lime').pack(anchor='center')
Button(MP, text='Other', background='cyan', command=lambda:raise_frame(a4)).pack(ipadx='100')
Label(MP, text='Any other problems click here', background='lime').pack(anchor='center')
Button(MP, text="QUIT", background='lightblue', fg="red",command=quit).pack(side="bottom")
#MP

#a1
check1 = Radiobutton(a1, state = ACTIVE).pack(side="top")
check2 = Radiobutton(a1, state = ACTIVE).pack(side="top")
check3 = Radiobutton(a1, state = ACTIVE).pack(side="top")
Button(a1, text='Check Answer', command=lambda:radioBTN()).pack(ipadx='100')
Button(a1, text='Back', command=lambda:raise_frame(MP)).pack(ipadx='100')
#a1

#a2
Button(a2, text='dropped', command=lambda:raise_frame(b21)).pack(ipadx='100')
Button(a2, text='smashed', command=lambda:raise_frame(b22)).pack(ipadx='100')
Button(a2, text='water poured on phone', command=lambda:raise_frame(b23)).pack(ipadx='100')
Button(a2, text='Back', command=lambda:raise_frame(MP)).pack(ipadx='100')
#a2

#b21
Button(b21, text='light drop (less then 2 meters)', command=lambda:messagebox.showinfo("Store", "Go to a phone store to fix it")).pack(ipadx='100')
Button(b21, text='high drop (more then 2 meters)', command=lambda:messagebox.showinfo("Specialist", "Find someone privately to fix it for you")).pack(ipadx='100')
Button(b21, text='phone totaly destroyed', command=lambda:messagebox.showinfo("Shop", "Buy a new phone")).pack(ipadx='100')
Button(b21, text='Back', command=lambda:raise_frame(MP)).pack(ipadx='100')
#b21

#b22
Button(b22, text='small crack', command=lambda:messagebox.showinfo("Deal with it", "untill it works, dont bother fixing it")).pack(ipadx='100')
Button(b22, text='totaly smashed', command=lambda:messagebox.showinfo("Shop", "Ask if its better to repair or buy a new phone")).pack(ipadx='100')
Button(b22, text='screen fell out', command=lambda:messagebox.showinfo("Self-Repair", "Buy a new screen and replace it yourself")).pack(ipadx='100')
Button(b22, text='Back', command=lambda:raise_frame(MP)).pack(ipadx='100')
#b22

#b23
Button(b23, text='small amount of water', command=lambda:messagebox.showinfo("Rise", "Put it inside a boal of rise")).pack(ipadx='100')
Button(b23, text='big amount of water', command=lambda:messagebox.showinfo("Shop", "Go to a shop and see what they say")).pack(ipadx='100')
Button(b23, text='fell into the ocean', command=lambda:messagebox.showinfo("New Phone?", "You should buy a new phone")).pack(ipadx='100')
Button(b23, text='Back', command=lambda:raise_frame(MP)).pack(ipadx='100')
#b23

#a3
check1 = Checkbutton(a3, state = ACTIVE).pack(side="top")
check2 = Checkbutton(a3, state = ACTIVE).pack(side="top")
check3 = Checkbutton(a3, state = ACTIVE).pack(side="top")
Button(a3, text='asd', command=lambda:messagebox.showinfo("answer1", "answer1")).pack(ipadx='100')
Button(a3, text='Back', command=lambda:raise_frame(MP)).pack(ipadx='100')
#a3

#a4
Button(a4, text='problem', command=lambda:fileChecker()).pack(ipadx='100')
Button(a4, text='Back', command=lambda:raise_frame(MP)).pack(ipadx='100')
#a4

raise_frame(MP)
root.mainloop()
