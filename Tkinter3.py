#!/usr/bin/python
# -*- coding: UTF-8 -*-

import tkinter as tk

win = tk.Tk()
win.title('my win 3')
win.geometry('300x1000')

# 创建一个label用于显示,并通过变量传递值
var1 = tk.StringVar() # 设置变量
l = tk.Label(win, textvariable=var1, bg='green', width=20, height=2)
l.pack()

# 创建一个方法用于按钮的点击事件
def print_selection():
    # 获取当前选中的文本
    value = lb.get(lb.curselection())
    # 为label设置值
    var1.set(value)

# 创建一个按钮
b = tk.Button(win, text='print selection', height=2, bg='red', command=print_selection)
b.pack()

# 创建变量
var2 = tk.StringVar()
# 为变量设置值
#var2.set((1,2,3,4))
# 创建Listbox
lb = tk.Listbox(win, listvariable=var2)
# 创建一个list并将值循环添加到Listbox控件中
list_items = [11,22,33,44]
for i in list_items:
    # 从最后一个位置开始加入值
    lb.insert('end', i)
lb.insert('1', 'first')
lb.insert('3', 'third')
lb.delete('4')
lb.pack()

var3 = tk.StringVar()
l2 = tk.Label(win, bg='yellow', width=20, text='empty', height=2)
l2.pack()

# 定义显示函数
def select_result():
    l2.config(text='you have select: ' + var3.get()) #  var3.get()就是获取到变量 var3 的值
# 定义一个RadioButton
# variable=var3, value='A'的意思就是，当我们鼠标选中了其中一个选项，把value的值A放到变量var3中，然后赋值给variable
r1 = tk.Radiobutton(win, text='Option A', variable=var3, value='A', highlightcolor='#123', command=select_result)
r1.pack()

r2 = tk.Radiobutton(win, text='Option B', variable=var3, value='B', command=select_result)
r2.pack()

r3 = tk.Radiobutton(win, text='Option C', variable=var3, value='C', command=select_result)
r3.pack()

win.mainloop()
