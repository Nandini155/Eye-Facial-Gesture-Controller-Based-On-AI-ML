from tkinter import *
from tkinter import messagebox
import os
import sys




def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS2
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)



mainroot =Tk()
mainroot.title("Welcome to the Software")
mainroot.geometry("925x500+300+200")
mainroot.configure(bg="#fff")
mainroot.resizable(False,False)

def next():
    mainroot.destroy()
    import mainsignin2

######################################------------------------------------------------------------------

img = PhotoImage(file = resource_path('logo.png'))
Label(mainroot,image=img,bg = 'white').place(x=50,y=50)

frame =Frame(mainroot,width=350,height=350,bg="white")
frame.place(x=480,y=70)

heading = Label(frame,text="VISION AI",fg="#57a1f8",bg='white',font=('Microsoft YaHei UI Light',45,'bold'))
heading.place(relx=.5,rely=.3,anchor="center")

sub_heading = Label(frame,text="Welcome Users!",fg="#57a1f8",bg='white',font=('Microsoft YaHei UI Light',20,'bold'))
sub_heading.place(relx=.5,rely=.6,anchor="center")

img2 = PhotoImage(file= resource_path('nextbtn.png'))
next_btn = Button(frame,image=img2,border=0,bg='white',cursor='hand2',command=next)
next_btn.place(relx=.5,rely=.8,anchor="center")






#############################################----------------------------------------------------------



mainroot.mainloop()