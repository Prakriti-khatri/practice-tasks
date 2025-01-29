# import smtplib
# import pandas as pd
# import datetime as dt
# import schedule
# import time
# file_path="D:\dowload\Birthday Tracker - birthday.csv"
# # Load birthday data from CSV
# def load_birthdays(file_path):
#     return pd.read_csv(file_path)

# # Check today's birthdays
# def check_birthdays(birthday_data):
#     today = dt.datetime.now()
#     today_str = today.strftime("%m-%d")  # Format as MM-DD
#     return birthday_data[birthday_data['Birthday'].str.contains(today_str)]

# # Send email
# def send_email(to_email, subject, body):
#     try:
#         sender_email = "prakritikhatri756@gmail.com"
#         sender_password = "pqpo cgwx pbsb rwkr"
#         with smtplib.SMTP("smtp.gmail.com", 587) as server:
#             server.starttls()  
#             server.login(sender_email, sender_password)
#             message = f"Subject: {subject}\n\n{body}"
#             server.sendmail(sender_email, to_email, message)
#             print(f"Email sent to {to_email}")
#     except Exception as e:
#         print(f"Error sending email to {to_email}: {e}")
# def birthday_email_task():
#     try:
#         birthday_data = load_birthdays("birthdays.csv")
#         today_birthdays = check_birthdays(birthday_data)
        
#         if not today_birthdays.empty:
#             for _, row in today_birthdays.iterrows():
#                 name = row['Chesta Nyachhyon']
#                 email = row['cht1r2a3i4n5@gmail.com']
#                 body = f"Hi {name},\n\nWishing you a very Happy Birthday! 🎉🎂 Have a fantastic day!\n\nBest Wishes,\n[prakriti khatri]"
#                 send_email(email, "Happy Birthday!", body)
#         else:
#             print("No birthdays today.")
#     except Exception as e:
#         print(f"Error in task: {e}")
# schedule.every().day.at("08:00").do(birthday_email_task)
# print("Birthday Email Automator is running...")
# while True:
#     schedule.run_pending()
#     time.sleep(60)  

# import sqlite3
# connection=sqlite3.connect("store.db")
# cursor=connection.cursor()
# # Create a table of products
# cursor.execute('''CREATE TABLE IF NOT EXISTS products(
#                id INTEGER Primary Key,
#                name TEXT NOT NULL,
#                price REAL NOT NULL)'''
#                )
# # Insrt data
# cursor.execute("INSERT INTO products(name,price)VALUES(?,?)",("Laptop",999.999))
# connection.commit()

# #Using SQLAlchemy for database interaction 
# from sqlalchemy import create_engine, Column, Integer, String, Float
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker

# Base = declarative_base()

# class Product(Base):
#     __tablename__ = 'products'
#     id = Column(Integer, primary_key=True)
#     name = Column(String, nullable=False)
#     price = Column(Float, nullable=False)

# #Create engine and session
# engine = create_engine('sqlite:///store.db')
# Base.metadata.create_all(engine)
# Session = sessionmaker(bind=engine)
# session = Session()

# #task 1
# import sqlite3
# connection = sqlite3.connect("Book.db")
# cursor = connection.cursor()

# # Corrected CREATE TABLE statement
# cursor.execute('''
# CREATE TABLE IF NOT EXISTS book(
#     id INTEGER PRIMARY KEY,
#     title TEXT NOT NULL,
#     author TEXT NOT NULL,
#     price REAL NOT NULL
# )
# ''')

# # Insert data
# cursor.execute("INSERT INTO book(title, author, price) VALUES (?, ?, ?)", ("Life or Death", "Salina Adhikari", 600.23))
# cursor.execute("INSERT INTO book(title, author, price) VALUES (?, ?, ?)", ("Life on Verge", "APM on Line", 700.23))
# cursor.execute("INSERT INTO book(title, author, price) VALUES (?, ?, ?)", ("Hello from Other side", "lilly", 400))
# connection.commit()

# # Fetch and print data
# cursor.execute("SELECT * FROM book")
# for row in cursor.fetchall():
#     print(row)

# # Close the connection
# connection.close()

# from sqlalchemy import create_engine, Column, Integer, String, Float
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker

# Base = declarative_base()

# class ToDoList(Base):
#     __tablename__ = 'todolist'
#     id = Column(Integer, primary_key=True)
#     description = Column(String, nullable=False)
#     due_date=Column(String,nullable=False)


# engine = create_engine('sqlite:///mytask.db')
# Base.metadata.create_all(engine)
# Session = sessionmaker(bind=engine)
# session = Session()

# new_todolist_1=ToDoList(description="Make  bed",due_date=2)
# new_todolist_2=ToDoList(description="Wash Clothes",due_date=3)
# new_todolist_3=ToDoList(description="Do dishes",due_date=3)


# session.add(new_todolist_1)
# session.add(new_todolist_2)
# session.add(new_todolist_3)
# session.commit()
# session.delete(new_todolist_3)
# session.commit()


# for todolist in session.query(ToDoList):
#     print(todolist.description,todolist.due_date)



    #tasks 2
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
  
Base = declarative_base()

class librarymanager(Base):
    __tablename__='books'
    id = Column(Integer, primary_key=True)
    genre = Column(String, nullable=False)
    author=Column(String,nullable=False)
    rating= Column(Integer, nullable=False)

engine = create_engine('sqlite:///mylibrary.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
   
new_book_1=librarymanager(genre="Classic Fiction",author="F. Scott Fitzgerald",rating=5)
new_book_2=librarymanager(genre="Science Fiction",author=" Frank Herbert",rating=3)
new_book_3=librarymanager(genre=" Self-Help",author=" James Clear",rating=4)

session.add_all([new_book_1,new_book_2,new_book_3])
session.commit()
session.delete(new_book_3)

def search_book(search_author):
    books= session.query(librarymanager).filter(librarymanager.author==search_author).first()
    if books:
        print(f"Book is Found{books.genre} and {books.author}")

    
    else:
        print("Book is not found")
search_author="james clear"
search_book(search_author)
    

 
 #task 3
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
Base = declarative_base()
class student(Base):
    __tablename__='course'
    name = Column(String,nullable=False)
    course=Column(String,nullable=False)

engine = create_engine('sqlite:///student.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

new_course_1=student(student_name="prakriti khatri",course="BIT")
new_course_2=student()