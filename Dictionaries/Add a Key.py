students_dict = {
    "Ram": "Cricket",
    "Naresh": "Football",
    "Vani": "Tennis",
    "Rahim": "Cricket"
}

# Write your code here
a = input().split()
students_dict[a[0]] = a[1]
print(students_dict)
