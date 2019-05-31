import tkinter as tk
from app import EACESS
import time

session = EACESS()

def login_session(event):
    
    global session
    username = input_name.get()
    password = input_pass.get()

    try:
        session.login(username, password)      
        result.configure(text='Login Successful')
        return True
    except Exception as e:
        result.configure(text='An Error Occured')
        logfile = open('logfile.txt', 'a+')
        logfile.write(time.ctime() + ': ' + str(e) + '\n')
        logfile.close()
        return False

def logout_session(event):
    
    global session
    try:
        session.logout()
        result.configure(text='Logged Out')
        return True
    except:
        result.configure(text='An Error Occured')
        logfile = open('logfile.txt', 'a+')
        logfile.write(time.ctime() + ': ' + str(e) + '\n')
        logfile.close()
        return False
    
root = tk.Tk()
label = tk.Label(root,text='Enter Your Username:')
label.grid(row=0,column=0,sticky='E')
input_name = tk.Entry(root)
input_name.grid(row=1, column=0)
password = tk.Label(root, text='Enter Password:')
password.grid(row=0,column=1,sticky='E')
input_pass = tk.Entry(root)
input_pass.grid(row=1,column=1)
login = tk.Button(root,text='Login')
login.bind('<Button-1>',login_session)
login.place(x=110,y=100)
logout = tk.Button(root,text='Logout')
logout.bind('<Button-1>',logout_session)
logout.place(x=106,y=130)
result = tk.Label()
result.grid(columnspan=2)
mainMenu = tk.Menu(root)
subMenu = tk.Menu(mainMenu)
mainMenu.add_cascade(label='Settings', menu=subMenu)
subMenu.add_command(label='Quit', command=quit)
root.configure(menu=mainMenu)
root.resizable(0,0)
root.title('EACESS-CLIENT')
root.geometry('255x200')

root.mainloop() 


    

