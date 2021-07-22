price = int(input("Please enter the price: "))
unit = int(input("Please enter the units: "))

total = price*unit

print("Now we will calculate the Net Amount Payable")

if(total >= 15000):
    discount = total*15/100
    gst = total*18/100

elif(total >= 10000 & total < 15000):
    discount = total*10/100
    gst = total*15/100

elif(total <= 10000):
    discount = total*5/100
    gst = total*10/100

else:
    print("Not applicable")


print("GST IS", gst)
print("Discount is", discount)
nap = total-discount+gst
print("The Net Amount is", total-discount+gst)
