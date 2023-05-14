from itertools import groupby

students = [
    {'Name': 'Alice', 'Age': 25, 'Gender': 'F', 'City': 'Tokyo', 'Score': 80},
    {'Name': 'Bob', 'Age': 30, 'Gender': 'M', 'City': 'New York', 'Score': 90},
    {'Name': 'Charlie', 'Age': 20, 'Gender': 'M', 'City': 'London', 'Score': 85},
    {'Name': 'David', 'Age': 27, 'Gender': 'M', 'City': 'San Francisco', 'Score': 95},
    {'Name': 'Eve', 'Age': 22, 'Gender': 'F', 'City': 'Paris', 'Score': 75},
    {'Name': 'Frank', 'Age': 35, 'Gender': 'M', 'City': 'Sydney', 'Score': 70},
    {'Name': 'Grace', 'Age': 28, 'Gender': 'F', 'City': 'Tokyo', 'Score': 88},
    {'Name': 'Harry', 'Age': 24, 'Gender': 'M', 'City': 'New York', 'Score': 92},
    {'Name': 'Isabelle', 'Age': 29, 'Gender': 'F', 'City': 'Paris', 'Score': 83},
    {'Name': 'Jack', 'Age': 32, 'Gender': 'M', 'City': 'London', 'Score': 87}
]

sorted_by_city = sorted(students, key=lambda row: row['City'])
for city, students in groupby(sorted_by_city, lambda row: row['City']):
    student_list = list(students)
    print(city, sum(map(lambda row: row['Score'], student_list)) / len(student_list), len(student_list))

for line in map(lambda row: {'Name': row['Name'], 'Age': row['Age']}, students):
    print(line)
