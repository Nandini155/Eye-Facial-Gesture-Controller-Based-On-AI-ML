from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import os
import sys
import webbrowser




def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS2
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

videoroot =Tk()
videoroot.title("Instructions Window")
videoroot.geometry("925x500+300+200")
videoroot.configure(bg="#fff")
videoroot.resizable(False,False)

###################################################################################################
new = 1
url = "https://forms.gle/QUbJYzX8ocsVCPLN9"
def openfeedback():
    webbrowser.open(url,new=new)
    #os.system(resource_path("infovideo.mp4"))


def exit():
    videoroot.destroy()

    
###############################################################


img = ImageTk.PhotoImage(file = resource_path('logo.png'))
Label(videoroot,image=img,bg = 'white').place(x=50,y=90)


frame =Frame(videoroot,width=400,height=390,bg="white")
frame.place(x=480,y=70)

heading = Label(frame,text="VISION AI",fg="#57a1f8",bg='white',font=('Microsoft YaHei UI Light',30,'bold'))
heading.place(x=110,y=5)


sub_heading = Label(frame,text="THANK YOU FOR USING VISION AI !!",fg="#57a1f8",bg='white',font=('Microsoft YaHei UI Light',8,'bold'))
sub_heading.place(x=90,y=110)
###############################################################

playButton = Button(frame,width=25,text='Click For Feedback!',bg='#57a1f8',fg='white',cursor='hand2',font=('Open sans',9,'bold'),border=0,activebackground='RoyalBlue1',
                    activeforeground='white',command=openfeedback)
playButton.place(x=110,y=180)

###############################################################

skipButton = Button(frame,width=25,text='EXIT',bg='#57a1f8',fg='white',cursor='hand2',font=('Open sans',9,'bold'),border=0,activebackground='RoyalBlue1',activeforeground='white',command=exit)
skipButton.place(x=110,y=240)


videoroot.mainloop()