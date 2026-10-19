# This is my first python program --> Comments in Python 

print("Hello World!")
print("I'm learning python")
print("My goal is to become QA Automation")

# Variables in Python

name = "Rashmi"  # Name (Variable), = (value assigned), Rashmi (stored value)
status_code = 200
message = "Learning Python"

print(name, status_code, message)

# Data Types in Python

tester_name = "Rashmi"  # string
years_of_experience = 3  # Integer
test_execution_time = 2.5  # Float
is_test_passed = True  # Boolean

print(type(tester_name))
print(type(years_of_experience))
print(type(test_execution_time))
print(type(is_test_passed))


# Practice

# Excercise 1 - Print Statement

print("Rashmi Rai")
print("I am learning Python from zero")
print("My goal is QA Automation")


# Exercise 2 — Variables

tester_name = "Rashmi Rai"
experience = 3
salary = 24950.21

print(tester_name)
print(experience)
print(salary)


# Exercise 3 - QA Test Data

status_code = 200
response_message = "Success"
is_test_passed = True

print(type(status_code))
print(type(response_message))
print(type(is_test_passed))


# Exercise 4 — Concept check

'''
1. print() ka kya use hai?
2. Variable kya hota hai?
3. "200" aur 200 mein kya difference hai?
4. True kis data type ka example hai?


Answers : 
1. Print() is a python built in function which is used to display the text mentioned inside the ()
2. Variable is used to store value
3. "200" will be considered as text (string) whereas 200 is considered as integer
4. True is the Boolean data type
'''

# Lesson 2: input() and Type Conversion

name = input("Enter your name : ")
print(f"Hello, {name}")

age = input("Enter your age: ")
print(age)
print(type(age))

new_age = int(input("Enter your age: "))
print(new_age)
print(type(new_age))

status_code = int(input("Enter status code: "))
print(status_code)

# Lesson 3: Operators

# 1. Arithmetic operators

a = 20
b = 10

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)

'''
Operator	Meaning
+	        Addition
-	        Subtraction
*	        Multiplication
/	        Division — decimal result
//	        Floor division — rounds down
%	        Remainder

QA example: Agar hum test execution time ya test cases ki count calculate kar rahe hain, 
toh arithmetic operators ka use kar sakte hain.
'''

# 2. Comparison operators

status_code = 200

print(status_code == 200)
print(status_code == 400)
print(status_code != 200)
print(status_code > 200)
print(status_code > 200)
print(status_code >= 200)
print(status_code <= 200)

'''
Ek important difference:
= means value assign karna.
== means do values compare karna.
'''


# Lesson 4: Conditions

status_code = 404

if status_code == 200:
    print("API Test Passed")
elif status_code == 201:
    print("Resource Created")
else:
    print("API Test Failed")
    

age = 17

if age >= 18: print("Eligible")
else: print("Not Eligible")


# Day 1 — Final Practice Question

'''
Question: API Status Code Validation

Write a Python program to validate an API response using if, elif, and else.

status_code = 201

Requirements:
1. If status_code is equal to 200, print "API Test Passed".
2. If status_code is equal to 201, print "Resource Created Successfully".
3. For any other status code, print "API Test Failed".

Expected output: Resource Created Successfully

Your task: Write the complete Python code yourself. Use only the topics we have learned so far—no logical operators yet.

'''

status_code = 201

if status_code == 200:
    print("API Test Passed")
elif status_code == 201:
    print("Resource Created Successfully")
else:
    print("API Test Failed")
    

'''
Question: API Response Validation

Write a Python program to validate an API response based on its status code and response time.

Given:
status_code = 200
response_time = 1500

Requirements:
1. If the status code is 200 and the response time is less than or equal to 1000 milliseconds, print "API Test Passed".
2. If the status code is 200 but the response time is greater than 1000 milliseconds, print "API Passed but Slow".
3. For any other status code, print "API Test Failed".

Expected output:
API Passed but Slow

'''
status_code = 200
response_time = 1500

if status_code == 200 and response_time <= 1000:
    print("API Test Passed")
elif status_code == 200  and response_time > 1000:
    print("API Passed but slow")
else:
    print("API Test Failed")

