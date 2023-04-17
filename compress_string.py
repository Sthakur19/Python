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