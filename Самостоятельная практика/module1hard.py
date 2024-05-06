grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]

students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

new_grades = []

students = sorted(students)

result = {}

def gpa():
    for i in grades:
        nums = (sum(i) / len(i))
        new_grades.append(nums)
    global result
    result = dict(zip(students, new_grades))

gpa()
print(result)