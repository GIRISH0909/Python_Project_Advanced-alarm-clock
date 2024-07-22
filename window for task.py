from tkinter import *
from PIL import ImageTk,Image
import time
import datetime
from playsound import playsound
import pyttsx3
import random
from tkinter import messagebox
friend=pyttsx3.init()
friend.say("please Select what do you need")
friend.runAndWait()

def time24():
    global clock
    ts=time.strftime('%H:%M:%S')
    clock['text']=ts
    clock.after(1000,time24)
def time12():
    global clock
    ts = time.strftime('%I:%M:%S:%p')
    clock['text'] = ts
    clock.after(1000,time12)


def alarm_begin(event):
    global e1, e2, e3
    h = e1.get()
    m = e2.get()
    s = e3.get()
    friend = pyttsx3.init()
    friend.say("you have set alarm for")
    friend.say(h)
    friend.say('hour')
    friend.say(m)
    friend.say('minute')
    friend.say(s)
    friend.say('second')
    friend.runAndWait()
    friend = pyttsx3.init()
    friend.say("type 1 to set your message and type 2 show the task")
    friend.runAndWait()
    print('type "1" to set your message show that it will display after the time you have set')
    print('type "2" to run the task after the time you have set')
    q = int(input())
    if q==1:
        friend = pyttsx3.init()
        friend.say("type your message")
        friend.runAndWait()
        r = input('type your message here')
        friend = pyttsx3.init()
        friend.say("you have typed")
        friend.say(r)
        friend.runAndWait()
    while (True):
        if (int(h) == datetime.datetime.now().hour and int(m) == datetime.datetime.now().minute and int (s) == datetime.datetime.now().second):
            playsound(r"C:\\Users\\user\\PycharmProjects\\pythonProject\\music.mp3")
            if q == 1:
                friend = pyttsx3.init()
                friend.say(r)
                friend.runAndWait()
                print(r)
                messagebox.showinfo("Time's up!",r)

            if q==2:
                friend = pyttsx3.init()
                friend.say("complete the following task to stop alarm")
                friend.runAndWait()
                while True:
                    a = random.randint(60, 90)
                    b = random.randint(20, 50)
                    c = random.randint(50, 80)
                    d = random.randint(40, 80)
                    e = random.randint(1, 10)
                    f = random.randint(10, 20)
                    x = (a + b)
                    print(a, '+', b, '=')
                    n=int(input())
                    y = (c - d)
                    print(c, '-', d, '=')
                    m = int(input())
                    z = (e * f)
                    print(e, '*', f, '=')
                    o=int(input())
                    if n==x and m==y and  o==z:
                        print("correct")
                        friend = pyttsx3.init()
                        friend.say("you have entered correctly, your task is complete")
                        friend.runAndWait()
                        break
                    else:
                        playsound("C:\\Users\\user\\PycharmProjects\\pythonProject\\song.mp3")
                        print("Oops you have entered wrong please try again")
                        friend = pyttsx3.init()
                        friend.say("Oops you have entered wrong please try again")
                        friend.runAndWait()

def alarm():
    global e1, e2, e3, e4
    window = Toplevel()
    window.geometry('400x300')
    window.configure(background='orange')
    hours = Label(window, text="Enter hour to ring alarm", font=('Helevitica', 20, 'bold'), fg='red', bg='yellow')
    hours.place(x=0, y=20)
    e1 = Entry(window, relief=GROOVE)
    e1.place(x=50, y=60)
    minutes = Label(window, text="Enter minute to ring alarm", font=('Helevitica', 20, 'bold'), fg='dark blue',
                    bg='yellow')
    minutes.place(x=0, y=90)
    e2 = Entry(window, relief=GROOVE)
    e2.place(x=50, y=125)
    seconds = Label(window, text="Enter second to ring alarm", font=('Helevitica', 20, 'bold'), fg='green', bg='yellow')
    seconds.place(x=0, y=160)
    e3 = Entry(window, relief=GROOVE)
    e3.place(x=50, y=200)
    begin = Button(window, text='Start', font=('Helevitica', 20, 'bold'), fg='brown', bg='white', relief=GROOVE)
    begin.place(x=80, y=230)
    begin.bind("<Button-1>", alarm_begin)
    friend = pyttsx3.init()
    friend.say("thank you for selecting alarm, now you can set your alarm here")
    friend.runAndWait()

def tick(a):
    global clock
    window = Tk()
    window.title('24 HOUR CLOCK')
    window.geometry("350x300")
    window.configure(background='violet')
    clock = Label(window, font=('Franklin Gothic', 30, 'bold'), fg='green', bg='yellow')
    clock.place(x=60, y=100)
    if a=='btn_24':
        time24()
        friend = pyttsx3.init()
        friend.say("thank you for selecting 24 hour clock")
        friend.runAndWait()
    elif a == 'btn_12':
        time12()
        friend = pyttsx3.init()
        friend.say("thank you for selecting 12 hour clock")
        friend.runAndWait()

    else:
        alarm()

window = Tk()
window.title('Digital clock with Alarm')
photo=ImageTk.PhotoImage(Image.open('bg2a.jpg'))
l=Label(window,image=photo)
l.pack()
window.geometry('800x400')
text = Label(window, text='Which clock do you want to try ?', font=('Helevitica', 30, 'bold'), fg='purple', bg='yellow')
text.place(x=90, y=300)
b1 = Button(window, text='24 hour \n clock', borderwidth=10, font=('Helevitica', 25, 'bold'), fg='red', bg='cyan',
            command=lambda: tick("btn_24")).place(anchor=SW, x=70, y=240)
b2 = Button(window, text='12 hour \n clock', borderwidth=10, font=('Helevitica', 25, 'bold'), fg='red', bg='cyan',
            command=lambda: tick("btn_12")).place(anchor=SW, x=300, y=242)
b3 = Button(window, text='Alarm', borderwidth=10, font=('Helevitica', 25, 'bold'), fg='red', bg='cyan',
            command=alarm).place(anchor=SW, x=520, y=225)
window.mainloop()
