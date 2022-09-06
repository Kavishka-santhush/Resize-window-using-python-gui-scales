from tkinter import *
import random
root=Tk()

mylabel=Label(root,text="You can rezise the screen using slider Now !").pack()

verticle=Scale(root,from_=0,to=400)
verticle.pack()

horizontal=Scale(root,from_=0,to=400,orient=HORIZONTAL)
horizontal.pack()

def rezise():
    root.geometry(str(horizontal.get())+"x"+str(verticle.get()))

mybutton=Button(root,text="Resize",command=rezise).pack()

root.mainloop()