#Write a code which gives grade to students according to theirs scores:

score = float(input("Enter the student's score (0 - 100): "))

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
