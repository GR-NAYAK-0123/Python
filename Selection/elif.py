
# Here I will be taking an input(score) of a student and according to that i will print the grade
# For this I will use "elif"

score = int(input("Enter your exam score : "))


if score >= 90 :
    print("You have secured O grade")

elif score >= 80 and score < 90 :
    print("You have secured A grade")

elif score >= 70 and score < 80 :
    print("You have secured B grade")

elif score >= 30 and score < 50 :
    print("You have secured C grade")

else :
    print("You have failed in the exam")