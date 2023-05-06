from tkinter import*
from tkinter import messagebox
import time
m=Tk(className=' BILL MANAGEMENT SYSTEM')
m.geometry("1200x500")

a=StringVar()
b=StringVar()
c=StringVar()
d=StringVar()
e=StringVar()
f=StringVar()
g=StringVar()
h=StringVar()
i=StringVar()
j=StringVar()
k=StringVar()
l=StringVar()
n=StringVar()
o=StringVar()
p=StringVar()
q=StringVar()
r=StringVar()
s=StringVar()
x=StringVar()
y=StringVar()
z=StringVar()

def sum():
    m1=int(e1.get())
    m2 = int(e2.get())
    m3 = int(e3.get())
    m4 = int(e4.get())
    m5 =int(e5.get())
    m6 = int(e6.get())
    m7 = int(e7.get())
    m8 = int(e8.get())
    m9 = int(ee1.get())
    m10 = int(ee2.get())
    m11 = int(ee3.get())
    m12 = int(ee4.get())
    m13 = int(ee5.get())
    m14 = int(ee6.get())
    m15 = int(ee7.get())
    m16 = int(ee8.get())
    sum= (m1*80)+(m2*350)+(m3*120)+(m4*425)+(m5*850)+(m6*250)+(m7*30)+(m8*450)+(m9*850)+(m10*400)+(m11*250)+(m12*220)+(m13*120)+(m14*90)+(m15*300)+(m16*100)
    lbb1.config(text=sum)
    st = 0.13                 #sales Tax
    se = sum* 0.05            #Service charges
    sub= (st* sum) + sum      #subtotal
    tt=sub+ se                #total cost
    x.set(sum)
    y.set(se)
    z.set(st)
    a.set(sub)
    b.set(tt)
    c.set(m1*80)
    d.set(m2*350)
    e.set(m3*120)
    f.set(m4*425)
    g.set(m5*850)
    h.set(m6*250)
    i.set(m7*30)
    j.set(m8*450)
    k.set(m9*850)
    l.set(m10*400)
    s.set(m11*250)
    n.set(m12*220)
    o.set(m13*120)
    p.set(m14*90)
    q.set(m15 * 300)
    r.set(m16 * 100)

def exit():
    exit = messagebox.askyesno("BILL MANAGEMENT SYSTEM", "Do you want to exit?")
    if exit ==1 :     # yes==1 and no==0
        m.destroy()
        return

DateofOrder = StringVar()
DateofOrder.set(time.strftime("%d/%m/%y"))

def reset():
    t1.delete("1.0",END)                        #receipt area reset
    lbb1.config(text=0)                         #total button label reset
    ecs.delete(first=0, last=222)               #customer name reset
    x.set(0)                                    #total cost of foods
    y.set(0)                                    #service charges
    a.set(0)                                    #subtotal
    b.set(0)                                    #total cost
    e1.delete(first=0,last=222)                 #entry 1 ....
    e1.insert(0,"0")
    e2.delete(first=0,last=222)
    e2.insert(0,"0")
    e3.delete(first=0, last=222)
    e3.insert(0, "0")
    e4.delete(first=0, last=222)
    e4.insert(0, "0")
    e5.delete(first=0, last=222)
    e5.insert(0, "0")
    e6.delete(first=0, last=222)
    e6.insert(0, "0")
    e7.delete(first=0, last=222)
    e7.insert(0, "0")
    e8.delete(first=0, last=222)
    e8.insert(0, "0")
    ee1.delete(first=0, last=222)
    ee1.insert(0, "0")
    ee2.delete(first=0, last=222)
    ee2.insert(0, "0")
    ee3.delete(first=0, last=222)
    ee3.insert(0, "0")
    ee4.delete(first=0, last=222)
    ee4.insert(0, "0")
    ee5.delete(first=0, last=222)
    ee5.insert(0, "0")
    ee6.delete(first=0, last=222)
    ee6.insert(0, "0")
    ee7.delete(first=0, last=222)
    ee7.insert(0, "0")
    ee8.delete(first=0, last=222)
    ee8.insert(0, "0")

def gen():
    t1.delete("1.0", END)
    t1.insert(END, '\t\t" WELCOME TO CALZONE " ' + '\n')
    t1.insert(END, ' Receipt Ref:\t\t\t\t\t'  , '\t\t\t\t ' , DateofOrder.get() + '\n')
    t1.insert(END, ' Customer Name:\t\t\t\t', '\t\t ', ecs.get() +'\n')
    t1.insert(END, " ====================================================  " + "\n")
    t1.insert(END, ' Items:'+ '\t\t'+ " Qty" '\t' + "          Cost of Item  " "\t\t" + "          total cost"+ "\n")
    t1.insert(END, " ====================================================  "+"\n" )
    if int(e1.get())>0:
        t1.insert(END, ' Peri Bites: \t\t' + e1.get() + '\t\t' + "80/-" +'\t\t'+ c.get() +"/-" + '\n')
    if int(e2.get())>0:
        t1.insert(END, ' Soup: \t\t' + e2.get() + '\t\t' + "350/-"+'\t\t'+ d.get() +"/-" + '\n')
    if int(e3.get())>0:
        t1.insert(END, ' Cracker: \t\t' + e3.get() + '\t\t' + "120/-"+'\t\t'+ e.get() +"/-" + '\n')
    if int(e4.get())>0:
        t1.insert(END, ' Sandwich: \t\t' + e4.get() + '\t\t' + "425/-"+'\t\t'+ f.get() +"/-" + '\n')
    if int(e5.get())>0:
        t1.insert(END, ' Steak:\t\t' + e5.get() + '\t\t' + "850/-"+'\t\t'+ g.get() +"/-" + '\n')
    if int(e6.get())>0:
        t1.insert(END, ' Wings:\t\t' + e6.get() + '\t\t' + "250/-" +'\t\t'+ h.get() +"/-"+ '\n')
    if int(e7.get())>0:
        t1.insert(END, ' Wonton:\t\t' + e7.get() + '\t\t' + "30/-"+'\t\t'+ i.get() +"/-" + '\n')
    if int(e8.get())>0:
        t1.insert(END, ' Lasagna:\t\t' + e8.get() + '\t\t' + "450/-"+'\t\t'+ j.get() +"/-" + '\n')
    if    int(ee1.get()) > 0:
        t1.insert(END, ' Pizza:\t\t' + ee1.get() + '\t\t' + "850/-" +'\t\t'+ k.get() +"/-"+ '\n')
    if int(ee2.get()) > 0:
        t1.insert(END, ' Pasta:\t\t' + ee2.get() + '\t\t' + "400/-" +'\t\t'+ l.get() +"/-" + '\n')
    if int(ee3.get()) > 0:
        t1.insert(END, ' Tacos:\t\t' + ee3.get() + '\t\t' + "250/-" +'\t\t'+ s.get() +"/-" + '\n')
    if int(ee4.get()) > 0:
        t1.insert(END, ' Fries:\t\t' + ee4.get() + '\t\t' + "220/-" +'\t\t'+ n.get() +"/-" + '\n')
    if int(ee5.get()) > 0:
        t1.insert(END, ' Sundae:\t\t' + ee5.get() + '\t\t' + "120/-" +'\t\t'+ o.get() +"/-" + '\n')
    if int(ee6.get()) > 0:
        t1.insert(END, ' Drink:\t\t' + ee6.get() + '\t\t' + "90/-" +'\t\t'+ p.get() +"/-" + '\n')
    if int(ee7.get()) > 0:
        t1.insert(END, ' Mocktail:\t\t' + ee7.get() + '\t\t' + "300/-" +'\t\t'+ q.get() +"/-" + '\n')
    if int(ee8.get()) > 0:
        t1.insert(END, ' Water:\t\t' + ee8.get() + '\t\t' + "100/-" +'\t\t'+ r.get() +"/-" + '\n')
    t1.insert(END, " ====================================================  " +"\n" )
    t1.insert(END,'Total Cost of Foods:\t\t\t\t\t' + x.get()+"/-"  +  "\n")
    t1.insert(END, 'Sales Tax (13%):\t\t\t\t\t' + z.get() + "/-"+ '\nSubTotal:\t\t\t\t\t' + a.get()+"/-" + '\n')
    t1.insert(END, 'Service Charge (5%):\t\t\t\t\t' + y.get()+"/-"  + '\nTotal Cost:\t\t\t\t\t' + b.get()+"/-" +  "\n")

#saving data in file
file=open(r"C:\Users\SAAD COMMUNICATION\Documents\m.txt","w") 
file.write(  '\t\t" WELCOME TO CALZONE " ' + '\n')
file.write( ' Receipt Ref:\t\t\t\t\t'+ '\t\t ' + DateofOrder.get() + '\n')
file.write( ' Customer Name:\t\t\t\t' + ecs.get() + '\n')
file.write( " =======================================================================  " + "\n")
file.write( ' Items:' + '\t\t' + " Qty" '\t' + "            Cost of Item  " "\t\t" + " total cost" + "\n")
file.write( " =======================================================================  " + "\n")
if int(e1.get()) > 0:
    file.write( ' Peri Bites: \t\t' + e1.get() + '\t\t' + "80/-" + '\t\t' + c.get() + "/-" + '\n')
if int(e2.get()) > 0:
    file.write( ' Soup: \t\t' + e2.get() + '\t\t' + "350/-" + '\t\t' + d.get() + "/-" + '\n')
if int(e3.get()) > 0:
    file.write( ' Cracker: \t\t' + e3.get() + '\t\t' + "120/-" + '\t\t' + e.get() + "/-" + '\n')
if int(e4.get()) > 0:
    file.write( ' Sandwich: \t\t' + e4.get() + '\t\t' + "425/-" + '\t\t' + f.get() + "/-" + '\n')
if int(e5.get()) > 0:
    file.write( ' Steak:\t\t' + e5.get() + '\t\t' + "850/-" + '\t\t' + g.get() + "/-" + '\n')
if int(e6.get()) > 0:
    file.write( ' Wings:\t\t' + e6.get() + '\t\t' + "250/-" + '\t\t' + h.get() + "/-" + '\n')
if int(e7.get()) > 0:
    file.write( ' Wonton:\t\t' + e7.get() + '\t\t' + "30/-" + '\t\t' + i.get() + "/-" + '\n')
if int(e8.get()) > 0:
    file.write( ' Lasagna:\t\t' + e8.get() + '\t\t' + "450/-" + '\t\t' + j.get() + "/-" + '\n')
if int(ee1.get()) > 0:
    file.write( ' Pizza:\t\t' + ee1.get() + '\t\t' + "850/-" + '\t\t' + k.get() + "/-" + '\n')
if int(ee2.get()) > 0:
    file.write( ' Pasta:\t\t' + ee2.get() + '\t\t' + "400/-" + '\t\t' + l.get() + "/-" + '\n')
if int(ee3.get()) > 0:
    file.write( ' Tacos:\t\t' + ee3.get() + '\t\t' + "250/-" + '\t\t' + s.get() + "/-" + '\n')
if int(ee4.get()) > 0:
    file.write( ' Fries:\t\t' + ee4.get() + '\t\t' + "220/-" + '\t\t' + n.get() + "/-" + '\n')
if int(ee5.get()) > 0:
    file.write( ' Sundae:\t\t' + ee5.get() + '\t\t' + "120/-" + '\t\t' + o.get() + "/-" + '\n')
if int(ee6.get()) > 0:
    file.write( ' Drink:\t\t' + ee6.get() + '\t\t' + "90/-" + '\t\t' + p.get() + "/-" + '\n')
if int(ee7.get()) > 0:
    file.write( ' Mocktail:\t\t' + ee7.get() + '\t\t' + "300/-" + '\t\t' + q.get() + "/-" + '\n')
if int(ee8.get()) > 0:
    file.write( ' Water:\t\t' + ee8.get() + '\t\t' + "100/-" + '\t\t' + r.get() + "/-" + '\n')
file.write( " ========================================================================  " + "\n")
file.write( 'Total Cost of Foods:\t\t\t\t\t' + x.get() + "/-" + "\n")
file.write( 'Sales Tax (13%):\t\t\t\t\t' + z.get() + "/-" + '\nSubTotal:\t\t\t\t\t' + a.get() + "/-" + '\n')
file.write( 'Service Charge (5%):\t\t\t\t\t' + y.get() + "/-" + '\nTotal Cost:\t\t\t\t\t' + b.get() + "/-" + "\n")

file.close()

l1=Label(m, text="'WELCOME  TO  CALZONE'",fg="lavender", bg="firebrick4",bd=10,font=("times",38,"bold") ,relief=RAISED)
l1.pack(side=TOP ,fill=X)

f1=Frame(m,bg="tan1",bd=15, width=410,height=505,relief=GROOVE )
f1.place(x=0,y=80)

lcs=Label(m,text="Customer name:",fg="black",bg="tan1",width=12,bd=5,font=("times" ,15),relief=RAISED)
lcs.place(x=20,y=100)
ecs=Entry(m, width=24,bd=5, bg="white",relief=RAISED, font=('arial',12,'bold'))
ecs.place(x=165,y=100)

lq2=Label(f1,text="QTY",fg="black",bg="tan1",width=6,bd=5,font=('times',14,'bold'))
lq2.place(x=90,y=41)

l2=Label(f1,text="Peri Bites",fg="black",bg="tan1",width=6,bd=5,font=("times",15,"bold"))
l2.place(x=10,y=70)
e1=Entry(f1, width=5,bd=5, bg="white",font=("times",12,"bold"))
e1.place(x=100,y=75)
e1.insert(0,"0")

l3=Label(f1,text="Soup",fg="black",bg="tan1",width=6,bd=5,font=("times",15,"bold"))
l3.place(x=10,y=120)
e2=Entry(f1, width=5,bd=5, bg="white",font=("times",12,"bold"))
e2.place(x=100,y=125)
e2.insert(0,"0")

l4=Label(f1,text="Crackers",fg="black",bg="tan1",width=6,bd=5,font=("times",15,"bold"))
l4.place(x=10,y=170)
e3=Entry(f1, width=5,bd=5, bg="white",font=("times",12,"bold"))
e3.place(x=100,y=175)
e3.insert(0,"0")

l5=Label(f1,text="Sandwich",fg="black",bg="tan1",width=6,bd=5,font=("times",15,"bold"))
l5.place(x=10,y=220)
e4=Entry(f1, width=5,bd=5, bg="white",font=("times",12,"bold"))
e4.place(x=100,y=225)
e4.insert(0,"0")

l6=Label(f1,text="Steak",fg="black",bg="tan1",width=6,bd=5,font=("times",15,"bold"))
l6.place(x=10,y=270)
e5=Entry(f1, width=5,bd=5, bg="white",font=("times",12,"bold"))
e5.place(x=100,y=275)
e5.insert(0,"0")

l7=Label(f1,text="Wings",fg="black",bg="tan1",width=6,bd=5,font=("times",15,"bold"))
l7.place(x=10,y=320)
e6=Entry(f1, width=5,bd=5, bg="white",font=("times",12,"bold"))
e6.place(x=100,y=325)
e6.insert(0,"0")

l8=Label(f1,text="Wontons",fg="black",bg="tan1",width=6,bd=5,font=("times",15,"bold"))
l8.place(x=10,y=370)
e7=Entry(f1, width=5,bd=5, bg="white",font=("times",12,"bold"))
e7.place(x=100,y=375)
e7.insert(0,"0")

l9=Label(f1,text="Lasagna",fg="black",bg="tan1",width=6,bd=5,font=("times",15,"bold"))
l9.place(x=10,y=420)
e8=Entry(f1, width=5,bd=5, bg="white",font=("times",12,"bold"))
e8.place(x=100,y=425)
e8.insert(0,"0")

lq2=Label(f1,text="QTY",fg="black",bg="tan1",width=6,bd=5,font=('times',14,'bold'))
lq2.place(x=280,y=41)

ll2=Label(f1,text="Pizza(R)",fg="black",bg="tan1",width=6,bd=5,font=("times",15,"bold"))
ll2.place(x=190,y=70)
ee1=Entry(f1, width=5,bd=5, bg="white",font=("times",12,"bold"))
ee1.place(x=290,y=75)
ee1.insert(0,"0")

ll3=Label(f1,text="Pasta",fg="black",bg="tan1",width=6,bd=5,font=("times",15,"bold"))
ll3.place(x=190,y=120)
ee2=Entry(f1, width=5,bd=5, bg="white",font=("times",12,"bold"))
ee2.place(x=290,y=125)
ee2.insert(0,"0")

ll4=Label(f1,text="Tacos",fg="black",bg="tan1",width=6,bd=5,font=("times",15,"bold"))
ll4.place(x=190,y=170)
ee3=Entry(f1, width=5,bd=5, bg="white",font=("times",12,"bold"))
ee3.place(x=290,y=175)
ee3.insert(0,"0")

ll5=Label(f1,text="Fries",fg="black",bg="tan1",width=6,bd=5,font=("times",15,"bold"))
ll5.place(x=190,y=220)
ee4=Entry(f1, width=5,bd=5, bg="white",font=("times",12,"bold"))
ee4.place(x=290,y=225)
ee4.insert(0,"0")

ll6=Label(f1,text="Sundae",fg="black",bg="tan1",width=6,bd=5,font=("times",15,"bold"))
ll6.place(x=190,y=270)
ee5=Entry(f1, width=5,bd=5, bg="white",font=("times",12,"bold"))
ee5.place(x=290,y=275)
ee5.insert(0,"0")

ll7=Label(f1,text="Drink",fg="black",bg="tan1",width=6,bd=5,font=("times",15,"bold"))
ll7.place(x=190,y=320)
ee6=Entry(f1, width=5,bd=5, bg="white",font=("times",12,"bold"))
ee6.place(x=290,y=325)
ee6.insert(0,"0")

ll8=Label(f1,text="Mocktail",fg="black",bg="tan1",width=6,bd=5,font=("times",15,"bold"))
ll8.place(x=190,y=370)
ee7=Entry(f1, width=5,bd=5, bg="white",font=("times",12,"bold"))
ee7.place(x=290,y=375)
ee7.insert(0,"0")

ll9=Label(f1,text="Water",fg="black",bg="tan1",width=6,bd=5,font=("times",15,"bold"))
ll9.place(x=190,y=420)
ee8=Entry(f1, width=5,bd=5, bg="white",font=("times",12,"bold"))
ee8.place(x=290,y=425)
ee8.insert(0,"0")

f4=Frame(m,bg="firebrick4",bd=15, width=210,height=120,relief=GROOVE )
f4.place(x=0,y=585)

b1=Button(m,text="Total",bg="white",fg="black",width=15,bd=5,command=sum,font=("times",12,"bold"))
b1.place(x=30,y=610)

lbb1=Label(m,width=15,text=0,bd=4,fg="black", bg="white",font=("times",12,"bold"))
lbb1.place(x=30,y=655)
lbb2=Label(m,width=5,text="/-",bd=4,fg="black", bg="white",font=("times",12,"bold"))
lbb2.place(x=125,y=655)

f5=Frame(m,bg="firebrick4",bd=15, width=200,height=120,relief=GROOVE )
f5.place(x=210,y=585)

b2=Button(m,text="Generate bill",bg="white",fg="black",width=15,bd=5,command=gen,font=("times",12,"bold"))
b2.place(x=235,y=625)


f2=Frame(m,bg="lightgoldenrod",bd=15, width=400,height=505,relief=GROOVE)
f2.place(x=410,y=80)

lm=Label(f2,text="' MENU '",fg="black",bg="lightgoldenrod",width=10,bd=5,font=("times",25,"bold"),relief=RAISED)
lm.place(x=70,y=10)

lf2=Label(f2,text="Peri Bites  80/-",fg="black",bg="lightgoldenrod",width=10,bd=5,font=("times",18))
lf2.place(x=10,y=70)
lf3=Label(f2,text="Soup 350/-",fg="black",bg="lightgoldenrod",width=10,bd=10,font=("times",18))
lf3.place(x=0,y=120)
lf4=Label(f2,text="Crackers  120/-",fg="black",bg="lightgoldenrod",width=10,bd=10,font=("times",18))
lf4.place(x=10,y=170)
lf5=Label(f2,text="Sandwich  425/-",fg="black",bg="lightgoldenrod",width=10,bd=10,font=("times",18))
lf5.place(x=10,y=220)
lf6=Label(f2,text="Steak  850/-",fg="black",bg="lightgoldenrod",width=10,bd=5,font=("times",18))
lf6.place(x=10,y=270)
lf7=Label(f2,text="Wings  250/-",fg="black",bg="lightgoldenrod",width=10,bd=10,font=("times",18))
lf7.place(x=0,y=320)
lf8=Label(f2,text="Wontons 30/-",fg="black",bg="lightgoldenrod",width=10,bd=10,font=("times",18))
lf8.place(x=0,y=370)
lf9=Label(f2,text="Lasagna  450/-",fg="black",bg="lightgoldenrod",width=10,bd=10,font=("times",18))
lf9.place(x=0,y=420)

lf2=Label(f2,text="Pizza(R)  850/-",fg="black",bg="lightgoldenrod",width=10,bd=5,font=("times",18))
lf2.place(x=190,y=70)
lf3=Label(f2,text="Pasta  400/-",fg="black",bg="lightgoldenrod",width=10,bd=10,font=("times",18))
lf3.place(x=190,y=120)
lf4=Label(f2,text="Tacos 250/-",fg="black",bg="lightgoldenrod",width=10,bd=10,font=("times",18))
lf4.place(x=190,y=170)
lf5=Label(f2,text="Fries  220/-",fg="black",bg="lightgoldenrod",width=10,bd=10,font=("times",18))
lf5.place(x=190,y=220)
lf6=Label(f2,text="Sundae  120/-",fg="black",bg="lightgoldenrod",width=10,bd=5,font=("times",18))
lf6.place(x=190,y=270)
lf7=Label(f2,text="Drink  90/-",fg="black",bg="lightgoldenrod",width=10,bd=10,font=("times",18))
lf7.place(x=190,y=320)
lf8=Label(f2,text="Mocktail  300/-",fg="black",bg="lightgoldenrod",width=10,bd=10,font=("times",18))
lf8.place(x=190,y=370)
lf9=Label(f2,text="Water 100/-",fg="black",bg="lightgoldenrod",width=10,bd=10,font=("times",18))
lf9.place(x=190,y=420)

f6=Frame(m,bg="firebrick4",bd=15, width=200,height=120,relief=GROOVE )
f6.place(x=410,y=585)

bf1=Button(f6,text="Exit",bg="white",fg="black",width=15,bd=5,command=exit,font=("times",12,"bold"))
bf1.place(x=10,y=25)

f7=Frame(m,bg="firebrick4",bd=15, width=200,height=120,relief=GROOVE )
f7.place(x=610,y=585)

b3=Button(f7,text="Re-set",bg="white",fg="black",width=15,bd=5,command=reset,font=("times",12,"bold"))
b3.place(x=10,y=25)

f3=Frame(m,bg="orangered4",bd=15, width=557,height=625,relief=GROOVE)
f3.place(x=810,y=80)

lm=Label(f3,text="' BILL MANAGEMENT AREA '",fg="black",bg="salmon2",width=25,bd=5,font=("times",19,"bold"),relief=RAISED)
lm.place(x=70,y=0)

t1=Text(f3,width=53,height=29,bg='white',bd=3,font=('arial',12,'bold'))
t1.place(x=21,y=36)

m.mainloop()

