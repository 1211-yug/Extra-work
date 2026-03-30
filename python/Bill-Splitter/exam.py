
print('Welcome to the Bill Splitter App!')
print()

bill_amount=(float(input('Enter total bill amount:')))
people=(int(input('Enter number of people:')))
tip=(int(input('Enter tip percentage (0/5/10/15/20):')))

print()
Amount=(input(tip/100*bill_amount))
print('Tip Amount:-',Amount)

fbill=(input(bill_amount + Amount))
print('Total Bill (with Tip):- ',fbill)

per_person=(input(fbill/people))
print('Each person Should pay:- ',per_person)


print()
print('would you like to calculate another bill? (y/n): ')
print('...')