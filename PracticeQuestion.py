price = int(input("Please enter the price: "))
unit = int(input("Please enter the units: "))

total = price*unit

print("Now we will calculate the GST and Discount")

if(total >= 15000):
    discount = total*15/100
    gst = total*18/100
    print("The Net Amount is", total-discount+gst)

elif(total >= 10000 & total < 15000):
    discount = total*10/100
    gst = total*15/100
    print("The Net Amount is", total-discount+gst)

elif(total <= 10000):
    discount = total*5/100
    gst = total*10/100
    print("The Net Amount is", total-discount+gst)

else:
    print("Not applicable")
