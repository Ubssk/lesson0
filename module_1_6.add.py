grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students_list = list(students)
gpa = []
i=0
while i < len(grades):
    gpa.append(sum(grades[i]) / len(grades[i]))
    i = i + 1
#dict_students = dict(zip(students_list, gpa))
#print(dict_students)
print(dict(zip(students_list, gpa)))