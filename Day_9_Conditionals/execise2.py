#Write a code which gives grade to students according to theirs scores:

"""score = float(input("Enter the student's score (0 - 100): "))

if score >= 90 and score <= 100:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
elif score >= 0:
    print("Grade: C")
else:
    print("Invalid score! Please enter a value between 0 and 100.")

"""
# Get the month from user input then check if the season is Autumn, Winter, Spring or Summer. If the user input is: September, October or November, the season is Autumn. December, January or February, the season is Winter. March, April or May, the season is Spring June, July or August, the season is Summer
#The following list contains some fruits:
month = input("|Enter a month: ").capitalize()

if month in ["September", "October", "November"]:
    print("The season is Authumn")
elif month in ["December", "January", "February"]:
    print("The season is Winter.")
elif month in ["March", "April", "May"]:
    print("The season is Spring.")
elif month in ["June", "July", "August"]:
    print("The season is Summer.")
else:
    print("Invalid month! Please check your spelling and try again.")

