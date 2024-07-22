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
    global e1, e2, e3 , e4 , e5
    h = e1.get()
    m = e2.get()
    s = e3.get()
    q = e4.get()
    r = e5.get()
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
    def message(event):
        global e4,e5
        q = e4.get()
        r = e5.get()
        if q==1:
            friend = pyttsx3.init()
            friend.say("type your message")
            friend.runAndWait()
            friend = pyttsx3.init()
            friend.say("you have typed")
            friend.say(r)
            friend.runAndWait()
    while (True):
        if (int(h) == datetime.datetime.now().hour and int(m) == datetime.datetime.now().minute and int (s) == datetime.datetime.now().second):
            playsound("music.mp3")
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
                        playsound("song.mp3")
                        print("Oops you have entered wrong please try again")
                        friend = pyttsx3.init()
                        friend.say("Oops you have entered wrong please try again")
                        friend.runAndWait()
            print(r)
            friend = pyttsx3.init()
            friend.say("r")
            friend.runAndWait()


def alarm(message=None):
    global e1, e2, e3, e4 ,e5
    window = Toplevel()
    window.geometry('700x600')
    window.configure(background='cyan')
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
    text1 = Label(window, text="type 1 to set your message show that it will display after the time you have set", font=('Helevitica', 20, 'bold'), fg='red', bg='yellow')
    text1.place(x=0, y=270)
    text2 = Label(window, text="type 2 to run the task after the time you have set", font=('Helevitica', 20, 'bold'), fg='red', bg='yellow')
    text2.place(x=0, y=350)
    text3 = Label(window, text="type your message here",font=('Helevitica', 20, 'bold'), fg='red', bg='yellow')
    text3.place(x=0, y=400)
    e4 = Entry(window, relief=GROOVE)
    e4.place(x=50, y=450)
    e5=Entry(window,relief=GROOVE)
    e5.place(x=50,y=490)
    begin = Button(window, text='Start', font=('Helevitica', 20, 'bold'), fg='brown', bg='white', relief=GROOVE)
    begin.place(x=80, y=230)
    begin.bind("<Button-1>", alarm_begin)
    begin = Button(window, text='Start', font=('Helevitica', 20, 'bold'), fg='brown', bg='white', relief=GROOVE)
    begin.place(x=80, y=370)
    begin.bind("<Button-2>",message)
    friend = pyttsx3.init()
    friend.say("thank you for selecting alarm, now you can set your alarm here")
    friend.runAndWait()

def tick(a):
    global clock
    window = Toplevel()
    window.geometry("350x200")
    window.configure(background='pink')
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
window.configure(background='coral')
text = Label(window, text='Which clock do you want to try', font=('Helevitica', 24, 'bold'), fg='purple', bg='lime')
text.place(x=20, y=20)

b1 = Button(window, text='12 hour clock', borderwidth=0, font=('Helevitica', 30, 'bold'), fg='green', bg='cyan',
            command=lambda: tick("btn_12")).place(anchor=SW, x=100, y=200)
b2 = Button(window, text='Alarm', borderwidth=0, font=('Helevitica', 30, 'bold'), fg='orange', bg='cyan',
            command=alarm).place(anchor=SW, x=180, y=300)
window.mainloop()


    