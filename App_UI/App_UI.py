from candy import *
import webbrowser
import tkinter as tk
from tkinter import messagebox
from typing import List, Union
from difflib import get_close_matches
import json
import tkinter as tk
from PIL import Image, ImageTk
import threading
import pywhatkit
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
  if messagebox.askyesno('AUTOMATIZED AUTOMATION','Do you want close this login application?')== True:
    speak('activate code 0')
    app.destroy()
    speak('application was sucessfully closed')
  else:
    pass
app.bind("<Double 1>", close)
#---------------------------------------------------------------------------------------------------#

#-----------------------------------------MENU FRAME------------------------------------------------#
def menu_frame():
  global back
  global forward
  global img

  def back_btn():
    app_menu_frame.destroy()

  def front_btn():
    pass

  def setting():
    def app01_work_frame_back():
      app1_work_frame.destroy()

    def app01_work_frame_front():
      app1_work_frame.destroy()
      app_menu_frame.destroy()
    
##    app1_work_frame=Frame(app,width=925,height=500)
##    app1_work_frame.place(x=0,y=0)
##    app1_work_framebg = Label(app1_work_frame,image=bgimage)
##    app1_work_framebg.place(x=-2,y=-2)
##    #---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
##    bg_setting=Frame(app1_work_frame,bg="#fd7200",width=817,height=130)
##    bg_setting.place(x=52,y=90)
##    bg1_setting=Frame(app1_work_frame,bg="#fd7200",width=475,height=130)
##    bg1_setting.place(x=52,y=225)
##
##    def bg_setting_bgimg1():
##      global img1
##      img1 = ImageTk.PhotoImage(file="Y:/PROJECTS/AUTOMIZED AUTOMATION/WORK SPACE/Assts/Images/1.png")
##      bglabel.set(image=img1)
##
##    def bg_setting_bgimg2():
##      global img2
##      img2 = ImageTk.PhotoImage(file="Y:/PROJECTS/AUTOMIZED AUTOMATION/WORK SPACE/Assts/Images/2.png")
##      bglabel.configure(image=img2)
##
##    def bg_setting_bgimg3():
##      global img3
##      img3 = ImageTk.PhotoImage(file="Y:/PROJECTS/AUTOMIZED AUTOMATION/WORK SPACE/Assts/Images/3.png")
##      bglabel.configure(image=img3)
##
##    def bg_setting_bgimg4():
##      global img4
##      img4 = ImageTk.PhotoImage(file="Y:/PROJECTS/AUTOMIZED AUTOMATION/WORK SPACE/Assts/Images/4.png")
##      bglabel.configure(image=img4)
##
##    def bg_setting_bgimg5():
##      global img1
##      img1 = ImageTk.PhotoImage(file="Y:/PROJECTS/AUTOMIZED AUTOMATION/WORK SPACE/Assts/Images/1.png")
##      bglabel.configure(image=img1)
##
##    def bg_setting_bgimg6():
##      pass
##
####    bg_setting_bgimg1_changer=Button(app1_work_frame,bg='red',width=15,height=7,bd=0,text='1',command=bg_setting_bgimg1).place(x=105,y=99)
##    bg_setting_bgimg2_changer=Button(app1_work_frame,bg='red',width=15,height=7,bd=0,text='2',command=bg_setting_bgimg2).place(x=225,y=99)
##    bg_setting_bgimg3_changer=Button(app1_work_frame,bg='red',width=15,height=7,bd=0,text='3',command=bg_setting_bgimg3).place(x=345,y=99)
##    bg_setting_bgimg4_changer=Button(app1_work_frame,bg='red',width=15,height=7,bd=0,text='4',command=bg_setting_bgimg4).place(x=465,y=99)
##    bg_setting_bgimg5_changer=Button(app1_work_frame,bg='red',width=15,height=7,bd=0,text='5',command=bg_setting_bgimg5).place(x=585,y=99)
##    bg_setting_bgimg6_changer=Button(app1_work_frame,bg='red',width=15,height=7,bd=0,text='6',command=bg_setting_bgimg6).place(x=705,y=99)
##    
##    bg2_setting=Frame(app1_work_frame,bg="#fd7200",width=337,height=130)
##    bg2_setting.place(x=532,y=225)
##    bg3_setting=Frame(app1_work_frame,bg="#fd7200",width=350,height=80)
##    bg3_setting.place(x=52,y=360)
##    bg4_setting=Frame(app1_work_frame,bg="#fd7200",width=300,height=80)
##    bg4_setting.place(x=407,y=360)
##    bg5_setting=Frame(app1_work_frame,bg="#fd7200",width=157,height=80)
##    bg5_setting.place(x=712,y=360)
    speak("initialize hands")

    call(["Python","Y:\PROJECTS\AUTOMIZED AUTOMATION\WORK SPACE\mouse\Virtual Mouse.py"])

    speak("terminated hands")
  
    #---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
##    app1_work_frame_testing_label=Label(app1_work_frame,text='SETTINGS',font=("Times New Roman",24,'bold')).place(x=375,y=20)
##
##    app1_work_frame_back=PhotoImage(file="Y:\\PROJECTS\\AUTOMIZED AUTOMATION\\WORK SPACE\\Assts\\Images\\back.png")
##    app1_work_frame_back_button=Button(app1_work_frame,image=back,command=app01_work_frame_back,bd=0,bg='#fdbe00',fg='#fdbe00',activebackground='#fdbe00',cursor='hand2')
##    app1_work_frame_back_button.place(x=20,y=20)
##
##    app1_work_frame_forward=PhotoImage(file="Y:\\PROJECTS\\AUTOMIZED AUTOMATION\\WORK SPACE\\Assts\\Images\\forward.png")
##    app1_work_frame_front_button=Button(app1_work_frame,image=forward,command=app01_work_frame_front,bd=0,bg='#fdbe00',fg='#fdbe00',activebackground='#fdbe00',cursor='hand2')
##    app1_work_frame_front_button.place(x=50,y=20)
    
  def apps():
    def main_apps_work_frame_back():
      apps_work_frame.destroy()

    def main_apps_work_frame_front():
      apps_work_frame.destroy()
      app_menu_frame.destroy()

    def app1():
      def app1_back():
        app1_work_frame.destroy()
      
      app1_work_frame=Frame(app,width=925,height=500)
      app1_work_frame.place(x=0,y=0)
      global bg_app1
      bg_app1 = ImageTk.PhotoImage(file="Y:\\PROJECTS\\AUTOMIZED AUTOMATION\\WORK SPACE\\Assts\\Images\\bg2.png")
      app1_work_framebg = Label(app1_work_frame,image=bg_app1)
      app1_work_framebg.place(x=-2,y=-2)
      app1_work_frame_testing_label=Label(app1_work_frame,text='APP1',font=("Times New Roman",24,'bold')).place(x=330,y=20)

      global app1_work_frame_back
      app1_work_frame_back=PhotoImage(file="Y:\\PROJECTS\\AUTOMIZED AUTOMATION\\WORK SPACE\\Assts\\Images\\back.png")
      app1_work_frame_back_button=Button(app1_work_frame,image=app1_work_frame_back,command=app1_back,bd=0,bg='#fdbe00',fg='#fdbe00',activebackground='#fdbe00',cursor='hand2')
      app1_work_frame_back_button.place(x=20,y=20)

      global app1_work_frame_forward
      app1_work_frame_forward=PhotoImage(file="Y:\\PROJECTS\\AUTOMIZED AUTOMATION\\WORK SPACE\\Assts\\Images\\forward.png")
      app1_work_frame_front_button=Button(app1_work_frame,image=app1_work_frame_forward,command=main_apps_work_frame_front,bd=0,bg='#fdbe00',fg='#fdbe00',activebackground='#fdbe00',cursor='hand2')
      app1_work_frame_front_button.place(x=50,y=20)

    def app2():
      def app2_back():
        app2_work_frame.destroy()
      
      app2_work_frame=Frame(app,width=925,height=500)
      app2_work_frame.place(x=0,y=0)
      global bg_app2
      bg_app2 = ImageTk.PhotoImage(file="Y:\\PROJECTS\\AUTOMIZED AUTOMATION\\WORK SPACE\\Assts\\Images\\bg2.png")
      app2_work_framebg = Label(app2_work_frame,image=bg_app2)
      app2_work_framebg.place(x=-2,y=-2)
      app2_work_frame_testing_label=Label(app2_work_frame,text='APP2',font=("Times New Roman",24,'bold')).place(x=330,y=20)

      global app2_work_frame_back
      app2_work_frame_back=PhotoImage(file="Y:\\PROJECTS\\AUTOMIZED AUTOMATION\\WORK SPACE\\Assts\\Images\\back.png")
      app2_work_frame_back_button=Button(app2_work_frame,image=app2_work_frame_back,command=app2_back,bd=0,bg='#fdbe00',fg='#fdbe00',activebackground='#fdbe00',cursor='hand2')
      app2_work_frame_back_button.place(x=20,y=20)

      global app2_work_frame_forward
      app2_work_frame_forward=PhotoImage(file="Y:\\PROJECTS\\AUTOMIZED AUTOMATION\\WORK SPACE\\Assts\\Images\\forward.png")
      app2_work_frame_front_button=Button(app2_work_frame,image=app2_work_frame_forward,command=main_apps_work_frame_front,bd=0,bg='#fdbe00',fg='#fdbe00',activebackground='#fdbe00',cursor='hand2')
      app2_work_frame_front_button.place(x=50,y=20)

    def app3():
      def app3_back():
        app3_work_frame.destroy()
      
      app3_work_frame=Frame(app,width=925,height=500)
      app3_work_frame.place(x=0,y=0)
      global bg_app3
      bg_app3 = ImageTk.PhotoImage(file="Y:\\PROJECTS\\AUTOMIZED AUTOMATION\\WORK SPACE\\Assts\\Images\\bg2.png")
      app3_work_framebg = Label(app3_work_frame,image=bg_app3)
      app3_work_framebg.place(x=-2,y=-2)
      app3_work_frame_testing_label=Label(app3_work_frame,text='APP3',font=("Times New Roman",24,'bold')).place(x=330,y=20)

      global app3_work_frame_back
      app3_work_frame_back=PhotoImage(file="Y:\\PROJECTS\\AUTOMIZED AUTOMATION\\WORK SPACE\\Assts\\Images\\back.png")
      app3_work_frame_back_button=Button(app3_work_frame,image=app3_work_frame_back,command=app3_back,bd=0,bg='#fdbe00',fg='#fdbe00',activebackground='#fdbe00',cursor='hand2')
      app3_work_frame_back_button.place(x=20,y=20)

      global app3_work_frame_forward
      app3_work_frame_forward=PhotoImage(file="Y:\\PROJECTS\\AUTOMIZED AUTOMATION\\WORK SPACE\\Assts\\Images\\forward.png")
      app3_work_frame_front_button=Button(app3_work_frame,image=app3_work_frame_forward,command=main_apps_work_frame_front,bd=0,bg='#fdbe00',fg='#fdbe00',activebackground='#fdbe00',cursor='hand2')
      app3_work_frame_front_button.place(x=50,y=20)

    def app4():
      def app4_back():
        app4_work_frame.destroy()
      
      app4_work_frame=Frame(app,width=925,height=500)
      app4_work_frame.place(x=0,y=0)
      global bg_app4
      bg_app4 = ImageTk.PhotoImage(file="Y:\\PROJECTS\\AUTOMIZED AUTOMATION\\WORK SPACE\\Assts\\Images\\bg2.png")
      app4_work_framebg = Label(app4_work_frame,image=bg_app4)
      app4_work_framebg.place(x=-2,y=-2)
      app4_work_frame_testing_label=Label(app4_work_frame,text='APP4',font=("Times New Roman",24,'bold')).place(x=330,y=20)

      global app4_work_frame_back
      app4_work_frame_back=PhotoImage(file="Y:\\PROJECTS\\AUTOMIZED AUTOMATION\\WORK SPACE\\Assts\\Images\\back.png")
      app4_work_frame_back_button=Button(app4_work_frame,image=app4_work_frame_back,command=app4_back,bd=0,bg='#fdbe00',fg='#fdbe00',activebackground='#fdbe00',cursor='hand2')
      app4_work_frame_back_button.place(x=20,y=20)

      global app4_work_frame_forward
      app4_work_frame_forward=PhotoImage(file="Y:\\PROJECTS\\AUTOMIZED AUTOMATION\\WORK SPACE\\Assts\\Images\\forward.png")
      app4_work_frame_front_button=Button(app4_work_frame,image=app4_work_frame_forward,command=main_apps_work_frame_front,bd=0,bg='#fdbe00',fg='#fdbe00',activebackground='#fdbe00',cursor='hand2')
      app4_work_frame_front_button.place(x=50,y=20)

    def app5():
      def app5_back():
        app5_work_frame.destroy()
      
      app5_work_frame=Frame(app,width=925,height=500)
      app5_work_frame.place(x=0,y=0)
      global bg_app5
      bg_app5 = ImageTk.PhotoImage(file="Y:\\PROJECTS\\AUTOMIZED AUTOMATION\\WORK SPACE\\Assts\\Images\\bg2.png")
      app5_work_framebg = Label(app5_work_frame,image=bg_app5)
      app5_work_framebg.place(x=-2,y=-2)
      app5_work_frame_testing_label=Label(app5_work_frame,text='APP5',font=("Times New Roman",24,'bold')).place(x=330,y=20)

      global app5_work_frame_back
      app5_work_frame_back=PhotoImage(file="Y:\\PROJECTS\\AUTOMIZED AUTOMATION\\WORK SPACE\\Assts\\Images\\back.png")
      app5_work_frame_back_button=Button(app5_work_frame,image=app5_work_frame_back,command=app5_back,bd=0,bg='#fdbe00',fg='#fdbe00',activebackground='#fdbe00',cursor='hand2')
      app5_work_frame_back_button.place(x=20,y=20)

      global app5_work_frame_forward
      app5_work_frame_forward=PhotoImage(file="Y:\\PROJECTS\\AUTOMIZED AUTOMATION\\WORK SPACE\\Assts\\Images\\forward.png")
      app5_work_frame_front_button=Button(app5_work_frame,image=app5_work_frame_forward,command=main_apps_work_frame_front,bd=0,bg='#fdbe00',fg='#fdbe00',activebackground='#fdbe00',cursor='hand2')
      app5_work_frame_front_button.place(x=50,y=20)

    def app6():
      def app6_back():
        app6_work_frame.destroy()
      
      app6_work_frame=Frame(app,width=925,height=500)
      app6_work_frame.place(x=0,y=0)
      global bg_app6
      bg_app6 = ImageTk.PhotoImage(file="Y:\\PROJECTS\\AUTOMIZED AUTOMATION\\WORK SPACE\\Assts\\Images\\bg2.png")
      app6_work_framebg = Label(app6_work_frame,image=bg_app6)
      app6_work_framebg.place(x=-2,y=-2)
      app6_work_frame_testing_label=Label(app6_work_frame,text='APP6',font=("Times New Roman",24,'bold')).place(x=330,y=20)

      global app6_work_frame_back
      app6_work_frame_back=PhotoImage(file="Y:\\PROJECTS\\AUTOMIZED AUTOMATION\\WORK SPACE\\Assts\\Images\\back.png")
      app6_work_frame_back_button=Button(app6_work_frame,image=app6_work_frame_back,command=app6_back,bd=0,bg='#fdbe00',fg='#fdbe00',activebackground='#fdbe00',cursor='hand2')
      app6_work_frame_back_button.place(x=20,y=20)

      global app6_work_frame_forward
      app6_work_frame_forward=PhotoImage(file="Y:\\PROJECTS\\AUTOMIZED AUTOMATION\\WORK SPACE\\Assts\\Images\\forward.png")
      app6_work_frame_front_button=Button(app6_work_frame,image=app6_work_frame_forward,command=main_apps_work_frame_front,bd=0,bg='#fdbe00',fg='#fdbe00',activebackground='#fdbe00',cursor='hand2')
      app6_work_frame_front_button.place(x=50,y=20)

    def app7():
      def app7_back():
        app7_work_frame.destroy()
      
      app7_work_frame=Frame(app,width=925,height=500)
      app7_work_frame.place(x=0,y=0)
      global bg_app7
      bg_app7 = ImageTk.PhotoImage(file="Y:\\PROJECTS\\AUTOMIZED AUTOMATION\\WORK SPACE\\Assts\\Images\\bg2.png")
      app7_work_framebg = Label(app7_work_frame,image=bg_app7)
      app7_work_framebg.place(x=-2,y=-2)
      app7_work_frame_testing_label=Label(app7_work_frame,text='APP7',font=("Times New Roman",24,'bold')).place(x=330,y=20)

      global app7_work_frame_back
      app7_work_frame_back=PhotoImage(file="Y:\\PROJECTS\\AUTOMIZED AUTOMATION\\WORK SPACE\\Assts\\Images\\back.png")
      app7_work_frame_back_button=Button(app7_work_frame,image=app7_work_frame_back,command=app7_back,bd=0,bg='#fdbe00',fg='#fdbe00',activebackground='#fdbe00',cursor='hand2')
      app7_work_frame_back_button.place(x=20,y=20)

      global app7_work_frame_forward
      app7_work_frame_forward=PhotoImage(file="Y:\\PROJECTS\\AUTOMIZED AUTOMATION\\WORK SPACE\\Assts\\Images\\forward.png")
      app7_work_frame_front_button=Button(app7_work_frame,image=app7_work_frame_forward,command=main_apps_work_frame_front,bd=0,bg='#fdbe00',fg='#fdbe00',activebackground='#fdbe00',cursor='hand2')
      app7_work_frame_front_button.place(x=50,y=20)

    def app8():
      def app8_back():
        app8_work_frame.destroy()
      
      app8_work_frame=Frame(app,width=925,height=500)
      app8_work_frame.place(x=0,y=0)
      global bg_app8
      bg_app8 = ImageTk.PhotoImage(file="Y:\\PROJECTS\\AUTOMIZED AUTOMATION\\WORK SPACE\\Assts\\Images\\bg2.png")
      app8_work_framebg = Label(app8_work_frame,image=bg_app8)
      app8_work_framebg.place(x=-2,y=-2)
      app8_work_frame_testing_label=Label(app8_work_frame,text='APP8',font=("Times New Roman",24,'bold')).place(x=330,y=20)

      global app8_work_frame_back
      app8_work_frame_back=PhotoImage(file="Y:\\PROJECTS\\AUTOMIZED AUTOMATION\\WORK SPACE\\Assts\\Images\\back.png")
      app8_work_frame_back_button=Button(app8_work_frame,image=app8_work_frame_back,command=app8_back,bd=0,bg='#fdbe00',fg='#fdbe00',activebackground='#fdbe00',cursor='hand2')
      app8_work_frame_back_button.place(x=20,y=20)

      global app8_work_frame_forward
      app8_work_frame_forward=PhotoImage(file="Y:\\PROJECTS\\AUTOMIZED AUTOMATION\\WORK SPACE\\Assts\\Images\\forward.png")
      app8_work_frame_front_button=Button(app8_work_frame,image=app8_work_frame_forward,command=main_apps_work_frame_front,bd=0,bg='#fdbe00',fg='#fdbe00',activebackground='#fdbe00',cursor='hand2')
      app8_work_frame_front_button.place(x=50,y=20)
    
    apps_work_frame=Frame(app,width=925,height=500)
    apps_work_frame.place(x=0,y=0)
    apps_work_framebg = Label(apps_work_frame,image=bgimage)
    apps_work_framebg.place(x=-2,y=-2)
    apps_work_frame_testing_label=Label(apps_work_frame,text='APPLICATIONS',font=("Times New Roman",24,'bold'),bg='#fd9100').place(x=330,y=20)

    apps_work_frame_back=PhotoImage(file="Y:\\PROJECTS\\AUTOMIZED AUTOMATION\\WORK SPACE\\Assts\\Images\\back.png")
    apps_work_frame_back_button=Button(apps_work_frame,image=back,command=main_apps_work_frame_back,bd=0,bg='#fdbe00',fg='#fdbe00',activebackground='#fdbe00',cursor='hand2')
    apps_work_frame_back_button.place(x=20,y=20)

    apps_work_frame_forward=PhotoImage(file="Y:\\PROJECTS\\AUTOMIZED AUTOMATION\\WORK SPACE\\Assts\\Images\\forward.png")
    apps_work_frame_front_button=Button(apps_work_frame,image=forward,command=main_apps_work_frame_front,bd=0,bg='#fdbe00',fg='#fdbe00',activebackground='#fdbe00',cursor='hand2')
    apps_work_frame_front_button.place(x=50,y=20)
    #------------------------------------------------------apps window----------------------------------------------------------------------------------------------------------#
    global img_app1
    global img_app2
    global img_app3
    global img_app4
    global img_app5
    global img_app6
    global img_app7
    global img_app8
    img_app1=PhotoImage(file="Y:\\PROJECTS\\AUTOMIZED AUTOMATION\\WORK SPACE\\Assts\\Images\\menu.png")
    app1_button=Button(apps_work_frame,image=img_app1,width=100,height=100,command=app1,bd=0,bg='#fdbe00',fg='#fdbe00',activebackground='#fdbe00',cursor='hand2')
    app1_button.place(x=115,y=100)
    
    img_app2=PhotoImage(file="Y:\PROJECTS\AUTOMIZED AUTOMATION\WORK SPACE\Assts\Images\menu.png")
    app2_app_button=Button(apps_work_frame,image=img_app2,width=100,height=100,command=app2,bd=0,bg='#fdbe00',fg='#fdbe00',activebackground='#fdbe00',cursor='hand2')
    app2_app_button.place(x=405,y=100)

    img_app3=PhotoImage(file="Y:\PROJECTS\AUTOMIZED AUTOMATION\WORK SPACE\Assts\Images\menu.png")
    app3_button=Button(apps_work_frame,image=img_app3,width=100,height=100,command=app3,bd=0,bg='#fdbe00',fg='#fdbe00',activebackground='#fdbe00',cursor='hand2')
    app3_button.place(x=700,y=100)

    img_app4=PhotoImage(file="Y:\PROJECTS\AUTOMIZED AUTOMATION\WORK SPACE\Assts\Images\menu.png")
    app4_button=Button(apps_work_frame,image=img_app4,width=100,height=100,command=app4,bd=0,bg='red',fg='#fdbe00',activebackground='#fdbe00',cursor='hand2')
    app4_button.place(x=115,y=320)

    img_app5=PhotoImage(file="Y:\PROJECTS\AUTOMIZED AUTOMATION\WORK SPACE\Assts\Images\menu.png")
    app5_button=Button(apps_work_frame,image=img_app5,width=100,height=100,command=app5,bd=0,bg='#fdbe00',fg='#fdbe00',activebackground='#fdbe00',cursor='hand2')
    app5_button.place(x=405,y=320)

    img_app6=PhotoImage(file="Y:\PROJECTS\AUTOMIZED AUTOMATION\WORK SPACE\Assts\Images\menu.png")
    app6_button=Button(apps_work_frame,image=img_app6,width=100,height=100,command=app6,bd=0,bg='#fdbe00',fg='#fdbe00',activebackground='#fdbe00',cursor='hand2')
    app6_button.place(x=700,y=320)

    img_app7=PhotoImage(file="Y:\PROJECTS\AUTOMIZED AUTOMATION\WORK SPACE\Assts\Images\menu.png")
    app7_button=Button(apps_work_frame,image=img_app7,width=100,height=100,command=app7,bd=0,bg='red',fg='#fdbe00',activebackground='#fdbe00',cursor='hand2')
    app7_button.place(x=260,y=210)

    img_app8=PhotoImage(file="Y:\PROJECTS\AUTOMIZED AUTOMATION\WORK SPACE\Assts\Images\menu.png")
    app8_button=Button(apps_work_frame,image=img_app8,width=100,height=100,command=app8,bd=0,bg='#fdbe00',fg='#fdbe00',activebackground='#fdbe00',cursor='hand2')
    app8_button.place(x=552,y=210)
    #----------------------------------------------------------------------------------------------------------------------------------------------------------------#
  def app3():
    def app03_work_frame_back():
      app3_work_frame.destroy()

    def app03_work_frame_front():
      app3_work_frame.destroy()
      app_menu_frame.destroy()
    
    app3_work_frame=Frame(app,width=925,height=500)
    app3_work_frame.place(x=0,y=0)
    app3_work_framebg = Label(app3_work_frame,image=bgimage)
    app3_work_framebg.place(x=-2,y=-2)
    app3_work_frame_testing_label=Label(app3_work_frame,text='ABOUT',font=('Times New Roman',25,'bold'),bg='#fd9100').place(x=390,y=20)

    app3_work_frame_back=PhotoImage(file="Y:\\PROJECTS\\AUTOMIZED AUTOMATION\\WORK SPACE\\Assts\\Images\\back.png")
    app3_work_frame_back_button=Button(app3_work_frame,image=back,command=app03_work_frame_back,bd=0,bg='#fdbe00',fg='#fdbe00',activebackground='#fdbe00',cursor='hand2')
    app3_work_frame_back_button.place(x=20,y=20)

    app3_work_frame_forward=PhotoImage(file="Y:\\PROJECTS\\AUTOMIZED AUTOMATION\\WORK SPACE\\Assts\\Images\\forward.png")
    app3_work_frame_front_button=Button(app3_work_frame,image=forward,command=app03_work_frame_front,bd=0,bg='#fdbe00',fg='#fdbe00',activebackground='#fdbe00',cursor='hand2')
    app3_work_frame_front_button.place(x=50,y=20)


    bg_about_dev=Frame(app3_work_frame,bg="#fd7200",width=823,height=130)
    bg_about_dev.place(x=50,y=90)
    bg_about_label_dev=Label(bg_about_dev,text='DEVELOPERS',font=('Times New Roman',15,'bold'),bg='#fd7200').place(x=3,y=3)
    
    dev1=Label(bg_about_dev,text='"DHANESBABU.S"',font=('Times New Roman',20,'bold'),bg='#fd7200').place(x=30,y=50)
    dev2=Label(bg_about_dev,text='BALAMURUGAN.M',font=('Times New Roman',20),bg='#fd7200').place(x=300,y=50)
    dev3=Label(bg_about_dev,text='DHANUSH.S',font=('Times New Roman',20,),bg='#fd7200').place(x=600,y=50)

    bg_about_lic=Frame(app3_work_frame,bg="#fd7200",width=823,height=250)
    bg_about_lic.place(x=50,y=225)
    bg_about_label_lic=Label(bg_about_lic,text='LIENCES',font=('Times New Roman',15,'bold'),bg='#fd7200').place(x=3,y=3)

    lic=Label(bg_about_lic,text="HELLOW",font=("Times Nea Roman",9),bg='#fd7200').place(x=30,y=30)

    

  def app4():
    def app04_work_frame_back():
      app4_work_frame.destroy()

    def app04_work_frame_front():
      app4_work_frame.destroy()
      app4_menu_frame.destroy()
    
##      app4_work_frame=Frame(app,width=925,height=500)
##      app4_work_frame.place(x=0,y=0)
##      app4_work_framebg = Label(app4_work_frame,image=bgimage)
##      app4_work_framebg.place(x=-2,y=-2)
##      app4_work_frame_testing_label=Label(app4_work_frame,text='REACH ME',font=('Times New Roman',25,'bold')).place(x=370,y=20)
##
##      app4_work_frame_back=PhotoImage(file="Y:\\PROJECTS\\AUTOMIZED AUTOMATION\\WORK SPACE\\Assts\\Images\\back.png")
##      app4_work_frame_back_button=Button(app4_work_frame,image=back,command=app04_work_frame_back,bd=0,bg='#fdbe00',fg='#fdbe00',activebackground='#fdbe00',cursor='hand2')
##      app4_work_frame_back_button.place(x=20,y=20)
##
##      app4_work_frame_forward=PhotoImage(file="Y:\\PROJECTS\\AUTOMIZED AUTOMATION\\WORK SPACE\\Assts\\Images\\forward.png")
##      app4_work_frame_front_button=Button(app4_work_frame,image=forward,command=app04_work_frame_front,bd=0,bg='#fdbe00',fg='#fdbe00',activebackground='#fdbe00',cursor='hand2')
##      app4_work_frame_front_button.place(x=50,y=20)
    call(["Python","Y:\PROJECTS\AUTOMIZED AUTOMATION\WORK SPACE\Automation\Automation.pyw"])
      

  def app5():
    def app05_work_frame_back():
      app5_work_frame.destroy()

    def app05_work_frame_front():
      app5_work_frame.destroy()
      app_menu_frame.destroy()

    def r_navi():

      def app9():
        webbrowser.open("https://time.com/")

      def app10():
        webbrowser.open("https://web.whatsapp.com/")

      def app11():
        webbrowser.open("ttps://www.odoo.com/page/all-apps")

      def app12():
        webbrowser.open("https://gemoo.com/tools/screenshot-editor-online/")

      def app13():
        webbrowser.open("https://imagecolorpicker.com/en")

      def app14():
        webbrowser.open("https://www.the-qrcode-generator.com/")

      def app15():
        webbrowser.open("https://www.lucidchart.com/pages")

      def app16():
        webbrowser.open("https://scholar.google.com/schhp?hl=en-US")
      
      app1_button.destroy()
      app2_button.destroy()
      app3_button.destroy()
      app4_button.destroy()
      app5_button.destroy()
      app6_button.destroy()
      app7_button.destroy()
      app8_button.destroy()

      global img_app9
      global img_app10
      global img_app11
      global img_app12
      global img_app13
      global img_app14
      global img_app15
      global img_app16
      global app9_button
      global app10_button
      global app11_button
      global app12_button
      global app13_button
      global app14_button
      global app15_button
      global app16_button
      img_app9=PhotoImage(file="Y:\\PROJECTS\\AUTOMIZED AUTOMATION\\WORK SPACE\\Assts\\Images\\news.png")
      app9_button=Button(app5_work_frame,image=img_app9,width=100,height=100,command=app1,bd=0,bg='#fdbe00',fg='#fdbe00',activebackground='#fdbe00',cursor='hand2')
      app9_button.place(x=115,y=100)
      
      img_app10=PhotoImage(file="Y:\\PROJECTS\\AUTOMIZED AUTOMATION\\WORK SPACE\\Assts\\Images\\whatsapp.png")
      app10_button=Button(app5_work_frame,image=img_app10,width=100,height=100,command=app2,bd=0,bg='#fd7e00',fg='#fd7e00',activebackground='#fdbe00',cursor='hand2')
      app10_button.place(x=405,y=100)

      img_app11=PhotoImage(file="Y:\\PROJECTS\\AUTOMIZED AUTOMATION\\WORK SPACE\\Assts\\Images\\business.png")
      app11_button=Button(app5_work_frame,image=img_app11,width=100,height=100,command=app3,bd=0,bg='#fd3000',fg='#fd3000',activebackground='#fdbe00',cursor='hand2')
      app11_button.place(x=700,y=100)

      img_app12=PhotoImage(file="Y:\\PROJECTS\\AUTOMIZED AUTOMATION\\WORK SPACE\\Assts\\Images\\screen.png")
      app12_button=Button(app5_work_frame,image=img_app12,width=100,height=100,command=app4,bd=0,bg='#fd5c00',fg='#fd5c00',activebackground='#fdbe00',cursor='hand2')
      app12_button.place(x=115,y=320)

      img_app13=PhotoImage(file="Y:\\PROJECTS\\AUTOMIZED AUTOMATION\\WORK SPACE\\Assts\\Images\\color.png")
      app13_button=Button(app5_work_frame,image=img_app13,width=100,height=100,command=app5,bd=0,bg='#fc0005',fg='#fc0005',activebackground='#fdbe00',cursor='hand2')
      app13_button.place(x=405,y=320)

      img_app14=PhotoImage(file="Y:\\PROJECTS\\AUTOMIZED AUTOMATION\\WORK SPACE\\Assts\\Images\\qr.png")
      app14_button=Button(app5_work_frame,image=img_app14,width=100,height=100,command=app6,bd=0,bg='#f20442',fg='#f20442',activebackground='#fdbe00',cursor='hand2')
      app14_button.place(x=700,y=320)

      img_app15=PhotoImage(file="Y:\\PROJECTS\\AUTOMIZED AUTOMATION\\WORK SPACE\\Assts\\Images\\draw.png")
      app15_button=Button(app5_work_frame,image=img_app15,width=100,height=100,command=app7,bd=0,bg='#fd6f00',fg='#fd6f00',activebackground='#fdbe00',cursor='hand2')
      app15_button.place(x=260,y=210)

      img_app16=PhotoImage(file="Y:\\PROJECTS\\AUTOMIZED AUTOMATION\\WORK SPACE\\Assts\\Images\\note.png")
      app16_button=Button(app5_work_frame,image=img_app16,width=100,height=100,command=app8,bd=0,bg='#fd1200',fg='#fd1200',activebackground='#fdbe00',cursor='hand2')
      app16_button.place(x=552,y=210)

    def l_navi():
      
      app9_button.destroy()
      app10_button.destroy()
      app11_button.destroy()
      app12_button.destroy()
      app13_button.destroy()
      app14_button.destroy()
      app15_button.destroy()
      app16_button.destroy()

      global img_app1
      global img_app2
      global img_app3
      global img_app4
      global img_app5
      global img_app6
      global img_app7
      global img_app8

      img_app1=PhotoImage(file="Y:\\PROJECTS\\AUTOMIZED AUTOMATION\\WORK SPACE\\Assts\\Images\\pdf.png")
      app1_button=Button(app5_work_frame,image=img_app1,width=100,height=100,command=app1,bd=0,bg='#fdbe00',fg='#fdbe00',activebackground='#fdbe00',cursor='hand2')
      app1_button.place(x=115,y=100)
      
      img_app2=PhotoImage(file="Y:\\PROJECTS\\AUTOMIZED AUTOMATION\\WORK SPACE\\Assts\\Images\\123.png")
      app2_button=Button(app5_work_frame,image=img_app2,width=100,height=100,command=app2,bd=0,bg='#fd7e00',fg='#fdbe00',activebackground='#fdbe00',cursor='hand2')
      app2_button.place(x=405,y=100)

      img_app3=PhotoImage(file="Y:\\PROJECTS\\AUTOMIZED AUTOMATION\\WORK SPACE\\Assts\\Images\\chatgpt.png")
      app3_button=Button(app5_work_frame,image=img_app3,width=100,height=100,command=app3,bd=0,bg='#fd3000',fg='#fdbe00',activebackground='#fdbe00',cursor='hand2')
      app3_button.place(x=700,y=100)

      img_app4=PhotoImage(file="Y:\\PROJECTS\\AUTOMIZED AUTOMATION\\WORK SPACE\\Assts\\Images\\image.png")
      app4_button=Button(app5_work_frame,image=img_app4,width=100,height=100,command=app4,bd=0,bg='#fd5c00',fg='#fd5c00',activebackground='#fdbe00',cursor='hand2')
      app4_button.place(x=115,y=320)

      img_app5=PhotoImage(file="Y:\\PROJECTS\\AUTOMIZED AUTOMATION\\WORK SPACE\\Assts\\Images\\vs.png")
      app5_button=Button(app5_work_frame,image=img_app5,width=100,height=100,command=app5,bd=0,bg='#fc0005',fg='#fdbe00',activebackground='#fdbe00',cursor='hand2')
      app5_button.place(x=405,y=320)

      img_app6=PhotoImage(file="Y:\\PROJECTS\\AUTOMIZED AUTOMATION\\WORK SPACE\\Assts\\Images\\code.png")
      app6_button=Button(app5_work_frame,image=img_app6,width=100,height=100,command=app6,bd=0,bg='#f20442',fg='#fdbe00',activebackground='#fdbe00',cursor='hand2')
      app6_button.place(x=700,y=320)

      img_app7=PhotoImage(file="Y:\\PROJECTS\\AUTOMIZED AUTOMATION\\WORK SPACE\\Assts\\Images\\text.png")
      app7_button=Button(app5_work_frame,image=img_app7,width=100,height=100,command=app7,bd=0,bg='#fd6f00',fg='#fdbe00',activebackground='#fdbe00',cursor='hand2')
      app7_button.place(x=260,y=210)

      img_app8=PhotoImage(file="Y:\\PROJECTS\\AUTOMIZED AUTOMATION\\WORK SPACE\\Assts\\Images\\vr.png")
      app8_button=Button(app5_work_frame,image=img_app8,width=100,height=100,command=app8,bd=0,bg='#fd1200',fg='#fd1200',activebackground='#fdbe00',cursor='hand2')
      app8_button.place(x=552,y=210)

      

    def app1():
      webbrowser.open("https://www.ilovepdf.com/")

    def app2():
      webbrowser.open("https://123apps.com/")

    def app3():
      webbrowser.open("https://chat.openai.com/")

    def app4():
      webbrowser.open("https://www.simpleimageresizer.com/image-converter#google_vignette")

    def app5():
      webbrowser.open("https://vscode.dev/")

    def app6():
      webbrowser.open("https://www.codeconvert.ai/free-converter")

    def app7():
      webbrowser.open("https://www.wordstream.com/keywords")

    def app8():
      webbrowser.open("https://learn.framevr.io/")
    
    
    app5_work_frame=Frame(app,width=925,height=500)
    app5_work_frame.place(x=0,y=0)
    app5_work_framebg = Label(app5_work_frame,image=bgimage)
    app5_work_framebg.place(x=-2,y=-2)
    

    app5_work_frame_back=PhotoImage(file="Y:\\PROJECTS\\AUTOMIZED AUTOMATION\\WORK SPACE\\Assts\\Images\\back.png")
    app5_work_frame_back_button=Button(app5_work_frame,image=back,command=app05_work_frame_back,bd=0,bg='#fdbe00',fg='#fdbe00',activebackground='#fdbe00',cursor='hand2')
    app5_work_frame_back_button.place(x=20,y=20)

    app5_work_frame_forward=PhotoImage(file="Y:\\PROJECTS\\AUTOMIZED AUTOMATION\\WORK SPACE\\Assts\\Images\\forward.png")
    app5_work_frame_front_button=Button(app5_work_frame,image=forward,command=app05_work_frame_front,bd=0,bg='#fdbe00',fg='#fdbe00',activebackground='#fdbe00',cursor='hand2')
    app5_work_frame_front_button.place(x=50,y=20)

    global app_navi_work_frame_r
    app_navi_work_frame_r=PhotoImage(file="Y:\\PROJECTS\\AUTOMIZED AUTOMATION\\WORK SPACE\\Assts\\Images\\web_app_navi_r.png")
    app_navi_work_frame_r_button=Button(app5_work_frame,image=app_navi_work_frame_r,command=r_navi,bd=0,bg='#f60229',fg='#fdbe00',activebackground='#fdbe00',cursor='hand2')
    app_navi_work_frame_r_button.place(x=462,y=465)

    global app_navi_work_frame_l
    app_navi_work_frame_l=PhotoImage(file="Y:\\PROJECTS\\AUTOMIZED AUTOMATION\\WORK SPACE\\Assts\\Images\\web_app_navi_l.png")
    app_navi_work_frame_l_button=Button(app5_work_frame,image=app_navi_work_frame_l,command=l_navi,bd=0,bg='#f60229',fg='#fdbe00',activebackground='#fdbe00',cursor='hand2')
    app_navi_work_frame_l_button.place(x=423,y=465)

    

    global img_app1
    global img_app2
    global img_app3
    global img_app4
    global img_app5
    global img_app6
    global img_app7
    global img_app8
    img_app1=PhotoImage(file="Y:\\PROJECTS\\AUTOMIZED AUTOMATION\\WORK SPACE\\Assts\\Images\\pdf.png")
    app1_button=Button(app5_work_frame,image=img_app1,width=100,height=100,command=app1,bd=0,bg='#fdbe00',fg='#fdbe00',activebackground='#fdbe00',cursor='hand2')
    app1_button.place(x=115,y=100)
    
    img_app2=PhotoImage(file="Y:\\PROJECTS\\AUTOMIZED AUTOMATION\\WORK SPACE\\Assts\\Images\\123.png")
    app2_button=Button(app5_work_frame,image=img_app2,width=100,height=100,command=app2,bd=0,bg='#fd7e00',fg='#fdbe00',activebackground='#fdbe00',cursor='hand2')
    app2_button.place(x=405,y=100)

    img_app3=PhotoImage(file="Y:\\PROJECTS\\AUTOMIZED AUTOMATION\\WORK SPACE\\Assts\\Images\\chatgpt.png")
    app3_button=Button(app5_work_frame,image=img_app3,width=100,height=100,command=app3,bd=0,bg='#fd3000',fg='#fdbe00',activebackground='#fdbe00',cursor='hand2')
    app3_button.place(x=700,y=100)

    img_app4=PhotoImage(file="Y:\\PROJECTS\\AUTOMIZED AUTOMATION\\WORK SPACE\\Assts\\Images\\image.png")
    app4_button=Button(app5_work_frame,image=img_app4,width=100,height=100,command=app4,bd=0,bg='#fd5c00',fg='#fdbe00',activebackground='#fdbe00',cursor='hand2')
    app4_button.place(x=115,y=320)

    img_app5=PhotoImage(file="Y:\\PROJECTS\\AUTOMIZED AUTOMATION\\WORK SPACE\\Assts\\Images\\vs.png")
    app5_button=Button(app5_work_frame,image=img_app5,width=100,height=100,command=app5,bd=0,bg='#fc0005',fg='#fdbe00',activebackground='#fdbe00',cursor='hand2')
    app5_button.place(x=405,y=320)

    img_app6=PhotoImage(file="Y:\\PROJECTS\\AUTOMIZED AUTOMATION\\WORK SPACE\\Assts\\Images\\code.png")
    app6_button=Button(app5_work_frame,image=img_app6,width=100,height=100,command=app6,bd=0,bg='#f20442',fg='#fdbe00',activebackground='#fdbe00',cursor='hand2')
    app6_button.place(x=700,y=320)

    img_app7=PhotoImage(file="Y:\\PROJECTS\\AUTOMIZED AUTOMATION\\WORK SPACE\\Assts\\Images\\text.png")
    app7_button=Button(app5_work_frame,image=img_app7,width=100,height=100,command=app7,bd=0,bg='#fd6f00',fg='#fdbe00',activebackground='#fdbe00',cursor='hand2')
    app7_button.place(x=260,y=210)

    img_app8=PhotoImage(file="Y:\\PROJECTS\\AUTOMIZED AUTOMATION\\WORK SPACE\\Assts\\Images\\vr.png")
    app8_button=Button(app5_work_frame,image=img_app8,width=100,height=100,command=app8,bd=0,bg='#fd1200',fg='#fdbe00',activebackground='#fdbe00',cursor='hand2')
    app8_button.place(x=552,y=210)

    app5_label=Label(app5_work_frame,text='WEBNAV',font=("Times New Roman",24,'bold'),bg='#fd9100').place(x=382,y=20)


  def app6():
    def app06_work_frame_back():
      app6_work_frame.destroy()

    def app06_work_frame_front():
      app6_work_frame.destroy()
      app6_menu_frame.destroy()
    
    app6_work_frame=Frame(app,width=925,height=500)
    app6_work_frame.place(x=0,y=0)
    app6_work_framebg = Label(app6_work_frame,image=bgimage)
    app6_work_framebg.place(x=-2,y=-2)
    app6_work_frame_testing_label=Label(app6_work_frame,text='this is chat bot frame').place(x=500,y=300)
    #-------------------------------------------------------------------CAHT BOT-------------------------------------------------------------------------------------------------------------------#
    def load_knowledge_base(file_path: str) -> dict:
        with open(file_path, 'r') as file:
            data: dict = json.load(file)
        return data

    def save_knowledge_base(file_path: str, data: dict):
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=2)

    def find_best_match(user_question: str, questions: List[str]) -> Union[str, None]:
        matches: List = get_close_matches(user_question, questions, n=1, cutoff=0.6)
        return matches[0] if matches else None

    def get_answer_for_question(question: str, knowledge_base: dict) -> Union[str, None]:
        for q in knowledge_base["questions"]:
            if q["question"] == question:
                return q["answer"]
        return None

    def teach_bot(new_question: str, new_answer: str, knowledge_base: dict):
        knowledge_base["questions"].append({"question": new_question, "answer": new_answer})
        save_knowledge_base("Y:\PROJECTS\AUTOMIZED AUTOMATION\WORK SPACE\Assts\data_center\knowledge_base.json", knowledge_base)
        messagebox.askyesno("Success", "Thank you! The bot learned a new response.")

    def chat():
        knowledge_base: dict = load_knowledge_base("Y:\PROJECTS\AUTOMIZED AUTOMATION\WORK SPACE\Assts\data_center\knowledge_base.json")

        def send_message():
            user_input = entry.get()
            entry.delete(0, tk.END)

            if user_input.lower() == 'quit':
                root.destroy()
                return

            best_match = find_best_match(user_input, [q["question"] for q in knowledge_base["questions"]])

            if best_match:
                answer = get_answer_for_question(best_match, knowledge_base)
                if answer:
                    chat_history.config(state=tk.NORMAL)
##                    chat_history.insert(tk.END, f"You: {user_input}\n", "user")
                    chat_history.insert(tk.END, f"CANDY: {answer}\n\n", "bot")
                    chat_history.config(state=tk.DISABLED)
                else:
                    messagebox.askyesno("AUTOMIZED AUTOMATION", "Bot: I don't know the answer. Can you teach me?")
                    teach_window(best_match)
            else:
                messagebox.askyesno("AUTOMIZED AUTOMATION", "Bot: I don't know the answer. Can you teach me?")
                teach_window(user_input)

        def teach_window(question):
            teach_window = tk.Toplevel(app6_work_frame)
            teach_window.title("Teach Bot")
            teach_window.geometry('500x500+300+200')
            teach_window.resizable(0,0)

            tk.Label(teach_window, text="Question:").pack()
            new_question_entry = tk.Entry(teach_window)
            new_question_entry.insert(tk.END, question)
            new_question_entry.pack()

            tk.Label(teach_window, text="Answer:").pack()
            new_answer_entry = tk.Entry(teach_window)
            new_answer_entry.pack()

            def teach_bot_gui():
                new_question = new_question_entry.get()
                new_answer = new_answer_entry.get()
                if new_question and new_answer:
                    teach_bot(new_question, new_answer, knowledge_base)
                    teach_window.destroy()
                else:
                    messagebox.showerror("Error", "Both question and answer are required.")

            tk.Button(teach_window, text="Teach Bot", command=teach_bot_gui).pack()

        

        

        chat_history =Text(app6_work_frame, width=107, height=23, wrap=tk.WORD,bd=0,bg="#fd7200")
        chat_history.place(x=30, y=70)
##        chat_history.tag_configure("user", justify="center",font=("Times New Roman",20,"bold"))
        chat_history.tag_configure("bot", justify="center",foreground="black",font=("Times New Roman",20,"bold"))

        def on_enter(event):
          if entry.get()=='CHAT WITH ME NOW...':
            entry.delete(0,END)

        def on_leave(event):
          if entry.get()=='':
            entry.insert(0,'CHAT WITH ME NOW...')

        entry = tk.Entry(app6_work_frame, width=25,bd=0,bg="#fd7200",font=('Times New Roman',23))
        entry.place(x=260, y=452)
        entry.insert(0,'CHAT WITH ME NOW...')
        entry.bind("<Return>", lambda event: send_message())
        entry.bind("<FocusIn>",on_enter)
        entry.bind("<FocusOut>",on_leave)
        User_name_Line_Entry_Label = Frame(app6_work_frame,width=402,height=4,bg='black')
        User_name_Line_Entry_Label.place(x=260,y=487)

        send_button = tk.Button(app6_work_frame, text="Send", command=send_message)
        send_button.place(x=100, y=500)

        

    if __name__ == "__main__":
        chat()

    
    #----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

##    textarea=Text(app6_work_frame,height=13,width=61,font=("Times New Roman",20,"bold"),bg="#fd7200",bd=0,wrap='word').place(x=30,y=70)
  

 

    app6_work_frame_back=PhotoImage(file="Y:\\PROJECTS\\AUTOMIZED AUTOMATION\\WORK SPACE\\Assts\\Images\\back.png")
    app6_work_frame_back_button=Button(app6_work_frame,image=back,command=app06_work_frame_back,bd=0,bg='#fdbe00',fg='#fdbe00',activebackground='#fdbe00',cursor='hand2')
    app6_work_frame_back_button.place(x=20,y=20)

    app6_work_frame_forward=PhotoImage(file="Y:\\PROJECTS\\AUTOMIZED AUTOMATION\\WORK SPACE\\Assts\\Images\\forward.png")
    app6_work_frame_front_button=Button(app6_work_frame,image=forward,command=app06_work_frame_front,bd=0,bg='#fdbe00',fg='#fdbe00',activebackground='#fdbe00',cursor='hand2')
    app6_work_frame_front_button.place(x=50,y=20)

    mllabel = Label(app6_work_frame,text="MINDFLOW",font=("Times New Roman",20,"bold"),bg="#fd7200").place(x=380,y=20)

  app_menu_frame=Frame(app,width=925,height=500)
  app_menu_frame.place(x=0,y=0)
  app_menu_framebg = Label(app_menu_frame,image=bgimage)
  app_menu_framebg.place(x=-2,y=-2)
  
  back=PhotoImage(file="Y:\\PROJECTS\\AUTOMIZED AUTOMATION\\WORK SPACE\\Assts\\Images\\back.png")
  back_button=Button(app_menu_frame,image=back,command=back_btn,bd=0,bg='#fdbe00',fg='#fdbe00',activebackground='#fdbe00',cursor='hand2')
  back_button.place(x=20,y=20)
  
  forward=PhotoImage(file="Y:\\PROJECTS\\AUTOMIZED AUTOMATION\\WORK SPACE\\Assts\\Images\\forward.png")
  front_button=Button(app_menu_frame,image=forward,command=front_btn,bd=0,bg='#fdbe00',fg='#fdbe00',activebackground='#fdbe00',cursor='hand2')
  front_button.place(x=50,y=20)

  app_menu_conformation_lb = Label(app_menu_frame,text='APPLIACTION MENU',font=('Times New Roman',25,'bold'),bg='#fd9100').place(x=280,y=40)
  #-------------------------------------------------------------------------------------------------------------------------------------------------#
  global img1
  img1=PhotoImage(file="Y:\\PROJECTS\\AUTOMIZED AUTOMATION\\WORK SPACE\\Assts\\Images\\setting.png")
  setting_button=Button(app_menu_frame,image=img1,width=100,height=100,command=setting,bd=0,bg='#fdbe00',fg='#fdbe00',activebackground='#fdbe00',cursor='hand2')
  setting_button.place(x=115,y=140)
  #-------------------------------------------------------------------------------------------------------------------------------------------------#

  #-------------------------------------------------------------------------------------------------------------------------------------------------#
  global img2
  img2=PhotoImage(file="Y:\\PROJECTS\\AUTOMIZED AUTOMATION\\WORK SPACE\\Assts\\Images\\apps.png")
  apps_button=Button(app_menu_frame,image=img2,width=100,height=100,command=apps,bd=0,bg='#fd7200',fg='#fd7200',activebackground='#fdbe00',cursor='hand2')
  apps_button.place(x=405,y=140)
  #-------------------------------------------------------------------------------------------------------------------------------------------------#

  #-------------------------------------------------------------------------------------------------------------------------------------------------#
  global img3
  img3=PhotoImage(file="Y:\\PROJECTS\\AUTOMIZED AUTOMATION\\WORK SPACE\\Assts\\Images\\about.png")
  app3_button=Button(app_menu_frame,image=img3,width=100,height=100,command=app3,bd=0,bg='#fd1800',fg='#fd1800',activebackground='#fdbe00',cursor='hand2')
  app3_button.place(x=700,y=140)
  #-------------------------------------------------------------------------------------------------------------------------------------------------#

  #-------------------------------------------------------------------------------------------------------------------------------------------------#
  global img4
  img4=PhotoImage(file="Y:\\PROJECTS\\AUTOMIZED AUTOMATION\\WORK SPACE\\Assts\\Images\\contact.png")
  app4_button=Button(app_menu_frame,image=img4,width=100,height=100,command=app4,bd=0,bg='#fd5c00',fg='#fdbe00',activebackground='#fdbe00',cursor='hand2')
  app4_button.place(x=115,y=320)
  #-------------------------------------------------------------------------------------------------------------------------------------------------#

  #-------------------------------------------------------------------------------------------------------------------------------------------------#
  global img5
  img5=PhotoImage(file="Y:\\PROJECTS\\AUTOMIZED AUTOMATION\\WORK SPACE\\Assts\\Images\\link.png")
  app5_button=Button(app_menu_frame,image=img5,width=100,height=100,command=app5,bd=0,bg='#fd0003',fg='#fd0003',activebackground='#fdbe00',cursor='hand2')
  app5_button.place(x=405,y=320)
  #-------------------------------------------------------------------------------------------------------------------------------------------------#

  #-------------------------------------------------------------------------------------------------------------------------------------------------#
  global img6
  img6=PhotoImage(file="Y:\\PROJECTS\\AUTOMIZED AUTOMATION\\WORK SPACE\\Assts\\Images\\roadmap.png")
  app6_button=Button(app_menu_frame,image=img6,width=100,height=100,command=app6,bd=0,bg='#f2043f',fg='#f2043f',activebackground='#fdbe00',cursor='hand2')
  app6_button.place(x=700,y=320)
  #-------------------------------------------------------------------------------------------------------------------------------------------------#
  
img=PhotoImage(file="Y:\\PROJECTS\\AUTOMIZED AUTOMATION\\WORK SPACE\\Assts\\Images\\menu.png")
menu_button=Button(app,image=img,command=menu_frame,bd=0,bg='#fdbe00',fg='#fdbe00',activebackground='#fdbe00',cursor='hand2')
menu_button.place(x=30,y=30)

#---------------------------------------------------------------------------------------------------#
##gif_frames = []
##frame_delay = 0
##def gif():
##    global frame_delay
##    print('started')
##    gif_file = Image.open('frame1.gif')
##    for r in range(0,gif_file.n_frames):
##        gif_file.seek(r)
##        gif_frames.append(gif_file.copy())
##    frame_delay = gif_file.info['duration']
##    print('complete')
##    play()
##
##frame_count = -1
##def play():
##    global frame_count, current_frame
##    if frame_count >= len(gif_frames) - 1:
##        frame_count = -1
##    else:
##        frame_count += 1
##    current_frame = ImageTk.PhotoImage(gif_frames[frame_count])
##    labelg.config(image=current_frame)
##    app.after(frame_delay,play)
##
##def test():
##    call(["Python","Y:\PROJECTS\AUTOMIZED AUTOMATION\WORK SPACE\Automation\Automation.py"])
##
##
##
##labelg = tk.Button(app,bg="#fd7200",bd=0,command=test,cursor='hand2')
##labelg.place(x=270,y=68)
##threading.Thread(target=gif).start()

app.mainloop()

