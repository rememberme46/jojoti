import mysql.connector
mycon=mysql.connector.connect(host="localhost",user="root",passwd="nps@123",database="jvl")
if mycon.is_connected()==True:
        print("Successfully connected.")
        mycursor=mycon.cursor()
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        
        print("|~                         RAILWAY MANAGEMENT.               ~| ")
        
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
def addreco():
    if mycon.is_connected==False:
        print("Connection Error!")
    else:
        print("~~~~~~~~~~~~~~~~~~~~~~~")
        tno=int(input("Enter the Train number-:"))
        tname=input("Enter the Train name-:")
        S_station=input("Enter the name of the Starting station-:")
        T_station=input("Enter the name of the Target station:")
        T_type=input("Enter the Type of train:")
        D_cover=int(input("Enter the Total distance to be covered:"))
        T_d_w=str(input("Enter the Active days:"))
        A_time=str(input("Enter the Arrival time of the train:"))
        D_time=str(input("Enter the Departure time of the train:"))
        Halt_time=str(input("Enter the Halt time of the train:"))
        query="insert into m_train values({},'{}','{}','{}','{}',{},'{}','{}','{}','{}')".format(tno,tname,S_station,T_station,T_type,D_cover,T_d_w,A_time,D_time,Halt_time)
        mycursor.execute(query)
        mycon.commit()
        print("\n ## 𝑅𝐸𝒞𝒪𝑅𝒟 𝒜𝒟𝒟𝐸𝒟 𝒮𝒰𝒞𝒞𝐸𝒮𝒮𝐹𝒰𝐿𝐿𝒴!")


def dispreco():
         mycon=mysql.connector.connect(host="localhost",user="root",passwd="nps@123",database="jvl")
         if mycon.is_connected()==False:
                print("Connection Error!")
         else:
                mycursor=mycon.cursor()
                query=("select * from m_train")
                mycursor.execute(query)
                mydata=mycursor.fetchall()
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print('%10s'%"TrainNumber",'%10s'%"TrainName",'%10s'%"StartingStation",'%10s'%"TargetStation",'%10s'%"TrainType"'%10s'%"DistanceCovered",'%10s'%"ActiveDays",'%10s'%"ArrivalTime",'%10s'%"DepartureTime",'%10s'%"HaltTime")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
               

                count=mycursor.rowcount
                for row in mydata:
                    print('%5s' % row[0],'%16s'%row[1],'%16s'%row[2],'%16s'%row[3],'%16s' % row[4],'%16s'%row[5],'%16s'%row[6],'%16s'%row[7],'%16s'%row[8],'%16s'%row[9])

def dispreco2():
         mycon=mysql.connector.connect(host="localhost",user="root",passwd="nps@123",database="jvl")
         if mycon.is_connected()==False:
                print("Connection Error!")
         else:
                mycursor=mycon.cursor()
                query=("select * from m_train")
                mycursor.execute(query)
                mydata=mycursor.fetchall()
                header=["Train Number","Train Name","Starting Station","Target Station","Train Type","Distance Covered","Active Days","Arrival Time","Departure Time","HaltTime"]
                tab=[]
                for rec in mydata:
                        tab.append(rec)
                print(tabulate(tab,header,tablefmt="github",numalign="right"))

def modifyreco():
        mycon=mysql.connector.connect(host="localhost",user="root",passwd="nps@123",database="jvl")
        if mycon.is_connected()==False:
                print("Connection Error!")
        else:
                mycursor=mycon.cursor()
                tno=int(input("Enter the train number for searching:"))
                query="select * from m_train where tno="+str(tno)
                mycursor.execute(query)
                mydata=mycursor.fetchone()
                if mydata!=None:
                        print(mydata)
                        a=input("Enter the new trainname:")
                        b=int(input("Enter the new train number:"))
                        c=input("Enter the new starting station:")
                        d=input("Enter the new destination station:")
                        e=input("Enter the type of train to be modified into:")
                        f=int(input("Enter the new distance to be covered:"))
                        g=input("Enter the new active days:")
                        h=str(input("Enter the new arrival time:"))
                        i=str(input("Enter the new departure time:"))
                        j=str(input("Enter the new halt time:"))
                        query=("update m_train set Tname='{}',Tno={},S_station='{}',T_station='{}',T_type='{}',D_cover={},T_d_w='{}',Arrival_time='{}',Departure_time='{}',Halt_time='{}' where Tno={}").format(a,b,c,d,e,f,g,h,i,j,tno)
                        mycursor.execute(query)
                        mycon.commit()
                        print("Record modified")
                else:
                        print("Record not found")

def delreco():
        mycon=mysql.connector.connect(host="localhost",user="root",passwd="nps@123",database="jvl")
        if mycon.is_connected==False:
                print("Connection Error!")
        else:
                print("*******************DELETE TRAIN NUMBER **************************")
                mycursor=mycon.cursor()
                cno=int(input("Enter the train number for deleting:"))
                query="select * from m_train where Tno="+str(cno)
                mycursor.execute(query)
                mydata=mycursor.fetchone()
                if mydata!=None:
                        print(mydata)
                        ans=input("Do you want to delete? (Press Y if you want to delete else press N)")
                        if ans=='Y' or ans=='y':
                                query="Delete from m_train where Tno="+str(cno)
                                mycursor.execute(query)
                                mycon.commit()
                                print("Record has been deleted successfully.")
                        else:
                                print("Record not deleted.")
                else:
                        print("Record not found")
def searchreco():
         mycon=mysql.connector.connect(host="localhost",user="root",passwd="nps@123",database="jvl")
         if mycon.is_connected()==False:
                print("Error in connection")
         else:
                 
                 mycursor=mycon.cursor()
                 print("~~~~~~~~~~~~SEARCH TRAIN NAME/TRAIN NUMBER~~~~~~~~~~~~ ")
                 print(" Enter train number to get the train details attached to it")
                 tno=int(input("Enter the train number for searching:"))
                 print("The train details attached with the train number you have searched for is:")
                 query="select * from m_train where tno="+str(tno)
                 mycursor.execute(query)
                 mydata=mycursor.fetchone()
                 count=mycursor.rowcount
                 if mydata!=None:
                        print(mydata)

while True:
        print("~~~~~~~~~~~~~~~")
        print("             Menu")
        print("~~~~~~~~~~~~~~~")
        print("1. Data to be added:")
        print("2.Data to be modified:")
        print("3. Data to be deleted:")
        print("4. Data to searched:")
        print("5. Data to be displayed:")
        print("0. Unavailable Data")
        ch=int(input("Enter your choice:"))
        if ch==1:
                addreco()
        if ch==2:
                modifyreco()
        if ch==3:
                delreco()
        if ch==4:
                searchreco()
        if ch==5:
                dispreco()
        elif ch==0:
                print("Thankyou!!")
               
                break     
