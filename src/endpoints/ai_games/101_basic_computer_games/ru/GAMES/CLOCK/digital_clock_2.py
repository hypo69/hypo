# pip install tkinter
from tkinter import * 
from time import strftime

myWindow = Tk()
myWindow.title('Мои часы')
def time():
    myTime = strftime('%H:%M:%S %p')
    clock.config(text = myTime)
    clock.after(1, time)

clock = Label(myWindow, font = ('arial', 40, 'bold'),
                                background = 'dark green',
                                foreground = 'white')

clock.pack(anchor = 'center')
time()

mainloop()