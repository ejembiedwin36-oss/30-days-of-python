# Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. Output:

user_input = int(input("Enter you age: "))
if user_input >= 18:
    print("You are old enough to drive.")
else:
    print("You need 3 more years to learn to drive")


# Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age. Output:

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


# Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b. Output:

a = float(input("Enter number a: "))

b = float(input("Enter number b: "))

if a > b :
    print("a is greater than b")
elif a < b:
    print("a is lesser than b")
else:
    print("a is equal to b")