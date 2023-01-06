# This file will be used to explore dictionnaries in python

# import libraries
import numpy as np, pandas as pd
import time

# code starts here
time_start =time.time()

# Run random loops
x = 0.0
# for i in range(1000000):
for i in range(10):
    x += i
print("the sum of first million numbers =", x)

# our first dictionary
height = {}
list = []

height["prateek"] = 167
height["rohit"] = 180
print("the height of prateek", height["prateek"])

# another way to dictonarry
hometown ={
    "rohit": "Kakinada",
    "prateek": "Jodhpur"
}
print("the hometown of prateek", hometown["prateek"])

# lets create dictonnaries from two list
names = ["rohit","prateek","tushti"]
month_of_birth = ["January","July","may"]
MOBs = {}
for i in range(len(names)):
    MOBs[names[i]] = month_of_birth[i]
print("MOBs =", MOBs)

for name in MOBs:
    print(name,"'s birthday is in ", MOBs[name], sep="")

# merge two dictionnaries
dict1 = {"ten": 10, "Twenty": 20, "thirty": 30}
dict2 = {"thirty": 30, "forty": 40, "fifty": 50}


for i in dict2:
    dict1[i] = dict2[i]
print("dict1=",dict1)

dict3 = dict1| dict2
print("dict3", dict3)

classISBm = {}
classISBm['names'] = ["prateek","rohit","tushti","meenakshi"]
classISBm["marks"] = [100,100,100,99]
classISBm["section"] = ["A","B","C","D"]

# convert to dictionary of students
students = {}

# for name in classISBm["names"]:
for i in range(len(classISBm['names'])):
   name = classISBm["names"][i]
   marks = classISBm["marks"][i]
   section = classISBm["section"][i]
   students[name] = {"marks":marks,"section":section}

print("students['tushti']=",students['tushti'])
print("students['prateek']=",students['prateek'])

print("students['tushti']['marks']=",students['tushti']['marks'])
print("students['tushti']['section']=",students['tushti']['section'])





#code ends here
time_end =time.time()
print("time taken to run the file =", time_end-time_start)
