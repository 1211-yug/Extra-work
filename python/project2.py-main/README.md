# project2.py[project2.py](https://github.com/user-attachments/files/23325829/project2.py)
print()
print("Welcome to the Pattern Generator and Number Analyzer!")
print()
print("Select an option:")
print("1. Right-angled Triangle")
print("2. Pyramind")
print("3. Left-angled Triangle")
print("4. Analyze a Range of Numbers")
print('Instruction :- Please Enter The valid Choise For bettter Experience...!!')
print()
print()

choice=int(input("Enter your choice:-"))


if (choice == 1) or (choice ==2) or (choice ==3):
    rows = int(input("Enter the number of rows for the pattern:-"))

print()

if (choice == 1) or (choice ==2) or (choice ==3):
    print('Here is your pattern:-')
else:
    print('Here is the Analysis of your Given Range Number:-')

print()
print()


if choice == 1:
    for i in range(1,rows+1):
        for j in range (rows,i-1,-1):
            print(' ',end='')
        for k in range(1,i+1):
            print('*',end='')
        print()

elif choice == 2:
    for i in range(1,rows+1):
        for j in range(1,rows-i+1):
            print(' ',end='')
        for k in range(1,i+1):
            print('*',end=' ')
        print()

elif choice == 3:
    for i in range(1,rows+1):
        for k in range(1,i+1):
            print('*',end=' ')
        print()

elif choice == 4:
    srange = int(input("Enter the start of the range:-"))
    erange = int(input("Enter the end of the range:-"))
    sum = 0
    for i in range (srange,erange+1):
        sum = sum + i
        if i % 2 == 0:
            print('number', end='')
            print(i ,end='')
            print(' is even. ')
        else:
            print('number', end='')
            print(i,end='')
            print(' Is odd.')
    print()
    print('The sum of all numbers form ',end='')
    print(srange,end='')
    print(' to ',end='')
    print(erange,end='')
    print(' is ',sum)
else:
    print('Please EnterThe Valid choice ... !!')

print('Thank you...!!')
