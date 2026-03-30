print('welcome to the Personal Data collector!')

print(  )

name = input('Enter Your Name :- ')
age = int(input('Enter Your Age :- '))
number = int(input('Enter Your Favourite Number :- '))
height = float(input('Enter Your Height in meters :- '))

print(  )

print('Thank you! Here is the information we collected:')

print(  )

print("Name:", name,end=" ")
print(("Type:"),type(name),end="")
print(",Memory Address:",id(name))

print("Age:", age,end=" ")
print(("Type:"),type(age),end="")
print(",Memory Address:",id(age))

print("Number:", number,end=" ")
print(("Type:"),type(number),end="")
print(",Memory Address:",id(number))

print("Height:", height,end=" ")
print(("Type:"),type(height),end="")
print(",Memory Address:",id(height))

print(  )

age_sum = 2025 - age
print(age_sum)

print(  )

print('Thank you for using the personal Data Collector. Goodbye!')

print(  )