print()

# que 1. largest number in array.

import array as arr

print()

numbers = arr.array('i')
n = int(input("Enter value of number:- "))

for i in range(n):
    value  = int(input(f"Enter a value in numbers:- [{i}] = "))
    numbers.append(value)

largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

print()

print("larest number in array is :", largest)

print()
print('-----------------------------------------------------')
print()

# que 2. lenth of array.

import array as arr

print()

numbers = arr.array('i')
n = int(input("Enter value of number:- "))

for i in range(n):
    value  = int(input(f"Enter a value in numbers:- [{i}] = "))
    numbers.append(value)

length = 0

for a in numbers:
    length += 1

print()

print("length of array is :", length)

print()
print('-----------------------------------------------------')
print()

# que 3. Average of 1D Array without Using Built-in Functions.

import array as arr

print()

numbers =  arr.array('i')
num = int(input('Enter value of numbers:- '))

for i in range(num):
    value = int(input(f'Enter a value in numbers:- [{i}] = '))
    numbers.append(value)

total = 0

for n in numbers:
    total += n
average = total / num

print()

print('Average of 1D Array is :-', average)

print()

print('-----------------------------------------------------')

print()

# que 4. Addition of two 1D arrays and store into array C

import array as arr

print()
numberA = arr.array('i')
numberB = arr.array('i')
numberC = arr.array('i')

numA = int(input(f'Enter value of number A :- '))
numB = int(input(f'Enter value of number B :- '))

for i in range(numA):
    numberA.append(int(input(f'Enter a value in numbers:- [{i}] = ')))

for i in range(numB):
    numberB.append(int(input(f'Enter a value in numbers:- [{i}] = ')))

for i in range(min(numA, numB)):
    numberC.append(numberA[i] + numberB[i])

print('\nArray C is:', numberC)
