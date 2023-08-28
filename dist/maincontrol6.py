from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import cv2
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


startstoproot =Tk()
startstoproot.title("Instructions Window")
startstoproot.geometry("925x500+300+200")
startstoproot.configure(bg="#fff")
startstoproot.resizable(False,False)

#Functionality Part

def runcontrol():
    #video_window.destroy()
    messagebox.showinfo("Important Note",'To Exit This Controller Window Press "ESC" If "STOP" Does not works!!')
    import control
    import utils
    
   

def stop():
    # If the `Esc` key was pressed, break from the loop
    # Do a bit of cleanup
    cv2.destroyAllWindows()
    startstoproot.destroy()
    import mainlast7
    
   
    
def tovideoui5():
    startstoproot.destroy()
    import maininfo5
   
    
    


######################################------------------------------------------------------------------

img = ImageTk.PhotoImage(file = resource_path('logo.png'))
Label(startstoproot,image=img,bg = 'white').place(x=50,y=90)

frame =Frame(startstoproot,width=400,height=290,bg="white")
frame.place(x=480,y=70)

heading = Label(frame,text="VISION AI",fg="#57a1f8",bg='white',font=('Microsoft YaHei UI Light',30,'bold'))
heading.place(x=110,y=5)



sub_heading = Label(frame,text="Lets Get Started!!",fg="#57a1f8",bg='white',font=('Microsoft YaHei UI Light',20,'bold'))
sub_heading.place(x=90,y=100)



startButton = Button(frame,width=25,text='START',bg='#57a1f8',fg='white',cursor='hand2',font=('Open sans',9,'bold'),border=0,activebackground='RoyalBlue1',activeforeground='white',command=runcontrol)
startButton.place(x=110,y=170)



stopButton = Button(frame,width=25,text='STOP',bg='#57a1f8',fg='white',cursor='hand2',font=('Open sans',9,'bold'),border=0,
                    activebackground='RoyalBlue1',activeforeground='white',command=stop)
stopButton.place(x=110,y=200)


"""button3 = Button(text="FORCE QUIT", bg="RoyalBlue1",bd=0, command=quit,fg='white',activebackground='white',activeforeground='RoyalBlue1')
button3.bind('q',quit)
button3.pack(side=BOTTOM)"""





previousLabel = Button(frame,width=26,text='BACK TO INSTRUCTIONS',bg='white',fg='#57a1f8',cursor='hand2',font=('Open sans',9,'bold'),
                       border=0,activebackground='RoyalBlue1',activeforeground='white',command=tovideoui5)
previousLabel.place(x=110,y=230)


startstoproot.mainloop()