# Lesson 1: Assignment Operators

request = 10
print(request)
request += 3    # request = request + 3
print(request)
request -= 4    # request = request - 4
print(request)
request *=5
print(request)
request /=4
print(request)
request %=8
print(request)
request//=3

print(request)

# Lesson 2: Logical operators

# 1. 'and' logical operator  --> Both conditions must be true

status_code = 200
response_time =  900

print(status_code == 200 and response_time == 900)

'''
if status_code >=200 and response_time <= 1500:
    print(status_code, response_time)
else:
    print("No issues")
    
'''

# 2. 'or' logical operator --> At least one condition must be true

print(status_code == 300 or response_time == 900)

# 3. 'not' logical operator --> Reverses the result

print(status_code != 200)
print(response_time != 800)


# Lesson 3: Membership operators --> Membership operators check whether a value exists inside a collection, such as a list or a string.
# 'in' , 'not in'

status_codes = [200, 201, 400, 404, 500]
print(404 in status_codes)
print(404 not in status_codes)


# Lesson 4: Identity operators --> Identity operators check whether two variables refer to the same object in memory.
# This is different from checking whether two values are equal.

''' There are two operators:
- is — checks whether two references point to the same object.
- is not — checks whether they point to different object '''

a = [200, 201]
b = [200,201]

print(a == b)
print(a is b)

c = "Rashmi"
d = c

print(c == d)
print(c is d)


# Lesson 5: Bitwise operators - Bitwise & and Bitwise |

# 1. Bitwise & - A bit becomes 1 only when both bits are 1.
a = 5  # Binary: 0101
b = 3  # Binary: 0011

print(a & b)

# 2. Bitwise | - A bit becomes 1 when at least one bit is 1.

a = 5  # Binary: 0101
b = 3  # Binary: 0011

print(a | b)


# 3. Lesson 5 continued: XOR (^) --> XOR means exclusive OR. A bit becomes 1 when the two bits are different.

'''
First bit	Second bit	Result
0	            0	        0
0	            1	        1
1	            0	        1
1	            1	        0
'''

# 4. Lesson 5 continued: Bitwise NOT (~) --> The ~ operator flips all bits. 
# In Python, integers behave as though they use signed two's-complement representation, so a useful rule is:
#  ~n = -(n + 1)

a = 5
print(~a)


# 5. Lesson 5 continued: Left shift (<<) --> The left-shift operator moves the binary bits to the left. 
# For non-negative integers, shifting left by one position is equivalent to multiplying by 2.

a = 5
print(a << 1)  # Simple as multiply by 2
print(a << 2)

# 6. Lesson 5 continued: Right shift (>>) --> The right-shift operator moves binary bits to the right. 
# For non-negative integers, each shift by one position is equivalent to integer division by 2, rounding down

a = 12
print(a >> 1)



