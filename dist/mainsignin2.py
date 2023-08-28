from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import sqlite3
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




root = Tk()
root.title("Login page")
root.geometry('925x500+300+200')
root.configure(bg="#fff")
root.resizable(False,False)


#Functionality Part#######################################################-------------------

def loginuser():
    if user.get()=='' or code.get()=='':
        messagebox.showerror('Error','All Fields are Required')
    
    else:
        try:
            #con = pymysql.connect(host='localhost',user='root',password='root')
            con = sqlite3.connect(resource_path('data.db'))
            mycursor = con.cursor()
            
        except:
            messagebox.showerror("Error",'Connection not established, Please Try Again')
            return
        #query = 'use userdata'
        #mycursor.execute(query)
        select_data_query = '''SELECT * FROM User_data WHERE username=? and password=?'''
        mycursor.execute(select_data_query,(user.get(),code.get()))
        row = mycursor.fetchone()
        if row == None:
            messagebox.showerror('Error','Invalid username or password')
        else:
            
            messagebox.showinfo('Welcome','Login Successfull')
            root.destroy()
            import mainafterlogin4
        con.close()
    



def hide():
    openeye.config(file=resource_path('openeye.png'))
    code.config(show="")
    eyeButton.config(command=show)

#----------------------------------------------
def show():
    openeye.config(file=resource_path('closeeye.png'))
    code.config(show='*')
    eyeButton.config(command=hide)
    
def tosignup():
    root.destroy()
    import mainsignup3
    
def forget_pass():
    def change_password():
        if user_entry.get()=='' or newpass_entry=='' or confirmpass_entry.get()=='':
            messagebox.showerror('Error','All Fields Are Required',parent=newWindow)
        elif newpass_entry.get()!=confirmpass_entry.get():
            messagebox.showerror('Error','Password Mismatched,Try Again',parent=newWindow)
        else:
            #con = pymysql.connect(host='localhost',user='root',password='root',database='userdata')
            con = sqlite3.connect('data.db')
            mycursor = con.cursor()
            
            select_user_query = '''SELECT * FROM User_data WHERE username=?'''
            mycursor.execute(select_user_query,(user_entry.get(),))
            row = mycursor.fetchone()
            if row == None:
                messagebox.showerror('Error','Username not registered!',parent=newWindow)
            else:
                update_query = '''UPDATE User_data SET password=? where username=?'''
                mycursor.execute(update_query,(newpass_entry.get(),user_entry.get()))
                con.commit()
                con.close()
                messagebox.showinfo('Success','Password Reset Successful, Click OK to Login!',parent=newWindow)
                newWindow.destroy()            
            
        
    newWindow = Toplevel()
    newWindow.title('Change Password')
    newWindow.geometry('925x500+300+200')
    newWindow.configure(bg="#fff")
    
    
    bgPic = ImageTk.PhotoImage(file = resource_path('logo.png'))
    bgLabel = Label(newWindow,image=bgPic,bd=0)
    bgLabel.place(x=50,y=50)
    
    heading_label = Label(newWindow,text='RESET PASSWORD',font=('arial','18','bold'),bg='white',fg='#57a1f8')
    heading_label.place(x=540,y=60)
    
    #----------------------user------------------------------------------------#
    userLabel = Label(newWindow,text='Username',font=('arial',12,'bold'),bg='white',fg='#57a1f8')
    userLabel.place(x=500,y=130)
    
    user_entry = Entry(newWindow,width=25,fg='#57a1f8',font=('arial',11,'bold'),bd=0)
    user_entry.place(x=500,y=160)
    
    Frame(newWindow, width=305, height=2,bg='#57a1f8').place(x=500,y=180)
    
    #----------------------------new password-------------------------------------------#
    passwordLabel = Label(newWindow,text='New Password',font=('arial',12,'bold'),bg='white',fg='#57a1f8')
    passwordLabel.place(x=500,y=210)
    
    newpass_entry = Entry(newWindow,width=25,fg='#57a1f8',font=('arial',11,'bold'),bd=0)
    newpass_entry.place(x=500,y=240)
    
    Frame(newWindow, width=305, height=2,bg='#57a1f8').place(x=500,y=260)
    
    #-----------------------------Confirm password--------------------------------#
    confirmpassLabel = Label(newWindow,text='Confirm Password',font=('arial',12,'bold'),bg='white',fg='#57a1f8')
    confirmpassLabel.place(x=500,y=290)
    
    confirmpass_entry = Entry(newWindow,width=25,fg='#57a1f8',font=('arial',11,'bold'),bd=0)
    confirmpass_entry.place(x=500,y=320)
    
    Frame(newWindow, width=305, height=2,bg='#57a1f8').place(x=500,y=340)
    
    #----------------------------------Submit Button------------------------------------#
    submitButton = Button(newWindow,text='Submit',bd=0,bg='#57a1f8',fg='white',font=('Open Sans','16','bold')
                          ,width=19,cursor='hand2',
                          activebackground='#57a1f8',
                          activeforeground='white',command=change_password)
    submitButton.place(x=530,y=390)
    
    
    
    
    
    newWindow.mainloop()
    #root.destroy()
    #import forgotcode
    
    
####################################################-------------------------------------------

img = ImageTk.PhotoImage(file = resource_path('logo.png'))
Label(root,image = img,bg = 'white').place(x=50,y=90)

frame =Frame(root,width=350,height=390,bg="white")
frame.place(x=480,y=70)

heading = Label(frame,text="Sign in",fg="#57a1f8",bg='white',font=('Microsoft YaHei UI Light',23,'bold'))
heading.place(x=120,y=5)

#############################################Username-----------------------------------------------------------------
def on_enter(e):
    user.delete(0,'end')

def on_leave(e):
    name = user.get()
    if name == '':
        user.insert(0,'Username')
    
user = Entry(frame,width=25,fg='RoyalBlue1',border=0,bg='white',font=('Microsoft YaHei UI Light',11))
user.place(x=30,y=80)
user.insert(0,'Username')
user.bind('<FocusIn>',  on_enter)
user.bind('<FocusOut>', on_leave)

Frame(frame,width=295,height=2,bg='RoyalBlue1').place(x=25,y=107)

###############################################Password----------------------------------------------------------------
def on_enter(e):
    code.delete(0,'end')

def on_leave(e):
    name = code.get()
    if name == '':
        code.insert(0,'Password')
        
code = Entry(frame,width=25,fg='RoyalBlue1',border=0,bg='white',
             font=('Microsoft YaHei UI Light',11),show='*')
code.place(x=30,y=150)
code.insert(0,'Password')
code.bind('<FocusIn>',  on_enter)
code.bind('<FocusOut>', on_leave)

Frame(frame,width=295,height=2,bg='RoyalBlue1').place(x=25,y=177)

#-----
openeye = PhotoImage(file = resource_path('closeeye.png'))
eyeButton = Button(frame,image=openeye,bd=0,bg='white',activebackground='white',
                   cursor='hand2',command=show)
eyeButton.place(x=290,y=145)
#------

#--------------------------
forgetButton = Button(frame,text='Forgot Password?',bd=0,bg='white',activebackground='white',
                   cursor='hand2',font=('Microsoft YaHei UI Light',9,'bold'),
                   fg='RoyalBlue1',activeforeground='RoyalBlue1',command=forget_pass)
forgetButton.place(x=200,y=190)
#---------------------------

#########################################################------------------------------------------------------

#####################################################################################################

#_____________________________________________________________
loginButton = Button(frame,width=40,pady=7,text='Sign in',bg='#57a1f8',fg='white',
                     border=0,cursor='hand2',command=loginuser)
loginButton.place(x=35,y=220)
#______________________________________________________________

#______________________________________________________________
orLabel = Label(frame,text='-------------------- OR --------------------',
                font=('Microsoft YaHei UI Light',9,'bold'),bg='white',fg='#57a1f8')
orLabel.place(x=40,y=290)
#_______________________________________________________________


"""#---------------------------------------------------------------
google_logo = PhotoImage(file='google.png')
google_label = Button(frame,image=google_logo,bg='white',bd=0)
google_label.place(x=70,y=290)

linkedin_logo = PhotoImage(file='linkedin.png')
linkedin_label = Button(frame,image=linkedin_logo,bg='white',bd=0)
linkedin_label.place(x=160,y=290)

github_logo = PhotoImage(file='github.png')
github_label = Button(frame,image=github_logo,bg='white',bd=0)
github_label.place(x=250,y=290)

#-------------------------------------------------------------------
"""





#--------------------------------------------------------------------------------------------
label = Label(frame,text="Don't have an account?",fg='RoyalBlue1',bg='white',font=('Microsoft YaHei UI Light',9,'bold'))
label.place(x=60,y=340)
#---------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------
signup = Button(frame,width=6,text='Sign up',border=0,bg='white',cursor='hand2',
                fg='#57a1f8',font=('Microsoft YaHei UI Light',9,'bold underline'),command=tosignup)
signup.place(x=220,y=340)
#-----------------------------------------------------------------------------------------------


root.mainloop()
