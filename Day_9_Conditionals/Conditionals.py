# Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. Output:
"""
user_input = int(input("Enter you age: "))
if user_input >= 18:
    print("You are old enough to drive.")
else:
    print("You need 3 more years to learn to drive")
"""

my_age = int(input("Enter your age: "))

your_age = 10

if my_age > your_age:
    difference = my_age - your_age
    if difference == 1:
        print(f"You  are {difference} years older than me.")
    else:
        print(f"You  are {difference} years older than me.")

elif your_age > my_age:
    if difference == 1:
        print(f"I am {difference} year older than you.")
    else:
        print(f"I am {difference} year older than you.")

else:
    print("We are the exact same age! We are tech-twins.")

