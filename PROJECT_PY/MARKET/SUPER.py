from tkinter import *
import os
import sys
from tkinter import messagebox
import webbrowser
from PIL import Image, ImageTk
pro = Tk()
pro.title('SuperMarket')
pro.geometry('800x450+250+250')
title = Label(pro,text='Super Market',font=("Tajawal",16,'bold'),fg='gold',bg='black')
title.pack(fill=X)
pro.resizable(False,False)
# pro.config(bg="black")
pro.iconbitmap('hack.ico')
def openy():
    webbrowser.open_new('https://www.youtube.com/@KHAL_DRIC')
def openf():
    webbrowser.open_new('https://www.facebook.com/che.guevarra.508747')
def openi():
    webbrowser.open_new('https://www.instagram.com/twil_stories/?igshid=OGQ5ZDc2ODk2ZA%3D%3D')
def open1():
    messagebox.showinfo('المطور','خالد')
def open2():
    messagebox.showinfo('Projects','i have lot of projects if you wana see him you should go my githup')
def log():
    nom = e1.get()
    password = e2.get()
    if nom == 'khaldric' and password == '2007':
        messagebox.showinfo('Welcom',"مرحب بيك اسي خالد في برنامجك الخاص")
    else:
        messagebox.showerror('Erorr','معلومات خاطىء تاكد منها و حاول مرة اخرى')
f1 = Frame(pro,width=230,height=420,bg='#0B2F3A')
f1.place(x=590,y=30)
t1 = Label(f1,text='مرحبا بكم',bg='#0B2F3A',font=('Tajawal',22,'bold'),fg='gold')
t1.place(x=55,y=10)
t2 = Label(f1,text='في سوبر ماركت',bg='#0B2F3A',font=('Tajawal',18,'bold'),fg='gold')
t2.place(x=39,y=50)
t3 = Label(f1,text="مواقع تواصلنا",bg='#0B2F3A',font=('Tajawal',18,'bold'),fg='white')
t3.place(x=50,y=90)
b1 = Button(f1,text='موقعنا في فايسبوك',width=16,bg='#DBA901',font=('Tajawal',15,'bold'),fg='black',command=openf)
b1.place(x=6,y=130)
b2 = Button(f1,text='موقعنا في انستغرام',width=16,bg='#DBA901',font=('Tajawal',15,'bold'),fg='black',command=openi)
b2.place(x=6,y=177)

b3 = Button(f1,text='موقعنا في يوتيوب',width=16,bg='#DBA901',font=('Tajawal',15,'bold'),fg='black',command=openy)
b3.place(x=6,y=225)
b3 = Button(f1,text='مشاريع اخرى',width=16,bg='#DBA901',font=('Tajawal',15,'bold'),fg='black',command=open2)
b3.place(x=6,y=272)
b3 = Button(f1,text='لمحة عني',width=16,bg='#DBA901',font=('Tajawal',15,'bold'),fg='black',command=open1)
b3.place(x=6,y=318)
b4 = Button(f1,text='خروج',width=16,bg='#DBA901',font=('Tajawal',15,'bold'),fg='black',command=quit)
b4.place(x=6,y=365)
dev = Label(f1,text="المطور خالد",bg='#0B2F3A',font=('Tajawal',7,'bold'),fg='white')
dev.place(x=80,y=406)
logo = PhotoImage(file='logo.png')
home = Label(pro,image=logo)
home.place(x=-18,y=30,width=608,height=272)
f2 = Frame(pro,width=590,height=120,bg='#0B2F3A')
f2.place(x=0,y=330)
img = Image.open('user.png')
img = img.resize((100, 100))
usph = ImageTk.PhotoImage(img)
user = Label(pro, image=usph,bg='#0B2F3A')
user.place(x=490, y=335, width=100, height=100)
name = Label(f2,text=(': الاسم كامل'),bg='#0B2F3A',fg='gold',font=('Tajawal',16))
name.place(x=390,y=10)
pas = Label(f2,text=(': كلمة السر'),bg='#0B2F3A',fg='gold',font=('Tajawal',16))
pas.place(x=390,y=60)
e1 = Entry(f2,font=('Tajawal',14),fg='black')
e1.place(x=150,y=10)
e2 = Entry(f2,font=('Tajawal',14),fg='black')
e2.place(x=150,y=60)
bt = Button(f2,text='دخول',fg='white',bg='#DBA901',font=('Tajawal',20,'bold'),command=log)
bt.place(x=24,y=10,width=120,height=80)
pro.mainloop()