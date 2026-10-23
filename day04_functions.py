# A function is a reusable block of code that performs a particular task. Write it once, then call it whenever you need it.

def api_test(): 
    print("API Test Passed")

api_test()

'''
def — tells Python you're defining a function.
api_test — the function's name.
() — parentheses; we'll use these for parameters later.
: — starts the function body.
Indented print() — the code that runs when the function is called.
api_test() — calls, or executes, the function.
'''

# Note: Defining a function does not execute its body. Calling it does.
# Remember: defining a function creates it; calling it executes its code. Each call runs the entire function body.

# Lesson 2: Parameters and arguments

def greet_user(name): # name : Parameter
    print(f"Hello {name}")

greet_user("Rashmi") # rashmu is an argument
greet_user("Bunny") # Bunny is an argument

# name is a parameter — a variable that receives a value when the function is called.
# "Rashmi" is an argument — the actual value passed to the function.

''' A simple way to remember:
- Parameter = placeholder in the function definition.
- Argument = actual value you pass when calling the function.'''

def status_code(code):
    if code in [200, 201]:
        print("API Test Passed")
    else:
        print("API Test Failed")

status_code(200)
status_code(201)
status_code(404)
status_code(500)

# Lesson 3: return vs print()

def sum(a,b):
    print(a + b)

sum(2, 4)

def add(a,b):
    return a + b

sum = add(2, 7)
print(sum)

'''
print() = Displays the value. It does not give that value back as the function's result.
return = Sends a value back to the calling code so you can store it, compare it, or use it in another calculation.
'''

# Lesson 4: Default parameters

def greet(name = "Rashmi"):
    return f"Hello {name}"

message = greet()
print(message)
message2 = greet("Bunny")
print(message2)

# Key takeaway: A default parameter makes a function flexible when an argument is optional.

# Lesson 5: Write your own API validation function

def validate_api(status_code):
    if status_code == 200:
        return "API Test Passed"
    else:
        return "API Test Failed"
    
response = validate_api(200)
print(response)

response = validate_api(404)
print(response)


# Lesson 6: Multiple parameters

def validate_api(status_code, response_time):
    if status_code == 200 and response_time < 2:
        return "API Test Passed"
    else:
        return "API Test Failed"

print(validate_api(200, 1))
print(validate_api(200, 3))
print(validate_api(404, 1))


# Lesson 7: Boolean return values (True / False)

def validate_api(status_code):
    if status_code == 200:
        return True
    else:
        return False

print(validate_api(200))
print(validate_api(404))


''' Iska simple meaning
- True = condition satisfied.
- False = condition satisfied nahi hui.'''

# Lesson 8: Functions aur Pytest ka connection

def validate(code):
    return code == 200

response = validate(200)
assert response

# Lesson 9: assert in Python

# assert ka use condition verify karne ke liye hota hai. QA testing mein hum check karte hain ki actual result expected result ke according hai ya nahi.
def validate(code):
    return code == 200

response = validate(200)
assert response
print("Test Passed")

# Important: Test failure ka matlab zaroori nahi ki application broken hai. Iska matlab hai ki assertion ki expectation satisfy nahi hui.


# Lesson 10: Expected vs Actual result

expected_status = 200
actual_status = 200

assert actual_status == expected_status
print("Status code validation passed")


# Lesson 11: Your first Pytest-style test

# def validate_api(status_code):
#     return status_code == 200

# def test_api_failure():
#     assert validate_api(404)

# test_api_failure()


# Final Practice: Build an API validation function


def validate_api(status_code):
    if status_code in [200, 201]:
        return True
    else:
        return False

print(validate_api(200))
print(validate_api(201))
print(validate_api(404))
print(validate_api(500))

def validate_api(code):
    return code in [200, 201]

print(validate_api(200))
print(validate_api(201))
print(validate_api(404))
print(validate_api(500))

# Lesson 12: Positional vs Keyword Arguments

# 1. Positional arguments

def login(name, role):
    return f"Hi, My name is {name} and I'm a {role} by profession"

response = login("Rashmi", "QA")
print(response)

# 2. Keyword arguments

def login(name = "Bunny", role = "Senior Executive"):
    return f"Hi, I'm a {role} and my name is {name}"

response = login()
print(response)


# Lesson 13: *args 
# *args function ko variable number of positional arguments accept karne deta hai.

def add(*nums):
    value = 0
    for num in nums:
        value += num
    return value

result = add(2,3)
print(result)
result = add(2,3,7)
print(result)

def fruits(*fruits):
    return fruits

print(fruits("Apple", "Mango", "Banana"))

# Here, values will print in tuple ()

# Lesson 13: **kwargs

def student_details(name, age):
    print(name)
    print(age)

student_details(name="Rashmi", age=24)


def flowers(**flowers):
    print(flowers)
    

flowers(flower1 = "Lily", flower2 = "Mogra")

''' Samjho:
- **kwargs multiple named values accept karta hai.
- Function ke andar kwargs ek dictionary (dict) hota hai.
- Har argument ka naam dictionary ki key aur uski value dictionary ki value ban jaati hai. '''

def test_details(**kwargs):
    print(kwargs["name"])
    print(kwargs["status"])

test_details(name="Login", status="PASS")

def report_test(**kwargs):
    print("Test Name:", kwargs["name"])
    print("Status:", kwargs["status"])
    print("Response Time:", kwargs["response_time"])

report_test(name="Login API", status="PASS", response_time=1.2)

def report_test(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

report_test(name="Login", status="PASS", browser="Chrome")


# Lesson 15: Local and Global Scope

''' Python mein abhi do types samjho:
- Local variable: Function ke andar bana variable.
- Global variable: Function ke bahar bana variable. '''

def login():
    username = "Admin"       # Local Variable
    print(username)
    
login()

status = "PASS"       # Global variable

def check_status():
    print(status)
    
check_status()

print(status)

environment = "QA"

def run_test():
    test_name = "Login API"
    print("Environment:", environment)
    print("Test:", test_name)

run_test()

def status_update():
    global status
    status = "FAIL"
    print(status)
    
status_update()
print(status)

# Lesson 16: return, None aur Early Return

def run_test():
    print("Test executed")

result = run_test()
print(result)

# Early return

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"  # Return early

    return a / b

print(divide(10, 2))  # 5.0
print(divide(10, 0))  # Cannot divide by zero

