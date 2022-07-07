purchase = int(input("What is the value of the goods you have purchased: "))
discount = purchase*0.90
if purchase >= 1000:
    print("You have received a 10 percent discount. Please pay: ", discount)

else:
    print("You did not receive a discount.")    