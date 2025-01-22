
from tkinter import *

window = Tk()

window.title("Задача")
window.geometry("500x500")
window.resizable(width=False,height=False)

frame = Frame(window,bg="lightgreen")
frame.place(relx=0.01, rely=0.01,relwidth=0.98,relheight=0.98)

label = Label(frame,text="100+100",font=100)
label.place(x=1,y=1, width=488,height=75)

def click_button1():
    label.config(text="Да,верно")

def click_button2():
    label.config(text="Нет не верно")

button1 = Button(frame, text="200", font=50, command=click_button1)
button1.place(x=230,y=200,height=50)

button2 = Button(frame,text="100", font=50, command=click_button2)
button2.place(x=230,y=300,height=50)

window.mainloop()