#!/usr/local/bin/python3
#assignment2a.py

from tkinter import *;
from tkinter import ttk;
import math;

window = Tk();
window.title("Assignment 2a");
window.minsize(width=300, height=300);
window.maxsize(width=400, height=300);

lbl1 = Label(window, text='Please enter a grade');
lbl1.grid(column=0, row=1);

txt1 = Entry(window, width=10);
txt1.grid(column=0, row=0);



def userGrade():
    gradeentry = txt1.get()
    if txt1 in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
        if gradeentry >= 85: 
            grade = "A";
        elif gradeentry >= 75: 
            grade = "B";
        elif gradeentry >= 60: 
            grade = "C";
        else: 
            grade = "F";
    return grade;
    msg = "Something happened to " + grade;
    lbl1.configure( text = msg );
            
#def hasClicked():
   # msg = "Something happened to " + userGrade;
   # lbl1.configure( text = msg );
    
#def userGrade2(txt1):
    #txt1.get();
   # if txt1 = "A": 
    #    lettergrade = "85-100";
   # elif txt1 = "B": 
    #    lettergrade = "75-84.99";
   # elif txt1 = "C": 
   #     lettergrade = "60-74.99";
  #  elif txt1 = "F": 
   #     lettergrade = "0-59.99";
#msg = "Something happened to " + grade;
#lbl1.configure( text = msg );



btn1 = Button(window, text='Submit', command=userGrade);
btn1.grid(column=0, row=3);

window.mainloop( );