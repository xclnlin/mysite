#!/usr/bin/python
# -*- coding: UTF-8 -*-

import tkinter as tk

win = tk.Tk()
win.title('My Canvas')
win.geometry('400x400')

# create a canvas
canvas = tk.Canvas(win, bg='blue', width=200, height=100)

# put a picture
image_file = tk.PhotoImage(file='ins.gif')
image = canvas.create_image(0, 0, anchor='nw', image=image_file)

# draw some graphics
x0, x1, y0, y1 = 50, 50, 80, 80
line = canvas.create_line(x0, x1, y0, y1, fill='red')
oval = canvas.create_oval(x0, x1, y0, y1)
arc = canvas.create_arc(x0+30, x1+30, y0+20, y1+20, start=45, extent=135)
rect = canvas.create_rectangle(x0+30, x1+30, y0-30, y1-30)

canvas.pack()

# move the graphic
def moveitDown():
    canvas.move(rect, 0, 2)

def moveitUp():
    canvas.move(rect, 0, -2)

def moveitL():
    canvas.move(rect, 2, 0)

def moveitR():
    canvas.move(rect, -2, 0)

# button
b1 = tk.Button(win, text='Up', command=moveitUp).pack()
b2 = tk.Button(win, text='Down', command=moveitDown).pack()
b3 = tk.Button(win, text='Left', command=moveitL).pack()
b4 = tk.Button(win, text='Right', command=moveitR).pack()

win.mainloop()