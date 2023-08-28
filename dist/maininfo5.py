from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
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


videoroot =Tk()
videoroot.title("Instructions Window")
videoroot.geometry("925x500+300+200")
videoroot.configure(bg="#fff")
videoroot.resizable(False,False)

###################################################################################################

def play():
    os.system(resource_path("infovideo.mp4"))


def skip():
    videoroot.destroy()
    import maincontrol6
    
###############################################################

sheading = Label(videoroot,text="INSTRUCTIONS",fg="#57a1f8",bg='white',font=('Microsoft YaHei UI Light','30','bold'))
sheading.place(x=80,y=20)

img = PhotoImage(file = resource_path('info.png'))
Label(videoroot,image=img,bg = 'white').place(x=50,y=90)


frame =Frame(videoroot,width=400,height=390,bg="white")
frame.place(x=480,y=70)

heading = Label(frame,text="VISION AI",fg="#57a1f8",bg='white',font=('Microsoft YaHei UI Light',30,'bold'))
heading.place(x=110,y=5)


"""sub_heading = Label(frame,text="PLAY VIDEO OR SKIP TO NEXT!!",fg="#57a1f8",bg='white',font=('Microsoft YaHei UI Light',10,'bold'))
sub_heading.place(x=90,y=110)
###############################################################

img2 = PhotoImage(file = resource_path('infoimage.jpg'))
Label(videoroot,image=img2,bg ='white').place(x=100,y=90)"""

"""playButton = Button(frame,width=25,text='Play Instructions Video',bg='#57a1f8',fg='white',cursor='hand2',font=('Open sans',9,'bold'),border=0,activebackground='RoyalBlue1',activeforeground='white',command=play)
playButton.place(x=110,y=180)"""

###############################################################

img2 = PhotoImage(file = resource_path('logosmall.png'))
Label(frame,image=img2,bg = 'white').place(x=130,y=90)


skipButton = Button(frame,width=25,text='Move to Next Window',bg='#57a1f8',fg='white',cursor='hand2',font=('Open sans','9','bold'),border=0,activebackground='RoyalBlue1',activeforeground='white',command=skip)
skipButton.place(x=120,y=290)


videoroot.mainloop()