import pydub
import pyttsx3
from tkinter import *
import speech_recognition as sr
from pydub.playback import play
from pydub import AudioSegment
import qrcode
import time
from tkinter import messagebox
# from playsound import playsound

def welcom():
     music = AudioSegment.from_mp3('sound/welcom.mp3')
     play(music)

welcom()

root = Tk()
root.title('Inscriptione')
root.geometry('370x470+460+250')
root.resizable(False,False)
root.iconbitmap('good.ico')
wel = pyttsx3.init()
voices = wel.getProperty('voices')
wel.setProperty('voice',voices[1].id)
def speak(audio):
    wel.say(audio)
    wel.runAndWait()
def takcomands():
    command = sr.Recognizer()
    with sr.Microphone() as mic:
        command.phrase_threshold=0.1
        audio = command.listen(mic)
        try:
            query = command.recognize_google(audio,language='ar')
        except Exception as Error:
            print(Error)
        return query.lower()
def b1():
    query = takcomands()
    name =query
    e1.insert(0,name)
def b2():
    query = takcomands()
    name =query
    e2.insert(0,name)
def b3():
    query = takcomands()
    name =query
    e3.insert(0,name)
def sv():
    name_file = e4.get()
    name = e1.get()
    con = e2.get()
    job = e3.get()
    info = qrcode.make(f"مرحبًا، أنا {name}  من {con}، أعمل كـ {job}.  سعيد بانضمامي لمجتع خالد لتطور !")
    info.save('member/'+ name_file+'.jpg')
    messagebox.showinfo('Save','Save '+ name_file + 'member')
    
photo = PhotoImage(file='logo.png')
l_photo = Label(root,image=photo)
l_photo.place(x=2,y=15)
title1 = Label(root,text='Information',font=('Tajawal',15,'bold'))
title1.place(x=130,y=200)
title2 = Label(root,text='Name :',font=('Tajawal',15))
title2.place(x=5,y=250)
title3 = Label(root,text='country :',font=('Tajawal',15))
title3.place(x=5,y=300)
title4 = Label(root,text='Profession :',font=('Tajawal',15))
title4.place(x=5,y=350)
e1 = Entry(root,font=('Italic',12),fg="#333333")
e1.place(x=80,y=250)

e2 = Entry(root,font=('Italic',12),fg="#333333")
e2.place(x=90,y=300)

e3 = Entry(root,font=('Italic',12),fg="#333333")
e3.place(x=120,y=350)

b1 = Button(root,text='🔊',bg="#2564B7",
fg="white",command=b1)
b1.place(x=270,y=250)

b2 = Button(root,text='🔊',bg="#2564B7",
fg="white",command=b2)
b2.place(x=290,y=300)

b3 = Button(root,text='🔊',bg="#2564B7",
fg="white",command=b3)
b3.place(x=310,y=350)

file_name = Label(root,text="File Name :",font=('Italic',15))
file_name.place(x=10,y=400)

e4 = Entry(root,font=('Tajawal',14),width=14)
e4.place(x=120,y=400)

b4 = Button(root,text="Save ✅",bg="#2ECC71",
fg="white",command=sv)
b4.place(x=290,y=400)

final = Label(root,text='Devlope by Khalid',fg="#9B59B6")
final.place(x=130,y=445)

root.mainloop()