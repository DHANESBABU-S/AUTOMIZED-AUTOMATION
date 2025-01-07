from candy import *
#---------------------------------------------------------------------------------------------------#
app=Tk()
app.configure(bg='red')
app.geometry('925x500+300+200')
app.resizable(0,0)
app.bgcolor='red'
app.iconbitmap("Y:\PROJECTS\AUTOMIZED AUTOMATION\WORK SPACE\Assts\Images\wcm.ico")
app.title("AUTOMAIZED AUTOMATION")
app.overrideredirect(True)
app.attributes('-alpha',0.9)
global bgimage
bgimage = ImageTk.PhotoImage(file="Y:/PROJECTS/AUTOMIZED AUTOMATION/WORK SPACE/Assts/Images/bg2.png")
bglabel = Label(app,image=bgimage)
bglabel.place(x=-2,y=-2)
def on_drag(event):
  global x, y
  x = app.winfo_pointerx() - app._offsetx
  y = app.winfo_pointery() - app._offsety
  app.geometry(f"+{x}+{y}")
def on_start_drag(event):
    global x, y
    x = event.x
    y = event.y
    app._offsetx = event.x
    app._offsety = event.y
app.bind("<ButtonPress-1>", on_start_drag)
app.bind("<B1-Motion>", on_drag)
def close(event):
  speak('Do you want close this application')
  if messagebox.askyesno('AUTOMATIZED AUTOMATION','Do you want close this login application?') == True:
    app.destroy()
    speak('application was sucessfully closed')
  else:
    pass
app.bind("<Double 1>", close)
#---------------------------------------------------------------------------------------------------#

#---------------------------------------------------------------------------------------------------#
def on_enter(event):
  if User_name_Entry.get()=='NAME':
    User_name_Entry.delete(0,END)

def on_leave(event):
  if User_name_Entry.get()=='':
    User_name_Entry.insert(0,'NAME')

def on_enter1(event):
  if User_password_Entry.get()=='PASSWORD':
    User_password_Entry.delete(0,END)
    User_password_Entry.config(show='*')

def on_leave1(event):
  if User_password_Entry.get()=='':
    User_password_Entry.config(show='')
    User_password_Entry.insert(0,'PASSWORD')

def hide():
    User_password_Entry.config(show='')
    User_password_Entry.after(500, lambda: User_password_Entry.config(show="*"))

def forgot():
  if messagebox.askyesno('AUTOMATIZED AUTOMATION','DO YOU WANT CHANGE YOUR OLD PASSWORD...'):
    if User_name_Entry.get()=='' or User_name_Entry.get()=='NAME':
      messagebox.showerror('AUTOMATIZED AUTOMATION','CAN YOU ENTER ACCOUNT USER NAME...')
    else:
      app.destroy()
      call(["Python","Y:\PROJECTS\AUTOMIZED AUTOMATION\WORK SPACE\Forgot\App_Forgot.py"])
  else:
    pass

def Login():
  username=User_name_Entry.get()
  password=User_password_Entry.get()

  file=open('Y:\PROJECTS\AUTOMIZED AUTOMATION\WORK SPACE\Assts\data_center\data.txt','r')
  d=file.read()
  r=ast.literal_eval(d)
  file.close()
  if username in r.keys() and password==r[username]:
    messagebox.showinfo('AUTOMATIZED AUTOMATION','LOGIN SUCESFULLY...')
    app.destroy()
    call(["Python","Y:\PROJECTS\AUTOMIZED AUTOMATION\WORK SPACE\App_UI\App_UI.py"])

  elif username=='NAME' and password=='PASSWORD':
    messagebox.showerror('AUTOMATIZED AUTOMATION','ENTER USER NAME AND PASSWORD...')

  elif username=='NAME' or username=='':
    messagebox.showerror('AUTOMATIZED AUTOMATION','ENTER VALID USER NAME...')
    
  elif password=='PASSWORD' or password=='':
    messagebox.showerror('AUTOMATIZED AUTOMATION','ENTER VALID USER PASSWORD...')

  elif username=='' and password=='PASSWORD':
    messagebox.showerror('AUTOMATIZED AUTOMATION','ENTER VALID USER NAME...')

  elif username=='USERNAME' and password=='' or password=='PASSWORD':
    messagebox.showerror('AUTOMATIZED AUTOMATION','ENTER VALID USER PASSWORD...')

  else:
    messagebox.showerror('AUTOMATIZED AUTOMATION','INCORRECT USER NAME AND PASSWORD...')
    User_name_Entry.delete(0,END)
    User_name_Entry.insert(0,'NAME')
    User_password_Entry.delete(0,END)
    User_password_Entry.insert(0,'PASSWORD')
    User_password_Entry.config(show='')


def register():
  if messagebox.askyesno("AUTOMAIZED AUTOMATION","Do you want to create new account?"):
    app.destroy()
    call(["Python","Y:\PROJECTS\AUTOMIZED AUTOMATION\WORK SPACE\Register\App_Register.py"])
  else:
    pass
##  import App_Register

#---------------------------------------------------------------------------------------------------#

#---------------------------------------------------------------------------------------------------#
heading = Label(app,text = 'LOGIN',font=('Times New Roman',25,'bold'),bg='#fc8400')
heading.place(x = 400,y = 60)
#---------------------------------------------------------------------------------------------------#

#---------------------------------------------------------------------------------------------------#
User_name_Entry = Entry(app,width = 25,font=('Times New Roman',23),bd = 0,bg='#fd6f00')
User_name_Entry.place(x = 260,y = 170)
User_name_Entry.insert(0,'NAME')
User_name_Entry.bind("<FocusIn>",on_enter)
User_name_Entry.bind("<FocusOut>",on_leave)
User_name_Line_Entry_Label = Frame(app,width=402,height=4,bg='black')
User_name_Line_Entry_Label.place(x=260,y=205)
#---------------------------------------------------------------------------------------------------#

#---------------------------------------------------------------------------------------------------#
User_password_Entry = Entry(app,width = 25,font=('Times New Roman',23),bd = 0,bg='#fd6f00')
User_password_Entry.place(x = 260,y = 270)
User_password_Entry.insert(0,'PASSWORD')
User_password_Entry.bind("<FocusIn>",on_enter1)
User_password_Entry.bind("<FocusOut>",on_leave1)
User_password_Line_Entry_Label = Frame(app,width=402,height=4,bg='black')
User_password_Line_Entry_Label.place(x=260,y=305)
#---------------------------------------------------------------------------------------------------#

#---------------------------------------------------------------------------------------------------#
closeye = PhotoImage(file="Y:\\PROJECTS\\AUTOMIZED AUTOMATION\\WORK SPACE\\Assts\\Images\\openeye.png")
eyebutton = Button(app,image=closeye,bd=0,bg='#fd6f00',cursor='hand2',command=hide,activebackground='#fd6f00',activeforeground='#fd6f00')
eyebutton.place(x=630,y=276)
#---------------------------------------------------------------------------------------------------#

#---------------------------------------------------------------------------------------------------#
forgotbutton = Button(app,text  = 'Forgot Password?',bd=0,font=('Times New Roman',13),bg='#fa0111',fg='black',activebackground='#fa0111',cursor='hand2',command=forgot)
forgotbutton.place(x=530,y=310)
#---------------------------------------------------------------------------------------------------#

#---------------------------------------------------------------------------------------------------#
loginbutton = Button(app,text  = 'SUBMIT',bd=0,width=25,height=0,font=('Times New Roman',15),bg='#fd6f00',activebackground='#fd6f00',cursor='hand2',command=Login)
loginbutton.place(x=320,y=350)
#---------------------------------------------------------------------------------------------------#

#---------------------------------------------------------------------------------------------------#
createAccount = Label(app,text = "Don't Have an Account ",font=('Times New Roman',13,'bold'),bg='#fe0400')
createAccount.place(x = 300,y = 410)
#---------------------------------------------------------------------------------------------------#

#---------------------------------------------------------------------------------------------------#
createbutton = Button(app,text  = 'Create New Account...',bd=0,font=('Times New Roman',12),bg='#f70225',activebackground='#f70225',cursor='hand2',command=register)
createbutton.place(x=470,y=410)
#---------------------------------------------------------------------------------------------------#
app.mainloop()
