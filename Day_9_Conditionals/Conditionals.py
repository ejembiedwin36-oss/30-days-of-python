# Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. Output:

user_input = int(input("Enter you age: "))
if user_input >= 18:
    print("You are old enough to drive.")
else:
    print("You need 3 more years to learn to drive")