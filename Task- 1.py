d = {}
n = int(input("Enter number of students:"))
for i in range(n):
    name = input("Enter name:")
    marks = int(input("Enter marks:"))
    d[name] = marks

found = False
_name = input("Enter the student's name:")
for i in d:
    if i == _name:
        print(f"{i}'s marks: {d[i]}")
        found = True

if (found == False):
    print("Student not found")

