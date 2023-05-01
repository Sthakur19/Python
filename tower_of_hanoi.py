### Home Assignment --- Tower of hanoi ###
### Using recursive function of Python to achieve the results ###

### Importing in-built library of python to display time completion ###
import time

### This is the start time of code execution ###
start_time_of_execution = time.time()

### Defining the function with 4 parameters which include number of rods and disc ###
def tower_of_hanoi(numbers, start, middle, end):
    '''
    defining the project here with 4 parameters
    parameters "start", "middle", "end" represents numbers of rods and it's datatype is "str"
    parameters "numbers" represents disc and it's datatype is "int"
    '''
    ### Base case for Recursion ###
    if numbers == 1:
        print(f"1 {start} -> {end}")
        return

    ### Function calling itself ###
    tower_of_hanoi(numbers - 1, start, end, middle)

    print(f"{numbers} {start} -> {end}")
    
    ### Again function calling itself ###
    tower_of_hanoi(numbers - 1, middle, start, end)

### This refered as how many disc used ###
disc = 7

### Calculate the number of step ###
step = (2 ** disc) - 1

### Printing steps taken ###
print(f"Shortest solution is {step} steps:")

### Invoking the function here, A, B, C is referred as 3 rods ###
tower_of_hanoi(disc, "A", "B", "C")

### This is the end time of code execution ###
end_time_of_execution = time.time()

### This is the total time of code execution ###
total_execution_time = (end_time_of_execution - start_time_of_execution)

### Printing total time of code execution in milliseconds ###
print(f"Solution found in {round(total_execution_time * 1000, 6)}ms")


