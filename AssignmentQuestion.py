math = int(input("Enter you Math marks"))
eng = int(input("Enter your English marks"))
hin = int(input("Enter your marks in Hindi: "))

avgrage = (math + eng + hin)/3


if (avgrage >= 80):
    print("You are a scholar ")

else:
    print("You failed")
