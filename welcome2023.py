import numpy as np

listofnumbers = list(range(10))
print("listofNumbers", listofnumbers)

# problem 2 list of alternate numbers
# listofnumbers = list(range(start number1,end number10,gap2))
listofnumbers = list(range(1, 10, 2))
print("listofNumbers", listofnumbers)
# list in reverse
# listofnumbers = list(range(10,1,-2)) minus takes the list in reverse
listofnumbers = list(range(1, 100, 1))
print("listofNumbers", listofnumbers)

# can we iterate through the list and print if it's the multiple of 3?
listofmultiplesof3 = []
for num in listofnumbers:
    if num % 3 == 0:
        print(num)

listofmultiplesof3 = list(range(3, 100, 3))
listofmultiplesof5 = list(range(5, 100, 5))
print("listofmultiplesof3=", listofmultiplesof3, "listofmultiplesof5=", listofmultiplesof5)
listofmultiplesof3and5 = []
for num in listofmultiplesof3:
    if num in listofmultiplesof5:
        listofmultiplesof3and5.append(num)
print("listofmultiplesof3and5=", listofmultiplesof3and5)

#  merge two lists
listofmultiplesof3or5 = listofmultiplesof3 + listofmultiplesof5
sortedlistofmultiplesof3or5 = sorted(listofmultiplesof3or5)
print("sortedlistofmultiplesof3or5=", sortedlistofmultiplesof3or5)

# remove duplicates from the merge list
deduplicatedlist = []
for numIndex in range(1, len(sortedlistofmultiplesof3or5), 1):
    num = sortedlistofmultiplesof3or5[numIndex - 1]
    next_num = sortedlistofmultiplesof3or5[numIndex]
    if num != next_num:
        deduplicatedlist.append(num)
print("deduplicatedlist=", deduplicatedlist)

listofwords = ["rahul", "prateek", "tushti", "rohit", "meenakshi"]
print("prateek" in listofwords)
