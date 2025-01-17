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
