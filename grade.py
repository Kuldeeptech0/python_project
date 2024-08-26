markes = int(input("Enter the markes (0 to 100): "))
if markes >= 90:
    grade = "excellent"
elif markes >= 80:
    grade = "A++"
elif markes >= 70:
    grade = "B"
elif markes >= 60:
    grade = "C"
elif markes >= 50:
    grade = "D"
else:
    grade = "FAIL"
print("YOUR GRADE IS : " + grade)