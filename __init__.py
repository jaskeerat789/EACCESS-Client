from tkinter import *
import tkinter.messagebox

def validate(event):
    id1=input_name.get()
    password=input_pass.get()
    id1=id1.lower()
    if id1=='mankaran32@gmail.com' and password=='Devilman32':
        result.configure(text='Login Successful')
    else:
        result.configure(text='Invalid E-Mail or Password')
        
    return None


root=Tk()
label=Label(root,text='Enter Your E-Mail:')
label.grid(row=0,column=0,sticky='E')
input_name=Entry(root)
input_name.grid(row=1, column=0)
password=Label(root, text='Enter Password:')
password.grid(row=0,column=1,sticky='E')
input_pass=Entry(root)
input_pass.grid(row=1,column=1)
login=Button(root,text='Login')
login.bind('<Button-1>',validate)
login.place(x=110,y=100)
remember=Checkbutton(root, text='Remember me')
remember.grid(columnspan=2)
result=Label()
result.grid(columnspan=2)

#tkinter.messagebox.showinfo(title='Python', message='Python ID verifier')

#Creatinf menus and sub menus

mainMenu=Menu(root)
subMenu=Menu(mainMenu)
mainMenu.add_cascade(label='File', menu=subMenu)
subMenu.add_command(label='Quit', command=quit)
#subMenu.add_separator()
subMenu.add_command(label='New File', command=quit)
#subMenu.add_separator()
subMenu.add_command(label='Save File', command=quit)
#subMenu.add_separator()
subMenu.add_command(label='Save As..', command=quit)
#subMenu.add_separator()
subMenu.add_command(label='Debug', command=quit)
root.configure(menu=mainMenu)
root.resizable(0,0)
root.title('Password Manager')


root.geometry('255x200')


    

