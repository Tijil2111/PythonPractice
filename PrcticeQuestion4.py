
fare = int(input("Enter a base fare:"))
city = input("Enter the name of the city:")

if(city == "Delhi"):
    fare = fare + 10/100*fare
elif(city == "Mumbai"):
    fare = fare + 15/100*fare
else:
    fare = fare+20/100*fare


print("The fare is "+str(bf))
