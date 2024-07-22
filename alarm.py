from tkinter import *
import time
import datetime
from playsound import playsound
import pyttsx3
import random
friend=pyttsx3.init()
friend.say("please Select what do you need")
friend.runAndWait()

def time12():
    global clock
    ts = time.strftime('%I:%M:%S:%p')
    clock['text'] = ts
    clock.after(1000, time12)


def alarm_begin(event):
    global e1, e2, e3
    h = e1.get()
    m = e2.get()
    s = e3.get()
    friend = pyttsx3.init()
    friend.say("you have set alarm for")
    friend.say(h)
    friend.say(m)
    friend.runAndWait()
    while (True):
        if (int(h) == datetime.datetime.now().hour and int(m) == datetime.datetime.now().minute and int (s) == datetime.datetime.now().second):
            playsound("alarm.mp3")
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
                    playsound("song.mp3")
                    print("Oops you have entered wrong please try again")
                    friend = pyttsx3.init()
                    friend.say("Oops you have entered wrong please try again")
                    friend.runAndWait()



def alarm():
    global e1, e2, e3
    window = Toplevel()
    window.geometry('400x300')
    hours = Label(window, text="Enter hour to ring alarm", font=('Helevitica', 20, 'bold'), fg='red', bg='white')
    hours.place(x=0, y=20)
    e1 = Entry(window, relief=GROOVE)
    e1.place(x=50, y=60)
    minutes = Label(window, text="Enter minute to ring alarm", font=('Helevitica', 20, 'bold'), fg='dark blue',
                    bg='white')
    minutes.place(x=0, y=90)
    e2 = Entry(window, relief=GROOVE)
    e2.place(x=50, y=120)
    seconds = Label(window, text="Enter second to ring alarm", font=('Helevitica', 20, 'bold'), fg='green', bg='white')
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
    window = Toplevel()
    window.geometry("350x200")
    clock = Label(window, font=('Franklin Gothic', 24, 'bold'), fg='green', bg='yellow')
    clock.place(x=20, y=30)
    if a == 'btn_12':
        time12()
    else:
        alarm()
    friend = pyttsx3.init()
    friend.say("thank you for selecting 12 hour clock")
    friend.runAndWait()


window = Tk()
window.title('Digital clock with Alarm')
window.geometry('500x400')
text = Label(window, text='Which clock do you want to try', font=('Helevitica', 24, 'bold'), fg='purple', bg='white')
text.place(x=20, y=20)

b1 = Button(window, text='12 hour clock', borderwidth=0, font=('Helevitica', 30, 'bold'), fg='green', bg='white',
            command=lambda: tick("btn_12")).place(anchor=SW, x=100, y=200)
b2 = Button(window, text='Alarm', borderwidth=0, font=('Helevitica', 30, 'bold'), fg='orange', bg='white',
            command=alarm).place(anchor=SW, x=180, y=300)
window.mainloop()



