# Lesson 1: Python for loops
for i in range(3):
    print("Hello")

# Lesson 1: for loop with range()
for i in range(5):
    print("API Test Passed")
    
# Lesson 2: Using range(start, stop)
for i in range(1, 6):
    print(i)
    
# Lesson 3: Using range() with a step
for i in range(2, 11, 3):
    print(i)

# Output : 2, 5, 8

# Lesson 4: Looping through a list

fruits = ["Apple", "Mango", "Banana", "Kiwi", "Papaya"]
for fruit in fruits:
    print(fruit)
    
status_codes = [200, 201, 404, 500]
for code in status_codes:
    print(code)
    
# Lesson 5: Using for loops with if

fruits = ["Apple", "Mango", "Banana", "Kiwi", "Papaya", "Pomegranate"]
for fruit in fruits:
    if fruit.startswith("P"):
        print(fruit)
    else:
        print("No fruit available")
        
status_codes = [200, 201, 404, 500]
for code in status_codes:
    if code == 200 or code == 201:
        print("API Passed", code)
    else:
        print("API Failed", code)

# Lesson 6: while loops

attempt = 1

while attempt <= 3:
    print("API test attempt:", attempt)
    attempt = attempt + 1
    
# Important: If you forget attempt = attempt + 1, the condition stays True forever because attempt remains 1. 
# This causes an infinite loop.


# Lesson 7: break and continue

# 1. break — Stop the loop immediately

for code in [200, 201, 500, 404]:
    if code == 500:
        break
    print(code)
    
# 2. continue — Skip the current iteration

for code in [200, 201, 500, 404]:
    if code == 500:
        continue
    print(code)

''' Remember:
- break = stop the entire loop.
- continue = skip this iteration and keep looping. '''


# ASSIGNMENT : Loop through the API status codes. Print PASS for status 200 and 201, 
# print FAIL for other status codes, and skip status 404 entirely.

status_codes = [200, 404, 500, 201]

for code in status_codes:
    if code == 404:
        continue
    if code == 200 or code == 201:
        print(code, "PASS")
    else:
        print(code, "FAIL")
