# from functools import reduce

# # List and tuple
# my_list = [1,2,5,"a","d", [1,2,4]]

# my_tuple = (1,2,3,"a", "b", "c")

# add_list = (2,3,4)
# my_list.append(10)
# my_list.extend(my_tuple)
# print(my_list)

# # Function decorator

# def greet(fun):
#     def modified_function(*arg, **kwarg):
#         print("good morning")
#         fun(*arg, **kwarg)
#         print("Thanks")
#     return modified_function

# @greet
# def hello():
#     print("Hello word")

# @greet
# def add(a, b):
#     print(a + b)

# @greet
# def multiply(a, b):
#     print(a * b)

# hello()
# add(7,8)
# multiply(7,8)


# # Dic comprehension and list comprehension

# my_list = [2,3,4,5]

# my_list = [i for i in my_list if i >= 4]

# print(my_list)

# my_dic = {}

# my_dic = {i:f"item" for i in range(10) if i < 6}

# print(my_dic)

# # Generator and iterator

# def genratore():
#     for i in range(50):
#         yield i 
    
# gen = genratore()
# print(next(gen))
# print(next(gen))
# print(next(gen))

# # __init__ in Pyhton

# class PostIt:
#     def __init__(self, firstname, secondname, location):
#         self.firstname = firstname
#         self.secondname = secondname
#         self.location = location
    
#     def print_my_details(self):
#         print(f"{self.firstname} {self.secondname} {self.location}")

# obj1 = PostIt("swati", "Thakur" , "Raipur")
# obj2 = PostIt("sneha", "Thakur", "Hyde")

# obj1.print_my_details()
# obj2.print_my_details()


# # ternary oprator
# n=2
# print(True) if n == 1 else print(False)

# # Inheritance in python

# class Employee:
#     def __init__(self, id, name):
#         self.id = id
#         self.name = name

#     def print_details(self):
#         print(f"Employee detials {self.id} {self.name}")

# class Programmer(Employee):
#     def print_other_details(self):
#         print(f"She knows Java")

# emp1 = Employee("Swati", 20037552)
# emp2 = Programmer("Sneha", 20037553)

# emp1.print_details()
# emp2.print_details()

# emp2.print_other_details()


# # Continue, break and Pass

# for i in range(10):
#     if i == 7:
#         break
#     print(i, end=",")

# print("---")

# for i in range(10):
#     if i == 7:
#         continue
#     print(i, end=",")

# print("---") 
# # Map Filter and Reduce 
# my_list = [1,2,3,4,5]

# def cube(x):
#     return x*x*x

# my_new_list = list(map(cube , my_list))

# my_new_list_lambda = list(map(lambda x:x*x*x, my_list))
# print(my_new_list)
# print(my_new_list_lambda)


# my_new_filter_list = list(filter(lambda x: x > 2, my_list))
# print(my_new_filter_list)

# my_new_reduce_list = reduce(lambda x, y: x + y, my_list)


# morgan stnaly

def check_parentheses(expression):
    stack = []
    for char in expression:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                return False
            stack.pop()
              print("ll", stack)
    return not stack


# def check_parentheses(expression):
#     stack = ""
#     for char in range(0,len(expression)):
#         if char == '(':
#             stack += (char)
#         elif char == ')':
#             if len(stack) == 0:
#                 return False
#             stack.pop()
#             print("ll", stack)
#     return len(stack) == 0

# print(check_parentheses("((2+3)*4)/((5-1*2)"))