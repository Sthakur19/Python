import argparse

# Define the command-line arguments
parser = argparse.ArgumentParser()
parser.add_argument("-l", "--list", help="List all the tasks", action="store_true")
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

# Define a function to print the tasks
def print_tasks(tasks):
    if tasks:
        for i, task in enumerate(tasks, 1):
            print(f"{i} - {task}")
    else:
        print("No todos for today! :)")

# Define the main function
def main():
    if args.list:
        tasks = read_tasks()
        print_tasks(tasks)

        

# Run the application
if __name__ == "__main__":
    main()
