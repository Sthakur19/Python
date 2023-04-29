import sys

# Define the file where tasks are stored
TODO_FILE = "tasks.txt"


# Read the command line arguments
args = sys.argv

# Check if the correct number of arguments were provided
if len(args) != 3:
    print("Usage: python app.py -c <task_number>")
    sys.exit()

# Parse the task number from the command line arguments
try:
    task_number = int(args[2])
except ValueError:
    print("Invalid task number")
    sys.exit()

# Open the data file and read the tasks
with open(TODO_FILE, "r") as f:
    tasks = f.readlines()

# Check if the requested task number is valid
if task_number < 1 or task_number > len(tasks):
    print("Invalid task number")
    sys.exit()

# Print the requested task
print(tasks[task_number-1])

# Remove the second task if it exists
if len(tasks) >= 2:
    task_index = int(sys.argv[2]) - 1  # Convert the argument to 0-based index
    if task_index >= 0 and task_index < len(tasks):
        del tasks[task_index]

# Define a function to read the tasks from the file
def read_tasks():
    tasks = []
    with open(TODO_FILE, "r") as f:
        for line in f:
            tasks.append(line.strip())
    return tasks

# Define a function to write tasks to the file
def write_tasks(tasks):
    with open(TODO_FILE, "w") as f:
        for task in tasks:
            f.write(task + "\n")

with open(TODO_FILE, 'w') as f:
    f.writelines(tasks)

# Define a function to print the tasks
def print_tasks_fun(tasks):
    if tasks:
        for i, task in enumerate(tasks, 1):
            print(f"{i} - {task}")
    else:
        print("No todos for today! :)")

# Define the main function
def main():
    tasks = read_tasks()
    if sys.argv[1] == "-l":
        print_tasks_fun(tasks)
    if sys.argv[1] == "-a":
        tasks.append(sys.argv[2])
        write_tasks(tasks)
        print(f"Added task: {sys.argv[2]}")

### Argument error handling
if len(sys.argv) != 2 or sys.argv[1] not in ['-a', '-r']:
    sys.stderr.write('Unsupported argument\n')
    sys.stderr.write('Usage: python program.py [-a|-r] <task>\n')
    sys.exit(1)
# Add new task error handling
if len(sys.argv) == 2 and sys.argv[1] == "-a":
    print("Unable to add: no task provided", file=sys.stderr)

### Remove task error handling
if len(sys.argv) == 2 and sys.argv[1] == '-r':
    print('Unable to remove: no index provided', file=sys.stderr)    

# Run the application
if __name__ == "__main__":
    main()
