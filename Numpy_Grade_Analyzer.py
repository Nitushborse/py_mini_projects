import numpy as np

data = np.array([[40,56,35],
                 [46,50,43],
                 [52,39,57]])

total_marks = np.sum(data,axis=1)

avg_marks = np.average(data, axis=1)

mask = data >= 40
data[mask] = data[mask] + 5
max_marks = np.max(data, axis=0)


print("-------------------student data analyzer-----------------")
print(f"topers : {max_marks}")
for i in range(3):
    print(f"student {i + 1} data: total marks: {total_marks[i]}, average marks: {avg_marks[i]:.2f},  updated marks: {(data[i])}")