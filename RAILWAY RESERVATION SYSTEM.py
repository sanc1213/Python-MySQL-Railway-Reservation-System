#MODULES USED

import mysql.connector as n
import pickle as pl
import random as r

#MAIN

m=n.connect(host='localhost',database='railway',user='root',passwd='root')

cho=0
while cho==0:
    
    print("")
    print(" \n\t\t\t\tWELCOME TO INDIAN RAILWAYS")
    print(" \n\t\t\t\tBY:- SANCHIT SINGH ")
    print("")
    print("")
    print("1. CREATE TABLE FOR TRAIN DETAILS.")
    print("2. **UPDATE/ADD TRAIN DETAILS.")
    print("3. Delete Train DETAILS.")
    print("4. TRAIN DETAILS. ")
    print("5. RESERVATION OF TICKETS.")
    print("6. CANCELLATION OF TICKETS. ")
    print("7. DISPLAY PNR STATUS.")
    print("8. QUIT.")
    print("")
    print("")
    print("** - RAILWAY USE ......")
    print("##GOVERMENT OF INDIA##")
    print("")
    print("")
    ch=int(input("ENTER YOUR CHOICE : "))
    k=0

#TO CREATE TABLE FOR TRAIN DATA

    if ch==1:
        if m.is_connected()==True:
            s="create table railway(Tno int(6) unique,Tnm varchar(30),AcT1 int(4),AcT2 int(4),AcT3 int(4),SL int(4))"
            c=m.cursor()
            c.execute(s)
            m.commit()
            print("TABLE CREATED")

#TO UPDATE/ADD TRAIN DETAILS

    if ch==2:
        j="sanchit"
        r=input("\n\t\t\t\tENTER THE PASSWORD: ")
        if (j==r):
            a=int(input("Enter TRAIN NUMBER"))
            b=input("Enter TRAIN NAME")
            h=int(input("Enter AC Tier 1 Seats Available"))
            d=int(input("Enter AC Tier 2 Seats Available"))
            e=int(input("Enter AC Tier 3 Seats Available"))
            f=int(input("Enter SLEEPER Seats Available"))
            v="insert into railway values('%s','%s','%s','%s','%s','%s')"%(a,b,h,d,e,f)
            if m.is_connected()==True:
                c=m.cursor()
                c.execute(v)
                m.commit()
                print("TRAIN DATA ADDED")
                k=k+1
            
        elif(j>r):
            print("\n")
            print("WRONG PASSWORD")

    elif ch==3:
        j="sanchit"
        r=input("\n\t\t\t\tENTER THE PASSWORD: ")
        if (j==r):
            abc=int(input("ENTER TRAIN NUMBER TO BE DELETED"))
            v="delete from railway where Tno='%s'"%(abc)
            c=m.cursor()
            c.execute(v)
            m.commit()
            print("RECORDS OF TRAIN NUMBER:-  ",abc,"   IS DELETED.")

#TO DISPLAY ALL TRAIN DETAILS

    elif ch==4:
        abc=input("ENTER BOARDING PLACE  ")
        abcd=input("ENTER DESTINATION   ")
        print("")
        print("")
        v="select Tno,Tnm,AcT1,AcT2,AcT3,SL from railway"
        c=m.cursor()
        c.execute(v)
        v=c.fetchall()
        u=len(v)
        k="select Tno,Tnm,AcT1,AcT2,AcT3,SL from railway"
        c.execute(k)
        for i in range(0,u):
            k=c.fetchone()
            print("TRAIN NUMBER",k[0])
            print("TRAIN NAME",k[1])
            print("AC TIER 1 SEATS AVAILABLE",k[2])
            print("AC TIER 2 SEATS AVAILABLE",k[3])
            print("AC TIER 3 SEATS AVAILABLE",k[4])
            print("SLEEPER SEATS AVAILABLE",k[5])
            print("")
            print("")

#TICKETS BOOKING SYSTEM

    elif ch==5:
        print("\n\t\t\t\tWELCOME TO TICKET BOOKING SYSTEM")
        print("\n\t\t\t\t\t\t\t\tBY: SANCHIT SINGH")
        print("")
        print("")
        cd=int(input("ENTER TRAIN NUMBER"))
        print("")
        print("1. AC TIER 1.")
        print("2. AC TIER 2.")
        print("3. AC TIER 3.")
        print("4. SLEEPER CLASS.")
        print("")
        print("")
        al=int(input("ENTER YOUR CHOICE FOR RESERVATION"))
        if al==1:
            v="select Tno,Tnm,AcT1,AcT2,AcT3,SL from railway"
            k="select Tno,Tnm,AcT1,AcT2,AcT3,SL from railway"

            ab=int(input("ENTER HOW MANY SEATS YOU WANT TO RESERVE"))
            lmm="update railway set act1=act1-'%s' where Tno='%s'"%(ab,cd)
            
            c=m.cursor()
            c.execute(v)
            v=c.fetchall()
            u=len(v)
            c.execute(k)
            for i in range(0,u):
                k=c.fetchone()
                p=k[2]
                if ab<=p:
                    ml=n.connect(host='localhost',database='railway',user='root',passwd='root')
                    cc=ml.cursor()
                    cc.execute(lmm)
                    ml.commit()
                    
                    fare=0
                    fare=fare+(ab*1563)

                    ll=[]
                    vd=r.randrange(1000,10000)
                    vdr=vd
                
                    fd=open("tickets.dat","wb")
                    a=input("ENTER YOUR NAME")
                    b=int(input("ENTER YOUR AGE"))
                    c=input("ENTER YOUR DESTINATION")
                    d=input("ENTER YOUR BOARDING PLACE")
                    ll.append(a)
                    ll.append(b)
                    ll.append(c)
                    ll.append(d)
                    pl.dump(ll,fd)
                    fd.close()
                    print("TOTAL AMOUNT TO BE PAID:- ",fare)
                    print("")
                    print("TICKET CONFIRMED")
                    print("")
                    print("YOUR PNR NUMBER IS:- ",vd)
                    ve='CONFIRMED'
                    break

                else:
                    print("TICKET FAILED")
                    print("NO SEATS AVAILABLE")
                    break

        if al==2:
            v="select Tno,Tnm,AcT1,AcT2,AcT3,SL from railway"
            k="select Tno,Tnm,AcT1,AcT2,AcT3,SL from railway"
            
            ab=int(input("ENTER HOW MANY SEATS YOU WANT TO RESERVE"))
            lmm="update railway set act2=act2-'%s' where Tno='%s'"%(ab,cd)
            
            c=m.cursor()
            c.execute(v)
            v=c.fetchall()
            u=len(v)
            c.execute(k)
            for i in range(0,u):
                k=c.fetchone()
                p=k[3]
                if ab<=p:
                    ml=n.connect(host='localhost',database='railway',user='root',passwd='root')
                    cc=ml.cursor()
                    cc.execute(lmm)
                    ml.commit()
                    
                    fare=0
                    fare=fare+(ab*958)

                    ll=[]
                    vd=r.randrange(1000,10000)
                    vdr=vd
                
                    fd=open("tickets.dat","wb")
                    a=input("ENTER YOUR NAME")
                    b=int(input("ENTER YOUR AGE"))
                    c=input("ENTER YOUR DESTINATION")
                    d=input("ENTER YOUR BOARDING PLACE")
                    ll.append(a)
                    ll.append(b)
                    ll.append(c)
                    ll.append(d)
                    pl.dump(ll,fd)
                
                    print("TOTAL AMOUNT TO BE PAID:- ",fare)
                    print("")
                    print("TICKET CONFIRMED")
                    print("")
                    print("YOUR PNR NUMBER IS:- ",vd)
                    ve='CONFIRMED'
                    break

                else:
                    print("TICKET FAILED")
                    print("NO SEATS AVAILABLE")
                    break

        if al==3:
            v="select Tno,Tnm,AcT1,AcT2,AcT3,SL from railway"
            k="select Tno,Tnm,AcT1,AcT2,AcT3,SL from railway"
            
            ab=int(input("ENTER HOW MANY SEATS YOU WANT TO RESERVE"))
            lmm="update railway set act3=act3-'%s' where Tno='%s'"%(ab,cd)
            
            c=m.cursor()
            c.execute(v)
            v=c.fetchall()
            u=len(v)
            c.execute(k)
            for i in range(0,u):
                k=c.fetchone()
                p=k[4]
                if ab<=p:
                    ml=n.connect(host='localhost',database='railway',user='root',passwd='root')
                    cc=ml.cursor()
                    cc.execute(lmm)
                    ml.commit()
                    
                    fare=0
                    fare=fare+(ab*563)

                    ll=[]
                    vd=r.randrange(1000,10000)
                    vdr=vd
                
                    fd=open("tickets.dat","wb")
                    a=input("ENTER YOUR NAME")
                    b=int(input("ENTER YOUR AGE"))
                    c=input("ENTER YOUR DESTINATION")
                    d=input("ENTER YOUR BOARDING PLACE")
                    ll.append(a)
                    ll.append(b)
                    ll.append(c)
                    ll.append(d)
                    pl.dump(ll,fd)
                
                    print("TOTAL AMOUNT TO BE PAID:- ",fare)
                    print("")
                    print("TICKET CONFIRMED")
                    print("")
                    print("YOUR PNR NUMBER IS:- ",vd)
                    ve='CONFIRMED'
                    break

                else:
                    print("TICKET FAILED")
                    print("NO SEATS AVAILABLE")
                    break

        if al==4:
            v="select Tno,Tnm,AcT1,AcT2,AcT3,SL from railway"
            k="select Tno,Tnm,AcT1,AcT2,AcT3,SL from railway"
            
            ab=int(input("ENTER HOW MANY SEATS YOU WANT TO RESERVE"))
            lmm="update railway set sl=sl-'%s' where Tno='%s'"%(ab,cd)
            
            c=m.cursor()
            c.execute(v)
            v=c.fetchall()
            u=len(v)
            c.execute(k)
            for i in range(0,u):
                k=c.fetchone()
                p=k[5]
                if ab<=p:
                    ml=n.connect(host='localhost',database='railway',user='root',passwd='root')
                    cc=ml.cursor()
                    cc.execute(lmm)
                    ml.commit()
                    
                    fare=0
                    fare=fare+(ab*273)

                    ll=[]
                    vd=r.randrange(1000,10000)
                    vdr=vd
                
                    fd=open("tickets.dat","wb")
                    a=input("ENTER YOUR NAME")
                    b=int(input("ENTER YOUR AGE"))
                    c=input("ENTER YOUR DESTINATION")
                    d=input("ENTER YOUR BOARDING PLACE")
                    ll.append(a)
                    ll.append(b)
                    ll.append(c)
                    ll.append(d)
                    pl.dump(ll,fd)
                
                    print("TOTAL AMOUNT TO BE PAID:- ",fare)
                    print("")
                    print("TICKET CONFIRMED")
                    print("")
                    print("YOUR PNR NUMBER IS:- ",vd)
                    ve='CONFIRMED'
                    break
            
                else:
                    print("TICKET FAILED")
                    print("NO SEATS AVAILABLE")
                    break

#TICKETS CANCELLING SYSTEM

    elif ch==6:
        print("\n\t\t\t\tWELCOME TO TICKET CANCELLING SYSTEM")
        print("\n\t\t\t\t\t\t\t\tBY: SANCHIT SINGH")
        print("")
        print("")
        e=int(input("ENTER YOUR PNR NUMBER"))
        if e==vdr:
            fd=open("tickets.dat",'ab')
            rec=[]
            pl.dump(rec,fd)
            print("TICKET CANCELLED")
            ve='CANCELLED'
            print("")
            print("YOUR AMOUNT WILL BE REFUNDED WITHIN 15 DAYS IN YOUR BANK ACCOUNT")

        else:
            print("WRONG PNR NUMBER")

#TICKET VERIFYING SYSTEM

    elif ch==7:
        v="select Tnm from railway where tno='%s'"%cd
        mm=n.connect(host='localhost',database='railway',user='root',passwd='root')
        c=mm.cursor()
        c.execute(v)
        vm=c.fetchall()
        for i in vm:
            for j in i:
                vmd=j
        print("\n\t\t\t\tWELCOME TO TICKET VERIFYING SYSTEM")
        print("\n\t\t\t\t\t\t\t\tBY: SANCHIT SINGH")
        print("")
        print("")
        e=int(input("ENTER PNR NUMBER"))
        if e==vdr:
            fd=open("tickets.dat",'rb')
            stp=pl.load(fd)
            print("")
            print("")
            print("NAME :-  ",stp[0])
            print("AGE :-  ",stp[1])
            print("DESTINATION :-  ",stp[2])
            print("BOARDING :-  ",stp[3])
            print("TRAIN NAME:- ",vmd)
            print("TICKET STATUS:- ",ve)
            print("")

#EXIT/QUIT

    elif ch==8:
        print("\n\t\t\tTHANK YOU FOR VISITING INDIAN RAILWAYS")
        print("\n\t\t\tA project created by SANCHIT SINGH")
        cho=cho+1


            
