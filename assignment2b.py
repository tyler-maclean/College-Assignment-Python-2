#!/usr/local/bin/python3
#assignment2a.py

from tkinter import *;
from tkinter import ttk;

window = Tk();
window.title("Assignment 2a");
window.minsize(width=300, height=300);
window.maxsize(width=400, height=300);


lbl1 = Label(window, text='Please choose a pizza size');
lbl1.grid(column=0, row=1);

sizes = ("Choose Size", "Small", "Medium", "Large", "Extra-Large")
select1 = ttk.Combobox( window, values=sizes, width=20 );
select1.current(0);
select1.grid(column=0, row=0);

checkbox1 = StringVar( );
check1 = Checkbutton(window, text="Pepperoni", variable=checkbox1);

checkbox2 = StringVar( );
check2 = Checkbutton(window, text="Cheese", variable=checkbox2);

checkbox3 = StringVar( );
check3 = Checkbutton(window, text="Olive", variable=checkbox3);

checkbox4 = StringVar( );
check4 = Checkbutton(window, text="Pineapple", variable=checkbox4);

checkbox5 = StringVar( );
check5 = Checkbutton(window, text="Ham", variable=checkbox5);

check1.grid(column=1, row=1);
check2.grid(column=2, row=1);
check3.grid(column=1, row=2);
check4.grid(column=2, row=2);
check5.grid(column=1, row=3);

window.mainloop( );