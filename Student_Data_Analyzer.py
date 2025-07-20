"""
Date: 16/07/2025
Time: pass
topic: Student Data Analyzer
"""

roll_n = []
names = []
marks = []


def take_student_info():
    roll = int(input("Enter roll number :: "))
    name = input("Enter student name :: ")
    mark = int(input("Enter marks :: "))

    roll_n.append(roll)
    names.append(name)
    marks.append(mark)

def combine():
    combined_info = list(zip(roll_n,names,marks))
    return combined_info

def add_serial_num(combined_std):
    students_with_serial_num = list(enumerate(combined_std,start=1))
    return students_with_serial_num

def filter_pass_std(combined_std):
    passed = list(filter(lambda x:x[2] >= 40, combined_std))
    return passed
    # print(combined_std[])


while True:
    print("1.insert, 2.list, 3.serial, 4.passed.\n")
    flag = int(input("Enter your choic :: "))

    if(flag == 0):
        break
    elif(flag == 1):
        take_student_info()
    elif(flag == 2):
        std = combine()
        print(std)
    
    elif(flag == 3):
        std = combine()
        serial = add_serial_num(std)
        for i, (r,n,m) in serial:
            print(f"{i}. Roll no :: {r}, Name :: {n}, Marks :: {m}.")
    
    elif(flag == 4):
        std = combine()
        print(filter_pass_std(std))
    else:
        print("Invalid input!")