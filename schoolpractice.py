price = int( input("Please tell the Price of the product: "))
units = int(input("Please tell us the Units sold: "))
totalamount = price*units
discount = totalamount*10/100 

print("We will now calculate the total amount, Discount and Net Amount Payable")

print("Total amount payable is", totalamount)
print("TOtal discount is",discount )
print("Net Amount Payable is", totalamount-discount)