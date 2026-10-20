from tabulate import tabulate
import mysql.connector
mycon=mysql.connector.connect(host="localhost", user="root", password="sql")
cur=mycon.cursor()
print("Welcome to HelloBangalore! Book your dream stay with us. Enjoy exclusive deals, seamless booking, and unforgettable experiences. Get started today!")
print("Hotels in Bangalore - handpicked for you:","\n","1:Sunset Cove","\n","2:The Grand Horizon","\n","3:The Willow Stay")
def exploring():
 ch=int(input("Which hotel do you want to explore?"))
 if ch==1:
    print("\n","Great choice my friend!!","\n")
    print("Sunset Cove — your budget-friendly escape near the breathtaking Nandi Hills. Enjoy cozy rooms, serene surroundings, and stunning sunset views, all without stretching your wallet. Perfect for travelers seeking comfort, nature, and a peaceful retreat.")
    c=input("Do you want to go further with the booking? Y/N?")
    if c=="Y":
        cur.execute("Use sunset_cove")
        cur.execute("select * from rooms")
        booking()
        n=int(input("Select 1 to ADD, 2 to DELETE, 3 to MODIFY, 4 to SEARCH: "))
        if n==1:
            add()
        elif n==2:
            delete()
        elif n==3:
            modify()
        elif n==4:
            search()
        else:
            print("Enter valid choice")
    else:
        exploring()     

 elif ch==2:
    print("\n","You have a great taste!!","\n")
    print("The Grand Horizon — Bangalore’s premier address for business and luxury. Elegant rooms, top-notch amenities, and attentive service await, all just minutes from the airport. Stay productive, stay comfortable, stay impressive.")
    c=input("Do you want to go further with the booking? Y/N?")
    if c=="Y":
        cur.execute("Use the_grand_horizon")
        cur.execute("select * from rooms")
        booking()
        n=int(input("Select 1 to ADD, 2 to DELETE, 3 to MODIFY, 4 to SEARCH: "))
        if n==1:
            add()
        elif n==2:
            delete()
        elif n==3:
            modify()
        elif n==4:
            search()
        else:
            print("Enter valid choice")    
    else:
        exploring()
        
 elif ch==3:
    print("That's a great pick buddy!!","\n")
    print("The Willow Stay — your cozy retreat near the excitement of Wonderla Waterpark. Perfect for families and thrill-seekers alike, it offers comfortable rooms, peaceful surroundings, and easy access to endless fun and adventure. Make your Bangalore getaway truly memorable!","\n")
    c=input("Do you want to go further with the booking? Y/N?")
    if c=="Y":
       cur.execute("Use the_willow_stay")
       cur.execute("select * from rooms")
       booking() 
       n=int(input("Select 1 to ADD, 2 to DELETE, 3 to MODIFY, 4 to SEARCH: "))
       if n==1:
            add()
       elif n==2:
            delete()
       elif n==3:
            modify()
       elif n==4:
            search()
       else:
            print("Enter valid choice")
    else:
        exploring()
        
def booking():
    R=cur.fetchall()
    L=['Floor',' Room_Range','No_of_rooms','Room_type', 'Price_Range', 'Availabity']
    print(tabulate(R,headers=L,tablefmt="grid"))
    
def add():
    Room_no=int(input("Room No:"))
    Guest_ID=int(input("Guest ID:"))
    Guest_Name=input("Guest Name:")
    Phone_No=int(input("Enter 6 digit phone number"))
    Check_in_date=input("Check in date:")
    Check_out_date=input("Check out date:")
    Room_type=input("Room type:")
    cur.execute('insert into guests values({},{},"{}",{},"{}","{}","{}")'.format(Room_no,Guest_ID,Guest_Name,Phone_No,Check_in_date,Check_out_date,Room_type))
    mycon.commit() 
    bill()
    print("Room booked successfully!!")
    
def delete():
    n=int(input("Enter Guest ID to delete data:"))
    cur.execute('delete from guests where Guest_ID={}'.format(n))
    mycon.commit()
    print("Data deleted successfully")

def modify():
    n=input("Do you want to modify Name, Check_out_date or Room_type:")
    x=input("Enter new value:")
    y=int(input("Enter Guest_ID:"))
    if n=="Name":
        cur.execute('Update guests set Guest_name="{}" where Guest_ID="{}"'.format(x,y))
        mycon.commit()
        print("Name changed successfully!!")
    elif n=="Check_out_date":
        cur.execute('Update guests set Check_out_date="{}" where Guest_ID="{}"'.format(x,y))
        mycon.commit()
        print("Check_out_date changed successfully!!")
    elif n=="Room_type":
        cur.execute('Update guests set Room_type="{}" where Guest_ID="{}"'.format(x,y))
        mycon.commit()
        print("Room_type updated successfully!!")
    else:
        print("Enter valid choice")
        
def search():
    n=input("Enter name to search:")
    cur.execute('select * from guests where Guest_name="{}"'.format(n))
    R=cur.fetchall()
    if len(R)!=0:
        print("Here is the data you requested:")
        print("(Room_no, Guest_ID, Guest_name, Phone_No, Check_in_date, Check_out_date, Room_type)")
        for i in R:
          print(i)
    else:
        print("No data found")
        
def bill():
    cur.execute('select * from guests')
    R=cur.fetchall()
    x=(R[len(R)-1])
    print(x)
    y=x[-1]
    print(y)
    cur.execute('select * from rooms where Room_type="{}"'.format(y))
    R=cur.fetchall()
    print(R)
    z=(R[-1][-2])   
    print("Your total including GST is:",z+(5/100 * z))      
exploring()
 
