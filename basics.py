# This is our first python project

# variable declaration
someNumber = 1
print(someNumber)
print('someNumber= ', someNumber)
# variable declaration string
print('-'*50)
name = 'PRATEEK'
print("My Name is: ", name)
print('-'*50)

# simple for loop :type all numbers from 1 to 10



print('-'*50)

# simple if
# print only even number from 1 to 10
print('-'*50)
for num in range(10):
    remainderWhenDividingBy2 = num %2
    # print("num", num)
    # print("remainderWhenDividingBy2=", remainderWhenDividingBy2)
    # now we will use the if condition on the remainder
    # if the remaider is 1 then we will preint num+1, for even numbers
    if(remainderWhenDividingBy2==1):
        print(num+1)

print('-'*50)

#if using a function
# print only  even integers from 1 to 10
# we learn here about if,else,for loops
def isEven(num):
    remainderWhenDividingBy2 = num%2
    if remainderWhenDividingBy2==1:
        return False
    else:
        return True

print('-'*50)
for num in range(10):
    if isEven(num+1):
        print(num+1)

print('-'*50)

