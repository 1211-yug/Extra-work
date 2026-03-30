
print()
print("Welcome To CRUD System.")
print()
print()

st = []
uid = 1

while True:

    print("press 1 for add create student.")
    print("press 2 for add view students.")
    print("press 3 for add edit age of student.")
    print("press 4 for add edit course of student.")
    print("press 5 for remove student.")
    print("press 6 for exit student.")
    print()
    print()

    choice = int(input("Enter your choice (1-5):"))

    if (choice == 1):

        name = input("Enter your name :- ")
        age = int(input("Enter your age :- "))
        course = input("Enter your Course :-")
        
        student = {"uid":uid, "name":name, "age":age, "course":course}
        st.append(student)
        uid = uid+1

        print('---------------------------------')
        print()

    elif (choice == 2):

        print("ID    | Name    | Age   | Course    ")
        print('------------------------------------')
        for i in st:
            print (f"{i['uid']}     |{i['name']}     |{i['age']}     |{i['course']}")

    elif (choice == 3):
        
        usid = int(input("Enter your age of student :- "))
        for i in st:
            if (i['uid'] == usid):
                student['age'] = int(input("Enter you edit age :-"))
            break

        print("Edit age of  students for successfully...")

    elif (choice == 4):
        
        usid = int(input("Enter your course of student :- "))
        for i in st:
            if (i['uid'] == usid):
                student['course'] = input("Enter you edit course :-")
            break

        print("Edit age of  students for successfully...")


    elif (choice == 5):

        sid=int(input("Enter Your Delete student ID:-"))
        
        for s in st :
            if s["uid"] == sid:
                st.remove(s)
                print("Student remove successfully !")
                break
        else:       
            print("student not found ! ")

    elif (choice == 6):

        print("Exit students")
        break
    else:
        print("please enter your valid number")