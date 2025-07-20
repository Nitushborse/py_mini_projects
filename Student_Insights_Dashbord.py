"""
Date: 18/07/2025
Time: pass
topic: Student insughts Dashbord
"""

import pprint as pp

raw_names = ["BHavesh", "chEtan ", "PRAKASH", "  praful  ", "rakesh"]
cpp_marks = [57,46,47,48,13]
java_marks = [34,47,58,16,23]


clean_names = list(name.strip().title() for name in raw_names)

rolls = list(range(1,1+len(clean_names)))

# students = [(rolls[i], clean_names[i], cpp_marks[i], java_marks[i]) for i in range(len(clean_names))]
students = list(zip(rolls,clean_names,cpp_marks,java_marks))

pp.pprint(students)

def get_roll_name_map(students):
    mapped = {item[0]: item[1] for item in students}
    m = {roll: name for roll, name, _, _ in students}
    return mapped

print(get_roll_name_map(students))

def count_pass_fail(students):
    count = list(filter( lambda x: (x[2] +x[3])/2 >= 24, students))
    print(len(count))

count_pass_fail(students)

def get_subject_top(students):
    max = None
    for i in range(len(students)):
        if students[i][3] > students[i+1][3]:
            max = i

    


