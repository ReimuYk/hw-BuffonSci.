from tkinter import *
import math
import random

def clear():
    global c
    c=Canvas(root,height=500,width=500,bg='white')
    c.grid(row=0,rowspan=7)

def drawbg():
    for i in range(11):
        c.create_line(0,50*i,500,50*i,fill='gray')
    return

def pin(px,py,th):
    l=50*vl.get()/vd.get()
    x1=px-l*math.sin(th)/2
    x2=px+l*math.sin(th)/2
    y1=py-l*math.cos(th)/2
    y2=py+l*math.cos(th)/2
    x1=int(x1)
    x2=int(x2)
    y1=int(y1)
    y2=int(y2)
    c.create_line(x1,y1,x2,y2,fill='red')
    if int(y1/50)!= int(y2/50):
        return 1
    else:
        return 0

def check():
    vw.set('')
    if vl.get()>vd.get():
        vw.set('错误：间距d应当小于等于针长l')
        return True
    if vn.get()>2000:
        vw.set('警告：次数n过大可能导致图效果较差')
    if vn.get()>20000:
        vw.set('错误：次数n过大将导致绘图缓慢')
        return True
    

def pi(count):
    vp.set(2*vl.get()*vn.get()/(vd.get()*count))
    vh.set(count)

def run():
    clear()
    drawbg()
    if check():
        return
    count=0
    for i in range(vn.get()):
        px=random.random()*500
        py=random.random()*500
        th=random.random()*math.pi
        count+=pin(px,py,th)
    print(count)
    pi(count)
    print("runrunrun")
    return

root=Tk()
root.title('ButtonRandomSci')
c=Canvas(root,height=500,width=500,bg='white')
l1=Label(root,text='针长l:')
vl=IntVar()
vl.set(5)
e1=Entry(root,textvariable=vl)
l2=Label(root,text='间距d:')
vd=IntVar()
vd.set(5)
e2=Entry(root,textvariable=vd)
l3=Label(root,text='次数n:')
vn=IntVar()
vn.set(500)
e3=Entry(root,textvariable=vn)
b=Button(root,text='运行',command=run)
l5=Label(root,text='覆盖次数:')
vh=IntVar()
e5=Entry(root,textvariable=vh)
l4=Label(root,text='pi=')
vp=DoubleVar()
vp.set(0)
e4=Entry(root,textvariable=vp)
c.grid(row=0,rowspan=7)
l1.grid(row=1,column=1)
e1.grid(row=1,column=2)
l2.grid(row=2,column=1)
e2.grid(row=2,column=2)
l3.grid(row=3,column=1)
e3.grid(row=3,column=2)
b.grid(row=4,column=1,columnspan=2,sticky=W+E)
l5.grid(row=5,column=1)
e5.grid(row=5,column=2)
l4.grid(row=6,column=1)
e4.grid(row=6,column=2)
vw=StringVar()
##vw.set('warning')
l0=Label(root,textvariable=vw,width=30,font=("黑体",10,"bold"))
l0.grid(row=0,column=1,columnspan=2)

root.mainloop()
