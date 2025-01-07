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
global bgimage1
bgimage1 = ImageTk.PhotoImage(file="Y:/PROJECTS/AUTOMIZED AUTOMATION/WORK SPACE/Assts/Images/bg2.png")
bglabe2 = Label(app,image=bgimage1)
bglabe2.place(x=-2,y=-2)
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
heading = Label(app,text = 'REGISTER',font=('Times New Roman',25,'bold'),bg='#fc8400')
heading.place(x = 365,y = 70)
#---------------------------------------------------------------------------------------------------#
def register():
  if User_name_Entry.get()=='' or User_password_Entry.get()=='' or User_cpassword_Entry.get()=='' or User_name_Entry.get()=='NAME' or User_password_Entry.get()=='PASSWORD' or User_cpassword_Entry.get()=='CONFORM PASSWORD':
    messagebox.showerror('AUTOMATIZED AUTOMATION','ENTER INFORMATION FOR REGISTER...')

  else:
    username = User_name_Entry.get()
    password = User_password_Entry.get()
    cpassword = User_cpassword_Entry.get()

    if password == cpassword:
      try:
        file=open('Y:\PROJECTS\AUTOMIZED AUTOMATION\WORK SPACE\Assts\data_center\data.txt','r+')
        d=file.read()
        r=ast.literal_eval(d)

        dict2={username:password}
        r.update(dict2)
        file.truncate(0)
        file.close()

        file=open('Y:\PROJECTS\AUTOMIZED AUTOMATION\WORK SPACE\Assts\data_center\data.txt','w')
        w=file.write(str(r))
        messagebox.showinfo('AUTOMATIZED AUTOMATION','SUCESSFULLY REGISTERED')
        User_name_Entry.delete(0,END)
        User_name_Entry.insert(0,'NAME')
        User_password_Entry.delete(0,END)
        User_password_Entry.config(show='')
        User_password_Entry.insert(0,'PASSWORD')
        User_cpassword_Entry.delete(0,END)
        User_cpassword_Entry.config(show='')
        User_cpassword_Entry.insert(0,'CONFORM PASSWORD')
      except:
        file=open('Y:\PROJECTS\AUTOMIZED AUTOMATION\WORK SPACE\Assts\data_center\data.txt','w')
        pp=str({'username':'password'})
        file.write(pp)
        file.close()
    else:
      messagebox.showerror('AUTOMATIZED AUTOMATION','INCORRECT PASSWORD?')
  
def clear():
  if messagebox.askyesno("AUTOMAIZED AUTOMATION","DO YOU WANT TO CLEAR THE INFORMATION"):
    User_name_Entry.delete(0,END)
    User_name_Entry.insert(0,'NAME')
    User_password_Entry.delete(0,END)
    User_password_Entry.config(show='')
    User_password_Entry.insert(0,'PASSWORD')
    User_cpassword_Entry.delete(0,END)
    User_cpassword_Entry.config(show='')
    User_cpassword_Entry.insert(0,'CONFORM PASSWORD')
  else:
    pass

def login():
  if messagebox.askyesno("AUTOMAIZED AUTOMATION","DO YOU WANT TO LOGIN NOW?"):
    app.destroy()
    call(["Python","Y:\PROJECTS\AUTOMIZED AUTOMATION\WORK SPACE\Login\App_Login.py"])
  else:
    pass
##  import App_Login
#---------------------------------------------------------------------------------------------------#
def on_enter(event):
  if User_name_Entry.get()=='NAME':
    User_name_Entry.delete(0,END)

def on_leave(event):
  if User_name_Entry.get()=='':
    User_name_Entry.insert(0,'NAME')
    
User_name_Entry = Entry(app,width = 25,font=('Times New Roman',23),bd = 0,bg='#fd6f00')
User_name_Entry.place(x = 255,y = 170)
User_name_Entry.insert(0,'NAME')
User_name_Entry.bind("<FocusIn>",on_enter)
User_name_Entry.bind("<FocusOut>",on_leave)

User_name_Line_Entry_Label = Frame(app,width=402,height=4,bg='black')
User_name_Line_Entry_Label.place(x=255,y=205)
#---------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------#
def on_enter1(event):
  if User_password_Entry.get()=='PASSWORD':
      User_password_Entry.delete(0,END)
      User_password_Entry.config(show='*')
    

def on_leave1(event):
  if User_password_Entry.get()=='' or User_password_Entry.get()=='********':
    User_password_Entry.config(show='')
    User_password_Entry.insert(0,'PASSWORD')

User_password_Entry = Entry(app,width = 25,font=('Times New Roman',23),bd = 0,bg='#fd6f00')
User_password_Entry.place(x = 255,y = 240)
User_password_Entry.insert(0,'PASSWORD')
User_password_Entry.bind("<FocusIn>",on_enter1)
User_password_Entry.bind("<FocusOut>",on_leave1)

User_password_Line_Entry_Label = Frame(app,width=402,height=4,bg='black')
User_password_Line_Entry_Label.place(x=255,y=275)
#---------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------#
def on_enter2(event):
  if User_cpassword_Entry.get()=='CONFORM PASSWORD':
    User_cpassword_Entry.delete(0,END)
    User_cpassword_Entry.config(show='*')

def on_leave2(event):
  if User_cpassword_Entry.get()=='' or User_cpassword_Entry.get()=='****************':
    User_cpassword_Entry.config(show='')
    User_cpassword_Entry.insert(0,'CONFORM PASSWORD')

User_cpassword_Entry = Entry(app,width = 25,font=('Times New Roman',23),bd = 0,bg='#fd6f00')
User_cpassword_Entry.place(x = 255,y = 310)
User_cpassword_Entry.insert(0,'CONFORM PASSWORD')
User_cpassword_Entry.bind("<FocusIn>",on_enter2)
User_cpassword_Entry.bind("<FocusOut>",on_leave2)

User_cpassword_Line_Entry_Label = Frame(app,width=402,height=4,bg='black')
User_cpassword_Line_Entry_Label.place(x=255,y=345)
#---------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------#
def hide():
    User_password_Entry.config(show='')
    User_password_Entry.after(500, lambda: User_password_Entry.config(show="*"))
    
closeye = PhotoImage(file="Y:\\PROJECTS\\AUTOMIZED AUTOMATION\\WORK SPACE\\Assts\\Images\\openeye.png")
eyebutton = Button(app,image=closeye,bd=0,bg='#fd6f00',cursor='hand2',command=hide,activebackground='#fd6f00',activeforeground='#fd6f00')
eyebutton.place(x=630,y=247)
#---------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------#
def hide():
    User_cpassword_Entry.config(show='')
    User_cpassword_Entry.after(500, lambda: User_cpassword_Entry.config(show="*"))
    
ccloseye = PhotoImage(file="Y:\\PROJECTS\\AUTOMIZED AUTOMATION\\WORK SPACE\\Assts\\Images\\openeye.png")
ceyebutton = Button(app,image=closeye,bd=0,bg='#fd6f00',cursor='hand2',command=hide,activebackground='#fd6f00',activeforeground='#fd6f00')
ceyebutton.place(x=630,y=317)
#---------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------#
registerbutton = Button(app,text  = 'SUBMIT',bd=0,width=25,height=0,font=('Times New Roman',15),bg='#fd6f00',activebackground='#fd6f00',cursor='hand2',command=register)
registerbutton.place(x=315,y=380)
#---------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------#
forgotbutton = Button(app,text  = 'Clear?',bd=0,font=('Times New Roman',13),bg='#fa0111',activebackground='#fa0111',cursor='hand2',command=clear)
forgotbutton.place(x=600,y=350)
#---------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------#
createAccount = Label(app,text = "Do You Have an Account ",font=('Times New Roman',13,'bold'),bg='#fe0400')
createAccount.place(x = 295,y = 440)
#---------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------#
createbutton = Button(app,text  = 'Login The Application...',bd=0,font=('Times New Roman',12),bg='#f70225',activebackground='#f70225',cursor='hand2',command=login)
createbutton.place(x=480,y=438)
#---------------------------------------------------------------------------------------------------#
app.mainloop()
