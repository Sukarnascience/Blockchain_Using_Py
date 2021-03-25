import mysql.connector as sql
from tkinter import *
from tkinter import messagebox
import hashlib
import csv

def block(transaction):
    sender = transaction[0]
    recever = transaction[1]
    ammount = transaction[2]
    previous_hash = transaction[3]
    new_hash_data = "{},{},{},{}".format(sender,recever,ammount,previous_hash)
    assign_new_hash = hashlib.sha256(new_hash_data.encode()).hexdigest()
    return assign_new_hash

def login():
    username = UN.get()
    password = PW.get()
    database=sql.connect(host="localhost",passwd="1234",user="root",database="school")
    cc=database.cursor()
    cc.execute("select * from account where username='{}';".format(username))
    data = cc.fetchall()
    if(data[0][1]==password):
        screen.destroy()

        def ledger():
            database=sql.connect(host="localhost",passwd="1234",user="root",database="school")
            cc=database.cursor()
            cc.execute("select * from ledger;")
            data = cc.fetchall()

            printoutintxt = open("Myledger.csv",'a')
            mytyper = csv.writer(printoutintxt)
            for i in data:
                mytyper.writerow(list(i))

            printoutintxt.close()
            messagebox.showinfo("Thank You","Print Out has beed dun successfully \nnamed \"Myledger.csv\" in home Page ")

        def add_block():
            global newhashdata
            database=sql.connect(host="localhost",passwd="1234",user="root",database="school")
            cc=database.cursor()
            cc.execute("select * from ledger;")
            data = cc.fetchall()
            lastData = data[-1]
            PH = lastData[-1]
            newhashdata = block([SN.get(),RN.get(),AM.get(),PH])
            cc.execute("INSERT INTO ledger values('{}','{}',{},'{}');".format(SN.get(),RN.get(),AM.get(),newhashdata))
            database.commit()
            database.close()
            messagebox.showinfo("Great","Your block has added successfully")

        mainscreen = Tk()
        mainscreen.title("Block Chain - S.jana")
        mainscreen.geometry("480x250")

        l1=Label(mainscreen,text="Add your Block in Block Chain",font=("Courier",20))
        l1.pack()
        l2=Label(mainscreen,text="-----------------------------",font=("Courier",20))
        l2.pack()

        l3=Label(mainscreen,text="Sender :",font=("Courier",15))
        l3.place(x=20,y=80)
        l4=Label(mainscreen,text="Recever :",font=("Courier",15))
        l4.place(x=20,y=120)
        l6=Label(mainscreen,text="Ammount :",font=("Courier",15))
        l6.place(x=20,y=160)
        b2=Button(mainscreen,text="See Ledger",command=ledger)
        b2.place(x=240+30,y=200)
        b3=Button(mainscreen,text="Add the Block in chain",command=add_block)
        b3.place(x=100+30,y=200)

        SN=StringVar()
        RN=StringVar()
        AM=IntVar()

        u1=Entry(mainscreen,textvariable=SN)
        u1.place(x=220,y=80)
        u2=Entry(mainscreen,textvariable=RN)
        u2.place(x=220,y=120)
        u4=Entry(mainscreen,textvariable=AM)
        u4.place(x=220,y=160)

        mainscreen.mainloop()

    else:
        messagebox.showwarning("Not Alloud","Please check your Details\nBecause the data is not matching with out database")

def signup():
    username = NUN.get()
    password = NPW.get()
    passwordV = VPW.get()
    if(password==passwordV):
        database=sql.connect(host="localhost",passwd="1234",user="root",database="school")
        cc=database.cursor()
        cc.execute("INSERT INTO account values ('{}','{}');".format(username,password))
        database.commit()
        database.close()
        messagebox.showinfo("Alloud","Your Account has created successfully :)")
    else:
        messagebox.showerror("Not Alloud","Please check your password and re-password\nthey both are not same")

screen = Tk()
screen.title("Entry Gate")
screen.geometry("600x240")
l1=Label(screen,text="Login            Signup", font=("Courier",20))
l1.pack()
l2=Label(screen,text="|\n|\n|\n|\n|\n|", font=("Courier",20))
l2.pack()

l3=Label(screen,text="UserName :",font=("Courier",15))
l3.place(x=20,y=60)
l4=Label(screen,text="Password :",font=("Courier",15))
l4.place(x=20,y=100)
l6=Label(screen,text="UserName :",font=("Courier",15))
l6.place(x=320,y=60)
l7=Label(screen,text="Password :",font=("Courier",15))
l7.place(x=320,y=100)
l8=Label(screen,text="Re-Password:",font=("Courier",15))
l8.place(x=320,y=140)

b1=Button(screen,text="Login",command=login)
b1.place(x=130,y=200)
b3=Button(screen,text="Signup",command=signup)
b3.place(x=415,y=200)

UN=StringVar()
PW=StringVar()
NUN=StringVar()
NPW=StringVar()
VPW=StringVar()
u1=Entry(screen,textvariable=UN)
u1.place(x=150,y=65)
u2=Entry(screen,textvariable=PW)
u2.place(x=150,y=105)
u4=Entry(screen,textvariable=NUN)
u4.place(x=465,y=65)
u5=Entry(screen,textvariable=NPW)
u5.place(x=465,y=105)
u6=Entry(screen,textvariable=VPW)
u6.place(x=465,y=145)

screen.mainloop()
