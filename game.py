from tkinter import*
import random
import time
from random import randint
from tkinter import messagebox
def adjustWindow(window):
     w = 600 
     h = 600
     ws = screen.winfo_screenwidth() 
     hs = screen.winfo_screenheight() 
     x = (ws/2) - (w/2) 
     y = (hs/2) - (h/2)
     window.geometry('%dx%d+%d+%d' % (w, h, x, y)) 
     window.resizable(False, False) 
def random_circle():
    screen2=Tk()
    adjustWindow(screen2)
    w=Canvas(screen2,width=500,height=500,bg="#d9660a")
    w.pack()
    colors=["red","yellow","green","blue","violet"]
    #w.create_rectangle(20,20,380,380,fill="#174873")
    r=30
    for i in range(50):
        x=randint(0+r,500-r)
        y=randint(0+r,500-r)
        w.create_oval(x-r,y-r,x+r,y+r,fill=random.choice(colors)) 
    #screen2.mainloop()
    """now=time.time()
    future=now+10
    while time.time()<future:
        messagebox.showinfo("TIME", "CAN YOU COUNT?")"""
    for i in range(5):
        time.sleep(1)
    messagebox.showinfo("TIME", "stop")
 
def main_screen():
    global screen
    screen=Tk()
    adjustWindow(screen)
    w=Canvas(screen,width=500,height=500,bg="#d9660a")
    w.pack()
    #w.create_rectangle(70,20,450,400,fill="#174873")
    Label(text="Count the number of red balls within 10sec", width="100", height="2",font=("Calibri", 12, 'bold')).pack()
    Button(text="Start", bg="#e79700", width=15, height=1, font=("Open Sans",9, 'bold'), fg='white',command=random_circle).pack()
main_screen()
mainloop()