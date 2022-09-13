import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="queen30",
    database="python_batch"

)

mycursor=mydb.cursor()
def insert_data(places,days,budget):

 sql="insert into place_names(places,days,budget) values (%s,%s,%s)"

 val=(places,days,budget)

 mycursor.execute(sql,val)
 mydb.commit()
 print("data inserted successfully")
def view_data():
    mycursor.execute("select * from place_names")
    result=mycursor.fetchall()
    for i in result:
        print(i)
user=int(input("enter your number:"))
if user==1:
   place=input("enter your place:")
   days=int(input("enter your days:"))
   budget=int(input("enter your budget:"))
   insert_data(place,days,budget)
elif user==2:
    view_data()   

