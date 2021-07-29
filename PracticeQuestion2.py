# Program to calculate grade on basis of the Percentage

percentage = float(input("Enter your percentage: "))


if(percentage >= 90.0):
    print("Your grade is A")

elif(percentage >= 80.0 & percentage < 90.0):
    print("Your grade is B")


elif(percentage >= 70.0 & percentage < 80.0):
    print("Your grade is C")

elif(percentage >= 60.0 & percentage < 70.0):
    print("Your grade is D")

else:
    print("You are falied in exmas. Concentrate on your studies")
