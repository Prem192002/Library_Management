#Library management system 
#using python and MySQL(DBMS)

    
from tkinter.messagebox import YES


print("WELCOME TO LIBRARYxyz")

y=input("DO YOU WANT ANY ASSISTANCE (yes/no) ? \n")
if y=="no":
    print("THANK YOU")
if y=="yes":
    
    print("HOW CAN I HELP YOU:")
    print("""--> Issue a Book
--> Return a Book
--> Find a Book
--> Whats Trending""")
a="issue a book"
b="return a book"
c="find a book"
e="whats trending"
d=input("YOUR RESPONCE: \n")

if d==a:                          #Issue
    import mysql.connector
    db=mysql.connector.connect(
        host="localhost",
        user="root",
        password="prem@2002"
    )
      
    y=db.cursor()          
    y.execute("use library") 
   
   
        
    name=input("Enter your name\n")
    issuedby=int(input("Enter the registration number:\n"))
    issuedate=float(input("Enter the issue date: \n"))
    bname=input("Enter the book name:\n")                          #input variables                               
    bcode=int(input("Enter the book code:\n"))
    
    
    
    
    sql = "insert into library_data (name,registration_number,issue_date,book_name,book_code) values(%s,%s,%s,%s,%s)"
    t=(name,issuedby,issuedate,bname,bcode)
    y.execute(sql,t)
    db.commit()
    print("Your respoce has been recorded")


if d==b:                           #Return
    import mysql.connector
    db=mysql.connector.connect(
        host="localhost",
        user="root",
        password="prem@2002"
    )
    cur=db.cursor()
    cur.execute("use library")
    n=int(input("Enter the registration number \n"))
    c=float(input("Enter the return date: \n"))
    
    sql="update library_data set return_date=%s where registration_number=%s"
    t=(c,n)
    
    cur.execute(sql,t)
    db.commit()
    print("Thank you for Returning the book")
        

if d==c:                        #find book
    import mysql.connector
    db=mysql.connector.connect(
        host="localhost",
        user="root",
        password="prem@2002"
        
    )
    cur=db.cursor()
    cur.execute("use library")
    X = input("Enter the book name\n")
    Y = int(input("Enter the book code\n"))
    
    sql="SELECT shelf_no FROM books WHERE book_name=%s and book_code=%s"
    t = (X,Y)
    cur.execute(sql,t)
    z=cur.fetchall()
    for x in z:
        print(x)
    


if d==e:                            #prices
    import mysql.connector                  
    db=mysql.connector.connect(
        host="localhost",
        user="root",
        password="prem@2002"
    )
    
    y=db.cursor()          #ML
    y.execute("use library") 
    y.execute("select book_name from library_data")
    z=y.fetchall()
    from scipy import stats  #max repitationyes
    md=stats.mode(z)
    print(md)