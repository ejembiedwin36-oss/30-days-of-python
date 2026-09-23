# --- Section 1: Basic Variables & Types ---
age = 26
height = 9.75
store = 3 + 2j  # 2j represents a complex/imaginary number in Python
print(age, height, store)

# --- Section 2: Triangle Area Calculator ---
base = float(input("Enter the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))
area = 0.5 * base * height
# print(area) # it work too
print(f'Area of triangle is {area}')

# --- Section 3: Triangle Perimeter Calculator ---
# FIX: Changed prompts to ask for "side" measurements instead of "perimeter"
side_a = int(input("Enter side A of the triangle: "))
side_b = int(input("Enter side B of the triangle: "))
side_c = int(input("Enter side C of the triangle: "))

perimeter = side_a + side_b + side_c 
print(f'The perimeter of tringle is {perimeter}')

# --- Section 4: Rectangle Math ---
lenght = 10   # Note: Common spelling is 'length', but code works because it is consistent
width = 20
area =  lenght * width
perimeter = 2 * (lenght + width)
print(area, perimeter)

# --- Section 5: Circle Math ---
pi = 3.14
radius = float(input("Enter the radius of the circle: "))

area = pi * radius * radius
circumfrence = 2 * pi * radius  # Note: Common spelling is 'circumference'

print(f"Area: {area}")
print(f"Circumfrence: {circumfrence}")


# FIX: Added '#' comments to this text block below so it won't crash Python
# skip these once for now. Question 8
# Calculate the slope, x-intercept and y-intercept of y = 2x -2
# Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
# Compare the slopes in tasks 8 and 9.
# Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.

"""
NOTE: This whole math block is wrapped inside a multi-line string , 
which acts as a giant comment. Remove the triple quotes if you want this to run!

import math

# --- 1. Analysis of y = 2x - 2 (Task 8) ---
slope_8 = 2
y_intercept_8 = -2
x_intercept_8 = -y_intercept_8 / slope_8

print("=== Task 8: Equation Analysis ===")
print(f"Slope (m): {slope_8}")
print(f"y-intercept: (0, {y_intercept_8})")
print(f"x-intercept: ({x_intercept_8}, 0)\n")


# --- 2. Points (2, 2) and (6, 10) (Task 9) ---
x1, y1 = 2, 2
x2, y2 = 6, 10

slope_9 = (y2 - y1) / (x2 - x1)
distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

print("=== Task 9: Two Points Analysis ===")
print(f"Slope between points: {slope_9}")
print(f"Euclidean Distance: {distance:.2f}\n")


# --- 3. Compare Slopes ---
print("=== Slope Comparison ===")
if slope_8 == slope_9:
    print(f"The slopes are identical! Both equal {slope_8}.\n")
else:
    print("The slopes are different.\n")


# --- 4. Finding where y = x^2 + 6x + 9 is 0 ---
print("=== Finding the Root for y = x^2 + 6x + 9 ===")

# Test a range of x values from -5 to 1 to find where y becomes 0
for x in range(-5, 2):
    y = x**2 + 6*x + 9
    print(f"When x = {x:>2}, y = {y}")
    
    if y == 0:
        print(f"Found it! y is exactly 0 when x = {x}")"""



# --- Section 6: Text String Comparisons (Number 12) ---
print(len('python'))
print(len('python') == len('dragon'))  # Compares lengths (6 == 6) -> Output: True

if 'on' in 'python' and 'on' in 'dragon':
    print("True")

if 'in' in 'Edwin' and 'in' in 'Godwin':
    print('True')

sentence = "I hope this course is not full if jargon."
if "jargon" in sentence:
    print("Found 'jargon'!")
else:
    print("'jargon' was not found.")

# --- Section 7: Type Conversions ---
word = 'python'
word_length_float = float(len(word))  # len() gives 6, float() turns it into 6.0
print(word_length_float)

# Check if number is an even number or odd number
number = int(input("Enter a number: "))
if number % 2 == 0:  # % 2 calculates the remainder. If remainder is 0, it's even.
    print(f"{number} is an even number.")
else:
    print(f"{number} is an odd number.")

floor_div = 7 // 3  # // performs floor division (chops off decimals) -> results in 2
int_val = int(2.7)  # int() drops decimal places -> results in 2
if floor_div == int_val:
    print(f"True! Both equal {floor_div}")
    
# Check if the types are the same
result = (type('10')) == type(10)  # Compares text type (str) to number type (int) -> False
print(result)

# Handling decimal string conversion securely
result = int(float('9.8'))  # Must use float() first because int('9.8') crashes directly
print(result == 10)  # Output: False (9 is not equal to 10)

result_rounded = round(float('9.8'))  # Rounds 9.8 up to 10
print(result_rounded == 10)  # Output: True (10 is equal to 10)

# --- Section 8: Work Pay Calculator ---
hours = float(input("Enter hours: "))
rate = float(input("Enter rate per hour: "))
pay = hours * rate
print(f"Your pay is: {pay}")

# --- Section 9: Lifespan Seconds Calculator ---
years = float(input("Enter number of years you have lived: "))
second = years * 365 * 24 * 60 * 60  # Days * Hours * Minutes * Seconds
print(f"You have lived for {second} seconds.")

max_years = 100
max_second = max_years * 365 * 24 * 60 * 60
print(f"If a person live to be {max_years} years ald, they will live for {max_second} seconds!")


# --- Section 10: Table Matrix Displays ---
print("1 1 1 1 1")
print("2 1 2 4 8")
print("3 1 3 9 27")
print("4 1 4 16 64")
print("5 1 5 25 125")

# Another way to do this is to pass separate number values with commas.
print(1, 1, 1, 1, 1)
print(2, 1, 2, 4, 8)
print(3, 1, 3, 9, 27)
print(4, 1, 4, 16, 64)
print(5, 1, 5, 25, 125)
