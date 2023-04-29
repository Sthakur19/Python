import sys

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

if __name__ == '__main__':
    if len(sys.argv) == 1:
        print_usage()

