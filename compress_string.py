input_str = input("please enter String here :")

def string_compression(input_str):
    comp_str = ""
    count = 1
    for i in range(len(input_str)-1):
        if input_str[i] == input_str[i+1]:
            count += 1
        else:
            comp_str += input_str[i] + str(count)
            count = 1 
    comp_str += input_str[i] + str(count)
    return comp_str
    
print(string_compression(input_str))

# num = int(input("Please enter the number :"))

# def fizzbuzz(n):

#     for i in range(1, n):
#         if i % 3 == 0 and i % 5 == 0:
#             print("Fizz buzz")
#         elif i % 3 == 0:
#             print("Fizz")
#         elif i % 5 == 0:
#             print(" buzz")
#         else:
#             print(i)

# fizzbuzz(16)

# def fizzbuzz(n):
#     dict = {
#         3 : "Fizz",
#         5 : "Buzz"
#     }
#     for i in range(1, n):
#         result = ""
#         for key, value in dict.items():
#             if i % key == 0:
#                 result += value
#         if result == "":
#             result = i
#         print(result)

# fizzbuzz(16)