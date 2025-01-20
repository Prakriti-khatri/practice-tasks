#deque
from collections import deque
from collections import Counter
from collections import defaultdict
task=deque(['go to college','wash cloth','do your task'])
task.append('go to the supermarket')
print(task)
task.remove('go to college')
print(task)
task.rotate(1)
print(task)
paragraphs="""
Python is an amazing programming language. Python is easy to learn and versatile.
Python is widely used for web development, data analysis, artificial intelligence, and more.
"""
word_counts = Counter(paragraphs.split())
print(word_counts)  

top_words = word_counts.most_common(3)

print("Top 3 most common words: ")
for word, count in top_words:
    print(f"{word}: {count}")
inventory = defaultdict(list)
def add_product(category, product):
    inventory[category].append(product)
    print(f"Added '{product}' to category '{category}'.")
def display_inventory():
    print("\nInventory:")
    for category, products in inventory.items():
        print(f"{category}: {', '.join(products)}")
add_product("Electronics", "Smartphone")
add_product("Electronics", "Laptop")
add_product("Groceries", "Apples")
add_product("Groceries", "Bananas")
add_product("Clothing", "T-Shirt")
add_product("Clothing", "Jeans")

display_inventory()

#numpy 
import numpy as np
array=np.array([5,15,10,20])
array_sum=np.sum(array)
array_mean=np.std(array)
array_mul=array*2
print("original array",array)
print("sum of element",array_sum)
print("mean of deviation",array_mean)
print("array after multiplying each element by 2",array_mul)

import numpy as np
array1=np.array([3,4,8]),([5,10,15])
array2=np.array([3,4]),[7,11],([5,10])
result=np.dot(array1,array2)
print("array1")
print(array1)
print("array2")
print(array2)
print("\nmatrix multiplication result")
print(result)

#cvs
import csv
data_path = "employees.csv"

def create_csv():
    headers = ["Name", "Age", "Department",]
    with open(data_path, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(headers)
    print("File has been created.")

def add_data(Name, Age, Department):
    with open(data_path, mode = "a", newline = "") as file:
        writer = csv.writer(file)
        writer.writerow([Name, Age, Department])

def read_csv():
    with open(data_path, mode="r") as file:
        reader = csv.DictReader(file)
        print("\nEmployees older than 30:")
        for row in reader:
            name = row["Name"]
            age = int(row["Age"])
            if age > 30:
                print(name)
create_csv()
add_data("Roshna", 19, "Finance")
add_data("Salina", 35, "Marketing")
add_data("Prakriti", 39, "IT department")
add_data("Ashmita", 60, "Production")
add_data("Roar", 29, "HR")

read_csv()

import openpyxl
student_file_path = "results.xlsx"

def create_messy_dataset(student_file_path):
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.title = "Students Grades"

    sheet.append(["Student Name", "Grade"])
    sheet.append(["Roshna", "A"]) 
    sheet.append(["Salina", "B+"])
    sheet.append(["Prakriti", "A-"])
    sheet.append(["Ashmita", "B"])
    sheet.append(["pratushya", "A+"])

    workbook.save(student_file_path)
    print(f"Dataset created and saved to '{student_file_path}'.")

create_messy_dataset(student_file_path)

#http
import requests
api_url = "https://jsonplaceholder.typicode.com"
def fetch_and_display_titles(api_url):
    try:
        # Making a GET request to the API
        response = requests.get(api_url)
        
        # Checking if the request was successful
        if response.status_code == 200:
            posts = response.json()  # Parse the JSON data
            
            print("Titles of the first 5 posts:")
            for i, post in enumerate(posts[:5], start=1):  # Display titles of first 5 posts
                print(f"{i}. {post['title']}")
        else:
            print(f"Failed to fetch data. HTTP Status Code: {response.status_code}")
    except Exception as e:
        print(f"An error occurred: {e}")


