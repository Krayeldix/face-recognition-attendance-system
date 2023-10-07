#import module from tkinter for UI
from tkinter import *
from playsound import playsound
import os
from datetime import datetime;
#creating instance of TK
root=Tk()

root.configure(background="black")


def function1():
    
    os.system("py dataset_capture.py")
    
def function2():
    
    os.system("py training_dataSet.py")

def function3():

    os.system("py recognizer_alt.py")
    playsound('sound.mp3')

def function4():
    root.destroy()

def attend():
    os.startfile(os.getcwd()+"/firebase/attendance_files/attendance"+str(datetime.now().date())+'.xls')

#sitting title for the window
root.title("AUTOMATIC ATTENDANCE MANAGEMENT SYSTEM USING FACE RECOGNITION")

#creating a text label
Label(root, text="FACE RECOGNITION ATTENDANCE SYSTEM",font=("times new roman",20),fg="white",bg="red",height=3).grid(row=0,rowspan=2,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

#creating first button
Button(root,text="Creating Dataset",font=("times new roman",20),bg="#42a5f5",fg='white',command=function1).grid(row=3,columnspan=2,sticky=W+E+N+S,padx=5,pady=5)

#creating second button
Button(root,text="Training Dataset",font=("times new roman",20),bg="#42a5f5",fg='white',command=function2).grid(row=4,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

#creating third button
Button(root,text="Recognize & Taking Attendence",font=('times new roman',20),bg="#42a5f5",fg="white",command=function3).grid(row=5,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

#creating attendance button
Button(root,text="Attendance Sheet",font=('times new roman',20),bg="#42a5f5",fg="white",command=attend).grid(row=6,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

#creating exit buttom
Button(root,text="Exit",font=('times new roman',20),bg="gold",fg="white",command=function4).grid(row=8,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)


root.mainloop()
