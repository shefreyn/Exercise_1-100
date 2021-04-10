print('__ Tip Calculator __')
totalBill = input('Total bill amount : ')
totalBill = int(totalBill)
percentage = input('Percentage you would like to tip : ')
percentage = int(percentage)
totalPeople = input('Total no of people you want to split the bill : ')
totalPeople = int(totalPeople)
tip = percentage/totalBill * 100
perPerson = totalBill/totalPeople
totalPerPerson = tip + perPerson
print(f"Each have to pay tip of {tip} and a bill amount of {perPerson} that is : {totalPerPerson}")