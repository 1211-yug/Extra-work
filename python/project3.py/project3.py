print()
print('Welcome to the Student Data Organizer!')
print()
print()

st = []
sid = 1
while True:
    print()
    print('Select an option:')
    print('|---------------------------------|')
    print('| 1. Add Student                  |')
    print('| 2. Display All Students         |')
    print('| 3. Update Student Name          |')
    print('| 4. Update Student Age           |')
    print('| 5. Update Student Grade         |')
    print('| 6. Delete Student               |')
    print('| 7. Display Subjects Offered     |')
    print('| 8. Exit                         |')
    print('|---------------------------------|')

    choice = int(input('Enter your choice(1-6):-'))
    print()

    if (choice == 1):
        print('Enter student details:')
        print('Student ID:- ', sid)
        name = input('Name:- ')
        age = int(input('Age:- '))
        grade = input('Grade:- ')
        dob = input('Date of Birth (YYYY-MM-DD):- ')
        Sub = input('Subjects (comma-seprated):- ')

        student = {'sid':sid, 'name':name, 'age':age, 'grade':grade, 'dob':dob, 'sub':Sub }
        st.append(student)
        sid = sid+1


    elif(choice == 2):

        print('Display All Students')

        print("Sid    |Name       |Age      |Grade      |Date of brith            |Subjects       ")
        print('--------------------------------------------------------------------------------------')
        for s in st:
            print(f"{s['sid']}      |{s['name']}        |{s['age']}      |{s['grade']}       |{s['dob']}         |{s['sub']}")


    elif(choice == 3):

        usid = int(input("Enter your student ID :- "))

        for i in st:
            if (i['sid'] == usid):
                student['name'] = input("Enter your update name :-")
            break

        print("Update name of students for successfully...")

    elif (choice == 4):
        
        usid = int(input("Enter your student ID :- "))

        for i in st:
            if (i['sid'] == usid):
                student['age'] = int(input("Enter your update of  age :-"))
            break

        print("Update age of students for successfully...")

    elif (choice == 5):
        
        usid = int(input("Enter your student ID :- "))
        
        for i in st:
            if (i['sid'] == usid):
                student['grade'] = input("Enter your update student Grade:-")
            break

        print("Update  Grade of students for successfully...")

    elif(choice == 6):

        delete = int(input('Enter Your Delete Student ID:-'))

        for d in st:
            if d ["sid"] == delete:
                st.remove(d)
                print('Student Remove successfully !')
                break
        else:
            print('Student not found !') 

    elif(choice == 7):

        print('---------Display Subjects Offered----------')

        print('English,Hindi,Gujrati....')

    else:
        print('Thank the user for using the Student Data Organizer and displaying an exit message.')