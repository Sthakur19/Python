import argparse

# Define the command-line arguments
parser = argparse.ArgumentParser()
parser.add_argument("-l", "--list", help="List all the tasks", action="store_true")
parser.add_argument("-a", "--add", help="Add a new task")
args = parser.parse_args()

# Define the file where tasks are stored
TODO_FILE = "tasks.txt"

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

# Define a function to print the tasks
def print_tasks(tasks):
    if tasks:
        for i, task in enumerate(tasks, 1):
            print(f"{i} - {task}")
    else:
        print("No todos for today! :)")

# Define the main function
def main():
    tasks = read_tasks()
    if args.add:
        tasks.append(args.add)
        write_tasks(tasks)
        print(f"Added task: {args.add}")
    elif args.list:
        print_tasks(tasks)

# Run the application
if __name__ == "__main__":
    main()
