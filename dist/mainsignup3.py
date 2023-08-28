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

signup_window = Tk()
signup_window.title("Sign Up page")
signup_window.geometry('925x500+300+200')
signup_window.configure(bg="#fff")
signup_window.resizable(False,False)

####################Functionality Part-----------------------------------------------
def clear():
    emailEntry.delete(0,END)
    user.delete(0,END)
    code.delete(0,END)
    confirmlabel.delete(0,END)
    check.set(0)


def connect_database():
    if emailEntry.get()=='' or user.get()=='' or code.get()=='' or confirmlabel.get()=='':
        messagebox.showerror("Error",'All Fields are Required')
    elif code.get() != confirmlabel.get():
        messagebox.showerror("Error",'Password Mismatched Try again')
    elif check.get()==0:
        messagebox.showerror("Error",'Please accept terms and conditions')
    else:
        con = sqlite3.connect(resource_path('data.db'))
        mycursor = con.cursor()
        table_create_query = '''CREATE TABLE IF NOT EXISTS  User_data (email TEXT,
            username TEXT, password TEXT)
            '''
        mycursor.execute(table_create_query)
        #Insert data
        data_insert_query = '''INSERT INTO User_data (email, username, password) VALUES
            (?, ?, ?)'''
        data_insert_tuple = (emailEntry.get(), user.get(), code.get())
        mycursor.execute(data_insert_query, data_insert_tuple)
        con.commit()
        con.close()
        messagebox.showinfo('Success','Sign up is successful')
        messagebox.showinfo('Information','Launch App Again if To Sign in If Sign in window does not opens!')
        clear()
        signup_window.destroy()
        import mainsignin2
        #
        
        
        
    """else:
        try:
            #con = sqlite3.connect(host='localhost',user='root',password='root')
            con = sqlite3.connect('data.db')
            mycursor = con.cursor()
        except:
            messagebox.showerror("Error",'Connection not established, Please Try Again, Please Try Again')
            return
        try:
        """    """query = 'create database userdata'
            mycursor.execute(query)
            query = 'use userdata'
            mycursor.execute(query)""" """
            #id INT PRIMARY KEY NOT NULL
            table_create_query = '''CREATE TABLE IF NOT EXISTS  User_data (email TEXT,
            username TEXT, password TEXT)
            '''
            mycursor.execute(table_create_query)   
            
             #Insert data
            data_insert_query = '''INSERT INTO User_data (email, username, password) VALUES
            (?, ?, ?)'''
            data_insert_tuple = (emailEntry.get(), user.get(), code.get())
            mycursor.execute(data_insert_query, data_insert_tuple)
            con.commit()
            con.close()
            messagebox.showinfo('Success','Sign up is successful')
        except:
            messagebox.showerror('Error','Database not connected')
            #mycursor.execute('use userdata')
            
        #query = 'select * from data where username=%s'
        #mycursor.execute(query,(user.get()))  
        
        #row = mycursor.fetchone() 
        #if row != None:
            #messagebox.showerror('Error','Username already exists')
        else:
            #query = 'insert into data(email,username,password) value(%s,%s,%s)'
            #mycursor.execute(query,(emailEntry.get(),user.get(),code.get()))
           
            
            clear()
            signup_window.destroy()
            import signin2"""
            
        
            
            
        
        
        

def login_page():
    signup_window.destroy()
    import mainsignin2
    
def hide1():
    openeye1.config(file =resource_path('openeye.png'))
    code.config(show="")
    eyeButton1.config(command=show)
    
def hide2():
    openeye2.config(file = resource_path('openeye.png'))
    confirmlabel.config(show="")
    eyeButton2.config(command=show2)

#----------------------------------------------
def show():
    openeye1.config(file = resource_path('closeeye.png'))
    code.config(show='*')
    eyeButton1.config(command=hide1)
    
def show2():
    openeye2.config(file = resource_path('closeeye.png'))
    confirmlabel.config(show='*')
    eyeButton2.config(command=hide2)
    
"""def tologin():
    signup_window.destroy()
    import signin2
"""


####################################################-------------------------------------------

img = ImageTk.PhotoImage(file = resource_path('logo.png'))
Label(signup_window,image=img,bg = 'white').place(x=50,y=90)

signup_frame =Frame(signup_window,width=350,height=390,bg="white")
signup_frame.place(x=480,y=50)

heading = Label(signup_frame,text='CREATE NEW ACCOUNT',fg="#57a1f8",bg='white',
                font=('Microsoft YaHei UI Light',19,'bold'))
#heading.place(x=35,y=5)
heading.grid(row=0,column=0,padx=10,pady=10)

###################################################------------------------------------------
emailLabel = Label(signup_frame,text='Email',font=('Microsoft YaHei UI Light',10,'bold'),bg='white',
                   fg='RoyalBlue1')
emailLabel.grid(row=1,column=0,sticky='W',padx=25,pady=(10,0))

emailEntry = Entry(signup_frame,width=30,border=0,font=('Microsoft YaHei UI Light',10,'bold'),fg='RoyalBlue1')
emailEntry.grid(row=2,column=0,sticky='W',padx=25)

Frame(signup_frame,width=295,height=2,bg='RoyalBlue1').grid(row=3,column=0,sticky='W',padx=25)

###################################################-------------------------------------------------

user = Label(signup_frame,text='Username',font=('Microsoft YaHei UI Light',10,'bold'),bg='white',
                   fg='RoyalBlue1')
user.grid(row=4,column=0,sticky='W',padx=25,pady=(10,0))

user = Entry(signup_frame,width=30,border=0,font=('Microsoft YaHei UI Light',10,'bold'),fg='RoyalBlue1')
user.grid(row=5,column=0,sticky='W',padx=25)

Frame(signup_frame,width=295,height=2,bg='RoyalBlue1').grid(row=6,column=0,sticky='W',padx=25)

#####################################################-------------------------------------------------------

code = Label(signup_frame,text='Password',font=('Microsoft YaHei UI Light',10,'bold'),bg='white',
                   fg='RoyalBlue1')
code.grid(row=7,column=0,sticky='W',padx=25,pady=(10,0))

code = Entry(signup_frame,width=30,border=0,font=('Microsoft YaHei UI Light',10,'bold'),fg='RoyalBlue1',show='*')
code.grid(row=8,column=0,sticky='W',padx=25)

Frame(signup_frame,width=295,height=2,bg='RoyalBlue1').grid(row=9,column=0,sticky='W',padx=25)


#-----
openeye1 = PhotoImage(file = resource_path('closeeye.png'))
eyeButton1 = Button(signup_frame,image=openeye1,bd=0,bg='white',activebackground='white',
                   cursor='hand2',command=show)
eyeButton1.place(x=290,y=200)
#------




#####################################################-------------------------------------------------------

confirmlabel = Label(signup_frame,text='Confirm Password',font=('Microsoft YaHei UI Light',10,'bold'),bg='white',
                   fg='RoyalBlue1')
confirmlabel.grid(row=10,column=0,sticky='W',padx=25,pady=(10,0))

confirmlabel = Entry(signup_frame,width=30,border=0,font=('Microsoft YaHei UI Light',10,'bold'),fg='RoyalBlue1',show='*')
confirmlabel.grid(row=11,column=0,sticky='W',padx=25)

Frame(signup_frame,width=295,height=2,bg='RoyalBlue1').grid(row=12,column=0,sticky='W',padx=25)



#2
openeye2 = PhotoImage(file = resource_path('closeeye.png'))
eyeButton2 = Button(signup_frame,image=openeye2,bd=0,bg='white',activebackground='white',
                   cursor='hand2',command=show2)
eyeButton2.place(x=290,y=260)
#2
#####################################################-------------------------------------------------------

#CheckButton
check = IntVar()
terms = Checkbutton(signup_frame,text='I agree to the Terms & Conditions'
                    ,font=('Microsoft YaHei UI Light',9,'bold'),bg='white',fg='RoyalBlue1'
                    ,activebackground='white',activeforeground='RoyalBlue1',cursor='hand2',
                    variable=check)
terms.grid(row=13,column=0,sticky='W',padx=15,pady=(10,0))


#----------------------------------------------------------------------------------------------
signup = Button(signup_frame,width=40,pady=7,text='Sign up',bg='#57a1f8',border=0,cursor='hand2',
                fg='white',font=('Microsoft YaHei UI Light',9,'bold'),command=connect_database)
signup.grid(row=14,column=0,sticky='W',padx=15,pady=(10,0))
#-----------------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------------
alreadylabel = Label(signup_frame,text="Already have an account?",fg='RoyalBlue1',bg='white',font=('Microsoft YaHei UI Light',9,'bold'))
alreadylabel.grid(row=15,column=0,sticky='W',padx=15,pady=(10,0))
#---------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------
signin = Button(signup_frame,width=6,text='Sign in',border=0,bg='white',cursor='hand2',
                fg='#57a1f8',font=('Microsoft YaHei UI Light',9,'bold underline'),activebackground='white',
                activeforeground='RoyalBlue1',command=login_page)
signin.place(x=190,y=385)
#-----------------------------------------------------------------------------------------------

signup_window.mainloop()

