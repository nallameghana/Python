# -*- coding: utf-8 -*-
"""Python

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1JH1PuZ1u4X6qkkmAzc4UZ1SiZPO4Y9RG
"""

print("Hello World")
n = int(input("Enter a no : "))
print(len(str(n)))

import datetime
datetime.datetime.now()

import keyword
keyword.kwlist

n = 10
print(type(n))
name = "Meghana"
print(type(name))
a = True
print(type(a))
b = 1.34
print(type(b))
k = 3 + 4j
print(type(k))
m = "3"
print(type(m))

a = """
BVRIT
BACHUPALLY
HYDERABAD
"""
print(a)
print(bool(9000000))
print(bool(0.00))
print(bool(-1))
name = input("Enter a name : ")
age = int(input("Enter your age : "))
if(age >= 18):
    print("Eligible to vote")
else:
    print("Not Eligible to vote")

r = int(input("Enter radius : "))
pii = 3.14
area = pii * r * r
print(area)

a = int(input())
b = int(input())
c = int(input())
if((a > b) and (a > c)):
    print("a is maximum", a)
elif(b > c):
    print("b is maximum", b)
else:
    print("c is maximum", c)

age = int(input("Enter the age : "))
if((age > 0) and (age < 5)):
    print("No ticket is required to travel")
elif((age >= 5) and (age < 15)):
    print("The price of ticket is : ", 200)
elif((age >= 15) and (age < 60)):
    print("The price of ticket is : ", 400)
else:
    print("The price of ticket is : ", 280)

a = "Meghana"
m = "AEIOUaeiou"
for i in a:
    if i in m:
        print(i)

i = 1
sum = 0
while i <= 10:
    sum += i
    i += 1
print(sum)

i = 1
sum = 0
while i <= 10:
    if i%2 == 0:
        sum += i
    i += 1
print(sum)

for i in range(0, 11):
    print(i, end = " ")

for i in range(1, 5):
    for j in range(i):
        print("#", end = " ")
    print()

n = int(input("Enter n : "))
for i in range(n, 0, -1):
    for j in range(i):
        print("#", end = " ")
    print()

#Reverse a number
n = int(input("Enter a no : "))
sum = 0
while n != 0:
    r = n % 10
    sum = (sum * 10) + r
    n = n // 10
print(sum)

#Sum of the digits of a number
n = int(input("Enter a no : "))
sum = 0
while n != 0:
    r = n % 10
    sum += r
    n = n // 10
print(sum)

'''To check
whether the given number is palindrome'''
n = int(input("Enter a no : "))
a = n
sum = 0
while n != 0:
    r = n % 10
    sum = (sum * 10) + r
    n = n // 10
if sum == a:
    print("The given no is a palindrome")
else:
    print("The given no is not a palindrome")

#To check if a no is armstrong
n = int(input("Enter a no : "))
sum = 0
a = n
while n != 0:
    r = n % 10
    sum += (r ** len(str((a))))
    n = n // 10
if sum == a:
    print("The given no is armstrong no")
else:
    print("The given no is not armstrong")

#To check a no is perfect
n = int(input("Enter a no : "))
sum = 0
a = n
for i in range(1, n):
    if((n % i) == 0):
        sum += i
if sum == a:
    print("The given no is perfect")
else:
    print("The given no is not perfect")

#Generate prime nos
n = int(input("Enter a no upto which you want prime nos : "))
for i in range(2, n + 1):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        print(i, end = " ")

#Fibonacci series
n = int(input("Enter a no upto which you want fibonacci series : "))
a = 0
b = 1
print(0, 1, end = " ")
for i in range(n - 2):
    c = a + b
    a = b
    b = c
    print(c, end = " ")

name = input()
if name[::-1] == name:
    print("It is palindrome")
else:
    print("It is not a palindrome")

marks = [10, 50, 20, 199, 45]
max = marks[0]
for i in marks:
    if i > max:
        max = i
print(max)

l = [3, 4, 2, 7, 9, 4, 6, 3, 2]
sum = 0
for i in l:
    sum += i
print(sum)

m = []
for i in range(10):
    m.append(i)
print(m)

m = [i ** 2 for i in range(10)]
print(m)

m = [5 * i for i in range(1, 11)]
print(m)

list = ["Moscow", "Sweden", "Malaysia", "India", "Norway"]
for i in list:
    if((i[0] == 'M') or (i[0] == 'S')):
        print(i)

a = 0
b = 1
list = []

n = int(input("\nEnter n : "));
for i in range(n - 2):
    c = a + b
    a = b
    b = c
    list.append(c)
print([0, 1] + list)

name = input("\nEnter the name : ")
for i in name:
    print(i, name.count(i))

#1
#pythagorean theorem
import math
s = input("select which you want to evaluate a, b ,c")
if s == 'a':
    b = float(input("Enter b :"))
    c = float(input("Enter c :"))
    a = math.sqrt(c**2 - b**2)
    print(a)
elif s == 'b':
    a = float(input("Enter a : "))
    c =float(input("Enter c : "))
    b = math.sqrt(c**2 - a**2)
    print(b)
else:
    a = float(input("Enter a : "))
    b = float(input("Enter b : "))
    c = math.sqrt(a**2 + b**2)
    print(c)

#2
#Userid and password
n = 1
while((n >= 1) and (n <= 3)):
    n += 1
    name = input("Enter user name :")
    password = input("Enter password :")
    if name == password:
        print("Successfully loggedin")
        break
    else:
        print("login failed, try again")

#3
#age wise price of ticket
age = int(input("Enter age : "))
if((age > 0) and (age <= 5)):
    print("Can travel without ticket")
elif((age >= 6) and (age <= 12)):
    print("The price of ticket is : ", 250)
elif((age >=13) and (age <= 59)):
    print("The price of ticket is : ", 500)
elif((age >= 60) and (age <= 100)):
    print("The price of ticket is : ", 350)
else:
    print("Invalid input!!")

#4
#Fibonacci series
a = 0
b = 1
list = []

n = int(input("\nEnter n : "));
for i in range(n - 2):
    c = a + b
    a = b
    b = c
    list.append(c)
print([0, 1] + list)

#5
#Sales in a hotel
def sales(lst):
    sumofsales = 0
    for i in lst:
        sumofsales += i
    return sumofsales
sales([30, 250, 180, 500])

#6
#name in capitals
def cap(n):
    return n.upper()

cap("Meghana")

#7
#List of countries which start with S and M
list = ["Moscow", "Sweden", "Malaysia", "India", "Norway"]
for i in list:
    if((i[0] == 'M') or (i[0] == 'S')):
        print(i)

#8
#BMI calculation
wt = float(input("Enter the weight in kgs : "))
h = float(input("Enter the height in mtrs : "))
BMI = wt / (h**2)
print(BMI)

#9
#To perform calculator on 2 oparands
a = float(input("Enter a : "))
b = float(input("Enter b : "))
choice = input("Enter choice : 1. +, 2. -, 3. *, 4. /")
if choice == '+':
    print("Addition of 2 given nos is : ", a + b)
elif choice == '-':
    print("Sub of 2 given nos is : ", a - b)
elif choice == '*':
    print("Mult of 2 nos is : ", a * b)
elif choice == '/':
    print("Div of 2 given nos is : ", a / b)
else:
    print("Invalid input!!")

#10
#converting foriegnheit temp to celcius temp
def f_to_c(far):
    return (far - 32) * (5 / 9)
f_to_c(65)

print("OOPS: OBJET ORIENTED PROGRAMMING")

class Human:
    population = 0
    data = []
    def __init__(self, name, age, hobby): #instance variable
        self.name = name
        self.age = age
        self.hobby = hobby
        Human.population += 1
        Human.data.append(self.name)
    def greet(self):
        print(f"Hey my name is {self.name}.")

a = Human("Meghana", 18, "playing")
a.age

b = Human("Meghana", 18, "playing")
b.greet()

c = Human("Sathwika", 20, "painting")
c.population

Human.data

#Factorial of a given number
def fact(n):
    if((n == 0) or (n == 1)):
        return 1
    else:
        return n*fact(n - 1)
n1 = int(input("Enter no of terms : "))
for i in range(n1):
    print(fact(i), end = " ")

#Fibonacci series
def fib(n):
        if(n == 0):
            return 0
        elif(n == 1):
            return 1
        else:
            return fib(n - 1) + fib(n - 2)
n1 = int(input("Enter no of terms : "))
lst = []
for i in range(n1):
    a = fib(i)
    lst.append(a)
print(lst)

#project euler problems
# Sum of multiples of 3 or 5 below 1000
sum = 0
for i in range(1000):
    if((i%3 == 0) or (i%5 == 0)):
        sum += i
print("Sum = ", sum)

#Even fibonacci numbers
a = 0
b = 1
for i in range(30):
    c = a + b
    a = b
    b = c
    if(c%2 == 0):
        print(c, end = " ")

#largest prime factor
a = int(input("Enter a number to find largest prime factor :"))
lst = []
for i in range(2, a):
    for j in range(2, i):
        if i%j == 0:
            break
    else:
        lst.append(i)
for k in lst[::-1]:
    if(a%k == 0):
        break
print(k)

#10001st prime number
def isprime(n):
    for i in range(2, n):
            if(n%i == 0):
                return 0
            else:
                continue
    return 1
def Nthprime(no):
    prime = 1
    Nth_prime = 0
    while(Nth_prime < no):
        prime += 1
        if(isprime(prime)):
            Nth_prime += 1
    return prime

Nthprime(10001)

#1000 - digit Fibonacci number
def nthfib(N):
    a = 0
    b = 1
    nf = 2
    while(nf < N):
        c = a + b
        nf += 1
        a = b
        b = c
    return c
print(nthfib(20))

def prime(n):
    sum = 0
    for i in range(2, n):
        if(n%i == 0):
            return 0
        else:
            continue
    return 1
prime(19)

lst = []
for i in range(30):
    if(i%2 == 0):
        continue
    else:
        lst.append(i)
print(lst)

#Nth perfect no
def perfect(n)->bool:
    a = n
    sum = 0
    for i in range(1, n):
        if(n%i == 0):
            sum += i
        else:
            continue
    if(a == sum):
        return True
    else:
        return False
def Nthperfect(no)->int:
    per = 0
    nth_per = 0
    while(nth_per < no):
        per += 1
        if(perfect(per)):
            nth_per += 1
    return per
Nthperfect(4)

#Sum square difference
def ssd(no):
    sq_s = 0
    ss_q = 0
    for i in range(no):
        sq_s += i**2
        ss_q += i
    return (ss_q)**2 - sq_s
ssd(11)

#collatz series
def collatz(n):
    lst = []
    if(n%2 == 0):
        lst.append(n//2)
        n = n//2
    else:
        lst.append(3*n + 1)
        n = 3*n + 1
    while(n > 1):
        if(n%2 == 0):
            lst.append(n//2)
            n = n//2
        else:
            lst.append(3*n + 1)
            n = 3*n + 1
    return lst

collatz(1)

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

fib(6)

#Anagram
n1 = input("Enter string1 :")
n2 = input("Enter string2 :")
a = sorted(n1)
b = sorted(n2)
res = 1
for i1,i2 in zip(a,b):
    if(i1 != i2):
        res = 0
        break
    else:
        continue

if(res == 1):
    print("Both strings are anagram to each other.")
else:
    print("Both strings are not anagram to each other.")

#OR
n1 = input("Enter string1 : ")
n2 = input("Enter string2 : ")
if sorted(n1) == sorted(n2):
    print("Both strings are anagram to each other.")
else:
    print("Both strings are not anagram to each other.")

"""# Lambda, Reduce, Map, Filter functions :"""

#Lambda function is also called as anonymus function
#syntax lambda var_name : fqn on that variable
#Filter. It is used to filter specific elements
#syntax var_name = list(filter(function), iterable)
#We use map function if you want to perform same function on every no in iterable
#syntax var_name = map(function, iterable)
#We use reduce to take multiple values and convert it to one variable
#We cant use reduce directly as it is under functools
#syntax var_name = reduce(function, iterable)

def is_odd(n):
    if n%2 == 1:
        return 1
lst = [1, 4, 6, 7, 9, 8, 3]
odd_lst = list(filter(is_odd, lst))
print(odd_lst)

#Same program using lambda function
lst = [1, 4, 6, 7, 9, 8, 3]
odd_lst = list(filter(lambda n : n%2 == 1, lst))
print(odd_lst)

#We use map function if you want to perform same function on every no in iterable
lst = [1, 4, 6, 7, 9, 8, 3]
odd_lst = list(filter(lambda n : n%2 == 1, lst))
#To double every element in odd_lst
squares = list(map(lambda x : x **2, odd_lst))
print(squares)

#We cant use reduce directly as it is under functools
#We use reduce to take multiple values and convert it to one variable
from functools import reduce
lst = [1, 4, 6, 7, 9, 8, 3]
odd_lst = list(filter(lambda n : n%2 == 1, lst))
#To double every element in odd_lst
squares = list(map(lambda x : x **2, odd_lst))
print(squares)
sum = reduce(lambda a, b : a + b, squares)
print(sum)

"""# List Comprehensions"""

#To reduce the no of steps

lst = [i**2 for i in range(1, 11)]
print(lst)

#Using if condition
lst = [i**2 for i in range(1, 11) if i%2 == 0]
print(lst)

#Using nested if
lst = [i for i in range(1, 20) if i%2 == 0 if i%3 == 0]
print(lst)

#Using if-else
lst = [i**2 if i%2 == 0 else i*2 for i in range(20)]
print(lst)

def fib(n) -> list:
    lst = []
    a = 0
    b = 1
    lst.append(0)
    lst.append(1)
    for i in range(n-2):
        c = a + b
        lst.append(c)
        a = b
        b = c
    return lst
fib(9)

lst = ["Mango", "Apple", "Guava", "Banana"]
l = list(map(lambda x:x.upper(), lst))
print(l)

l = ["india", "japan", "korea", "italy"]
ls = list(map(lambda x:x.capitalize(), l))
print(ls)

marks = [2, 7, 8, 3, 1, 10, 0]
sum = 0
for i in marks:
    sum += i
avg = float(sum)/len(marks)
m = [i for i in marks if i>avg]
print(m)
n = [k for k in marks if k<avg]
print(n)

lst = ["Apple", "Banana", "America", "Boat", "Bun", "Orange"]
n = lst[::-1]
print(n)
m = list(filter(lambda x: x[0]=='B', lst))
print(m)

from functools import reduce
lst = [1, 2, 4, 5, 3, 8, 9, 10]
m = reduce(lambda x, y: x + y, lst)
print(m)

#Converting a number into binary number
n = int(input("Enter n :"))
lst = []
while(n > 0):
    r = n%2
    lst.append(r)
    n = n//2
m = lst[::-1]
n = ' '.join(map(str, m))
print(n)

#Converting a list to string
m = ["Hi!", "my", "name", "is", "Meghana"]
n = ' '.join(map(str, m))
print(n)

#Converting a binary number to number
from functools import reduce
n = int(input("Enter n :"))
k = [int(i) for i in str(n)]
m = k[::-1]
j = [2**i for i in range(len(m))]
lst = []
for i1,i2 in zip(m, j):
    lst.append(i1*i2)
s = reduce(lambda x, y : x + y, lst)
print(s)

#Subtract 2 lists element by element
lst = []
m = [6, 7, 8, 4, 2]
n = [3, 8, 4, 2, 1]
for i1,i2 in zip(m,n):
    lst.append(i1 - i2)
print(lst)

#Converting a no to roman no
def int_to_roman(n):
    if(n == 1):
        return 'I'
    elif(n == 5):
        return 'V'
    elif(n == 10):
        return 'X'
    elif(n == 50):
        return 'L'
    elif(n == 100):
        return 'C'
    elif(n == 500):
        return 'D'
    elif(n == 1000):
        return 'M'
m = [int(i) for i in str(n)]
k = [10**(len(str(n))-1) for i range(str(n))]

m = [i for i in range(1, 10, 2)]
m

"""# OOPS:(Object Oriented Programing)"""

class computer:
    def __init__(self, cpu, ram):
        self.cpu = cpu
        self.ram = ram
    def config(self):
        print("Config is ", self.cpu, self.ram)
comp1 = computer("i5", 16)
comp2 = computer("i3", 8)
comp1.config()
comp2.config()

#CAR class
class car:
    wheels = 4 #Class varibles(If we change no of wheels it will change for every object)
    def __init__(self, mil, comp, col, cost):
        self.mil = mil
        self.comp = comp
        self.col = col
        self.cost = cost
    def config(self):
        print("configurations of car are ", self.mil, self.comp, self.col, self.cost, self.wheels)
c1 = car(10, "hundai", "black", "1000000")
c2 = car(11, "Benz", "black", "6400000")
c1.config()
c2.config()

#Instance method.If you are working with instance variable use self keyword
#Class method, if you are working with class varible use cls keyword.
#Static method if you have nothing to do with cls or instance variable static method can be used, in static method we dont use any keyword.

class student:
    school = "SPR"
    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
    def avg(self):
        return (self.m1 + self.m2 +self.m3)/3
    @classmethod    #Decorater
    def sch(cls):
        return cls.school
    @staticmethod    #Decorater
    def info():
        print("This is a student class")

s1 = student(50, 100, 80)
print(s1.avg())
print(student.sch())
student.info()

#Class inside a class method
class student:
    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno
        self.lap = self.laptop()
    def show(self):
        print(self.name, self.rollno)
    class laptop:
        def __init__(self):
            self.brand = "DELL"
            self.pr = 'i5'
            self.ram = 16
        def show(self):
            print(self.brand, self.pr, self.ram)

s1 = student("Meghana", 1225)
s1.show()
lap1 = student.laptop()
lap1.show()

#Inheritance
#If you want the of a  created class and other class which is defined .Then we can get the features by inheriting it.
#Other class is known as parent class (or) super class, the one which inherits it is known as child (or) sub class

class A:
    def feature1(self):
        print("Feature 1 is working")
    def feature2(self):
        print("Feature 2 is working")
class B(A):                                 #If you want to inherit the features of a to b just do b(a)
    def feature3(self):
        print("Feature 3 is working")
    def feature4(self):
        print("Feature 4 is working")
class C(B):
    def feature4(self):
        print("Feature 5 is working")       #By C we can access feature1, 2, 3, 4, 5
a1 = A()
a1.feature1()
b = B()
b.feature1()
c = C()
c.feature1()

#Multi level inheritance
class A:
    def feature1(self):
        print("Feature 1 is working")
    def feature2(self):
        print("Feature 2 is working")
class B:                                   #Here A, B are seperate classes
    def feature3(self):
        print("Feature 3 is working")
    def feature4(self):
        print("Feature 4 is working")
class C(A, B):                             #C is inherting 2 seperate classes A and B(MultiLevel Inheritance)
    def feature4(self):
        print("Feature 5 is working")

c = C()
c.feature3()

def create_board():
     board = []
     for i in range(3):
         row = []
         for j in range(3):
             row.append('-')
         print(row)
         board.append(row)
create_board()

import numpy as np
np.random.rand(0, 1)

m = [1, 2, 3, 4, 5]
m.remove(1)
m

n = int(input())
lst = []
for i in range(n):
    lst.append(int(input()))
lst1 = []
for i in lst:
    if(i not in lst1):
        lst1.append(i)
    else:
        lst1.remove(i)
for i in lst1:
    print(i, end = " ")

lst="1 2 3 6 8 0"
print(lst.split())

n = input()
lst = list(map(int, n.split()))
lst1 = []
while(lst[0] != 0):
    lst1.append(lst[0]%2)
    lst[0] = lst[0] / 2
if(lst1[lst[1]] == 1):
    print("Yes")
else:
    print ("No")

print(ord('A'))
print(ord('Z'))
print(ord('a'))
print(ord('z'))

ord('z')

for i in range(1, 9, 2):
    print(i)

n = int(input())
def evenpair(n):
    l = [2*int(i) for i in range(1,n//2)]
    for i in l:
        j = n - i
        if j%2 == 0:
            return 1
    return 0
r = evenpair(n)
if r == 1:
    print("Yes")
else:
    print("No")

n = int(input())
l = list(map(int, input().split()))
test_c = int(input())
l1 = []
for i in range(test_c):
    a, b = tuple(map(int, input().split()))

s = input()
j = 0
m = "hello"
s1 = [i for i in s]
k = [i for i in m]
for i in s1:
    if i == k[j]:
        j += 1
if j == 5:
    print("YES")
else:
    print("NO")

n = "My name is abc"
k = n.replace(' ', '')
print(k)

for i in range(0, 5):
    print(i)