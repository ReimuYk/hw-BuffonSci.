from tkinter import *
import math

def clear():
    lambda x=ALL:c.delete(x)

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
    c.create_line(x1,y1,x2,y2,fill='red')
    

def run():
    drawbg()
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
vn.set(10000)
e3=Entry(root,textvariable=vn)
b=Button(root,text='运行',command=run)
l4=Label(root,text='pi=')
vp=DoubleVar()
vp.set(0)
e4=Entry(root,textvariable=vp)
c.grid(row=0,rowspan=6)
l1.grid(row=1,column=1)
e1.grid(row=1,column=2)
l2.grid(row=2,column=1)
e2.grid(row=2,column=2)
l3.grid(row=3,column=1)
e3.grid(row=3,column=2)
b.grid(row=4,column=1,columnspan=2,sticky=W+E)
l4.grid(row=5,column=1)
e4.grid(row=5,column=2)

root.mainloop()
