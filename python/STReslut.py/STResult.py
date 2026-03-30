print()
print('welcome to student result potal')
print()

name = input('Enter a student name :-')

print()
print('Enter your student all subject marks below :-')
print()

sub1 = int(input('Gujrati = '))
sub2 = int(input('English = '))
sub3 = int(input('Maths = '))
sub4 = int(input('Science = '))
sub5 = int(input('Social Studies = '))
marks = [sub1, sub2, sub3, sub4, sub5]
total = 0
for i in marks:
    total += i
print()

a = [sub1, sub2, sub3, sub4, sub5]

max_marks = max(a)
print('Maximum Marks =', max_marks)

min_marks = min(a)
print('Minimum Marks =', min_marks)

avg = sum(a) / len(a)
print('Student Name :-', name)
print('Average Marks =', avg)
print('Total Marks =', total)
percentage = (total / 500) * 100
print('Percentage =', percentage)

if percentage >= 90:
    print('Grade = A+')
elif percentage >= 80:
    print('Grade = A')
elif percentage >= 70:
    print('Grade = B+')
elif percentage >= 60:
    print('Grade = B')
elif percentage >= 50:
    print('Grade = C')
else:
    print('Grade = F')

print()
print('Thank you for using student result portal')
print()
