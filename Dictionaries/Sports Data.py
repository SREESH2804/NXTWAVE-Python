students_dict = {
    "Ram": "Cricket",
    "Naresh": "Football",
    "Vani": "Tennis",
    "Rahim": "Cricket"
}

# Write your code here
a = int(input())
for i in range(a):
    b = input().split()
    students_dict[b[0]] = b[1]
print(students_dict)
