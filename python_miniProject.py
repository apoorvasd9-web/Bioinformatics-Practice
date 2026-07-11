Python 3.13.9 (tags/v3.13.9:8183fa5, Oct 14 2025, 14:09:13) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#Print Function
print("Hello World")
Hello World
#Variables
name = "Apoorva"
age = 24
print(name)
Apoorva
print(age)
24
#Data Types
name = "Apoorva"
age = 24
height = 5.1
student = True
print(type(name))
<class 'str'>
print(type(age))
<class 'int'>
print(type(height))
<class 'float'>
print(type(student))
<class 'bool'>
#input() Function
name = input("Enter your name: ")
Enter your name: Apoorva
print(name)
Apoorva
#int()
age = int(inout("Enter your age: "))
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    age = int(inout("Enter your age: "))
NameError: name 'inout' is not defined. Did you mean: 'input'?
age = int(input("Enter your age: "))
Enter your age: 24
print(age)
24
print(type(age))
<class 'int'>
#float()
salary = float(input("Enter salary: "))
Enter salary: 50000
print(salary)
50000.0
print(type(salary))
<class 'float'>
#str()
number = 100
text = str(number)
print(text)
100
print(type(text))
<class 'str'>
#bool()
print(bool(100))
True
print(bool(0))
False
#Arithmetic Operators
a = 30
b = 20
print(a + b)
50
print(a - b)
10
print(a * b)
600
print(a / b)
1.5
print(a % b)
10
print(a // b)
1
print(a ** b)
348678440100000000000000000000
#Assignment Operators
x = 10
x += 5
print(x)
15
x -= 2
print(x)
13
x *= 2
print(x)
26
x /= 2
print(x)
13.0
#Comparison Operators
a = 20
b = 10
print(a == b)
False
print(a != b)
True
print(a > b)
True
print(a < b)
False
print(a >= b)
True
print(a <= b)
False
#Logical Operators
print(True and False)
False
print(True or False)
True
print(not True)
False
#Membership Operators
fruits = ["Apple", "Banana", "Mango"]
print("Apple" in fruits)
True
print("Orange" not in fruits)
True
#Identity Operators
x = [1, 2]
y = x
print(x is y)
True
print(x is not y)
False
#len()
name = "Apoorva"
print
<built-in function print>
print(len(name))
7
#range()
print(list(range(5)))
[0, 1, 2, 3, 4]
print(list(range(2, 7)))
[2, 3, 4, 5, 6]
print(list(range(2, 10, 2)))
[2, 4, 6, 8]
#list()
text = "CAT"
print(list(text))
['C', 'A', 'T']
#tuple()
text = "CAT"
print(tuple(text))
('C', 'A', 'T')
#sat()
#set()
fruits = ["Apple", "Banana", "Apple"]
print(set(fruits))
{'Apple', 'Banana'}
#dict()
student = {
    "Name": "Apoorva",
    "Age": 24
}
print(student)
{'Name': 'Apoorva', 'Age': 24}
#Sum()
marks = [80, 90, 70]
print(sum(marks))
240
#Max()
marks = [80, 90, 70]
print(max(marks))
90
#min()
marks = [94, 91, 89]
print(min(marks))
89
#Sorted()
numbers = [25, 10, 40, 15]
print(sorted(numbers))
[10, 15, 25, 40]
#Desending order:
numbers = [25, 10, 40, 15]
print(sorted(numbers, reverse=True))
[40, 25, 15, 10]
#abs()
number = -45
print(abs(numbers))
Traceback (most recent call last):
  File "<pyshell#119>", line 1, in <module>
    print(abs(numbers))
TypeError: bad operand type for abs(): 'list'
print(abs(number))
45
#round()
marks = 89.7
print(round(marks))
90
#Enumerate()
fruits = ["Apple", "Banana", "Mango"]
print(list(enumerate(fruits)))
[(0, 'Apple'), (1, 'Banana'), (2, 'Mango')]
#Zip()
names = ["Apoorva", "Chandan"]
marks = [90, 80]
print(list(zip(names, marks)))
[('Apoorva', 90), ('Chandan', 80)]


#Mini Project : Student MArks Ananlysis System
print("===== Student Marks Ananlysis System =====")
===== Student Marks Ananlysis System =====
name = input("Enter your name: ")
Enter your name: Apoorva
print("Welcome", name)
Welcome Apoorva
age = int(input("Enter your age: "))
Enter your age: 24
print(age)
24
print(type(age))
<class 'int'>
marks = []
marks.append(int(input("Enter Mark 1: ")))
Enter Mark 1: 72
marks.append(int(input("Enter Mark 2: ")))
Enter Mark 2: 86
marks.append(int(input("Enter Mark 3: ")))
Enter Mark 3: 92
marks.append(int(input("Enter Mark 4: ")))
Enter Mark 4: 66
marks.append(int(input("Enter Mark 5: ")))
Enter Mark 5: 78
print(marks)
[72, 86, 92, 66, 78]
#Length
print("Total subjects =", len(marks))
Total subjects = 5
print("Total Marks =", sum(marks))
Total Marks = 394
print("Highest Mark =", max(marks))
Highest Mark = 92
print("Lowest Mark =", min(marks))
Lowest Mark = 66
average = sum(marks)/len(marks)
print(average)
78.8
print(round(average))
79
print(sorted(marks))
[66, 72, 78, 86, 92]
print(sorted(marks, reverse=True))
[92, 86, 78, 72, 66]
marks_tuple = tuple(marks)
print(marks_tuple)
(72, 86, 92, 66, 78)
marks_set = set(marks)
print(marks_set)
{66, 72, 78, 86, 92}
student = {
    "Name": name,
    "Age": age,
    "Marks": marks
}
print(student)
{'Name': 'Apoorva', 'Age': 24, 'Marks': [72, 86, 92, 66, 78]}
for i, mark in enumerate(marks):
    print(i, mark)

    
0 72
1 86
2 92
3 66
4 78
subjects =
SyntaxError: invalid syntax
subjects = [
    "Python", "Math", "English", "Science",
    "Biology"]
for subject, mark in zip(subjects, marks):
...     print(subject, mark)
... 
...     
Python 72
Math 86
English 92
Science 66
Biology 78
>>> abs()
Traceback (most recent call last):
  File "<pyshell#182>", line 1, in <module>
    abs()
TypeError: abs() takes exactly one argument (0 given)
>>> number = -25
>>> print(abs(number))
25
>>> print(bool(name))
True
>>> print(bool(age))
True
>>> height = float(input("Enter Height: "))
Enter Height: 5.1
>>> print(height)
5.1
>>> print(type(height))
<class 'float'>
>>> roll = 101
>>> roll =str(roll)
>>> print(roll)
101
>>> print(type(roll))
<class 'str'>
>>> for i in range(1, 6):
...     print(i)
... 
...     
1
2
3
4
5
