import sys

# Define the file where tasks are stored
TODO_FILE = "tasks.txt"

def print_usage():
    print("""
Command Line Todo application
=============================

Command line arguments:
    -l   Lists all the tasks
    -a   Adds a new task
    -r   Removes an task
    -c   Completes an task
    """)

# the application is ran with `-l` argument
if len(sys.argv) != 2 or sys.argv[1] != '-l':
    print_usage()
    sys.exit(1)

try:
    with open(TODO_FILE, 'r') as file:
        tasks = file.readlines()

    if not tasks:
        '''Empty list = - **When** the application is ran with `-l` argument
        - **Then** it should show a message like this: `No todos for today! :)`'''
        print('No todos for today! :)')
    else:
        '''List tasks == it should print the tasks that are stored in the file
        And it should add numbers before each'''
        for i, task in enumerate(tasks):
            print(f'{i+1} - {task.strip()}')

except FileNotFoundError:
    print('No tasks file found.')

if __name__ == '__main__':
    if len(sys.argv) == 1:
        print_usage()

