num_list = [1, 2, 3, 4, 5, 6, 7]

sq_num_list = []
for num in num_list:
    if num < 2:
        sq_num_list.append(num)

print(sq_num_list)

for value in map(lambda val: val ** 2, num_list):
    print(value)

mapped_list = list(map(lambda val: val ** 2, num_list))

print(list(filter(lambda val: len(val) == 1,
                  map(str,
                      map(lambda val: val ** 2, num_list)))))

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

for row in filter(lambda row: row['Gender'] == 'M' and row['City'] == 'London', students):
    print(row)

print('Avarage score ', sum(map(lambda row: row['Score'], students)) / len(students))



