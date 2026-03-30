
print()

import array as arr
num = arr.array('i')
user_marks = int(input("Enter your student marks (minimum-20):- "))

print()

marks = []

for i in range(user_marks):
    m = int(input(f"Enter marks of student [{i+1}] = "))
    marks.append(m)

total_students = len(marks)
highest_marks = max(marks)
lowest_marks = min(marks)
average = sum(marks) / total_students

passed = sum(1 for m in marks if m >= 40)
failed = sum(1 for m in marks if m < 40)
pass_percentage = (passed / total_students) * 100

sorted_marks = sorted(marks)

A = B = C = D = E = F = 0

for m in marks:
    if m >= 90:
        A += 1
    elif m >= 80:
        B += 1
    elif m >= 70:
        C += 1
    elif m >= 60:
        D += 1
    elif m >= 40:
        E += 1
    else:
        F += 1

print()

print('-------------------------------------')

print("Total student:-", total_students)       
print("Highest marks:-", highest_marks)       
print("Lowest marks:-", lowest_marks)       
print("Average marks:-", average)
print("Passed:-", passed)
print("Failed:-", failed)
print("Pass percentage:-", pass_percentage ,"%")
print("Sorted Marks:-", sorted_marks)
print(f"Grade A: {A} Students")
print(f"Grade B: {B} Students")
print(f"Grade C: {C} Students")
print(f"Grade D: {D} Students")
print(f"Grade E: {E} Students")
print(f"Fail: {F} Students")

print('-------------------------------------')
