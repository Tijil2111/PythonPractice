# Making new calculator using the new functions taught by Sunita Maam in school 



name = input("Hello, Please Enter your name: ")
print("Hello", name,"Welcome to the Mathematical calculator made by Tijil")


print("This is a Calculating machine which does every possible mathematical calculations")

print("This machine can add, subtract, multiply, divide, square, suare root, cube and cube roots")
num1 = float(input("Please Tell Your 1st Number: "))
num2 = float(input("Please Tell Your 2nd Number: "))


print("Press 1 for addition ")
print("Press 2 for subtraction ")
print("Press 3 for multiplication ")
print("Press 4 for division ")
print("Press 5 for square")
print("Press 6 for square root")
print("Press 7 for cube")
print("Press 8 for cube root")
operation = int(input("Tell your preference:"))


if operation == 1:
   print ("The sum is ", num1+num2)

elif operation == 2:
    print("The difference is", num1-num2)

elif operation ==3:
    print("The product is", num1*num2)

elif operation ==4:
    print("The division is", num1/num2)

elif operation ==5:
    print("The square of 1st no is", num1*num1)
    print("The suare of 2nd no is", num2*num2)

elif operation ==6:
    print("The square root of 1st no is", num1*0.5)
    print("The square root of 2nd no  is", num2*0.5)

elif operation ==7:
    print("The cube of 1st no is", num1*num1*num1)
    print("The cube of 2nd no  is", num2*num2*num1)

elif operation ==8:
    print("The cube root of 1st no is", num1 ** (1/3))
    print("The cube root of 2nd no  is",num2 ** (1/3))

else :
    print("Invalid Input")

