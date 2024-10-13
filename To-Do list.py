# Task 1
# Command-line To-Do List Application

# Task list to store all the tasks
tasks = []

# Function to display all tasks
def show_tasks():
    if len(tasks) == 0:
        print("No tasks found!")
    else:
        print("\nTo-Do List:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

# Function to add a new task
def add_task():
    task = input("Enter the task: ")
    tasks.append(task)
    print(f"Task '{task}' added successfully!")

# Function to update a task
def update_task():
    show_tasks()
    task_no = int(input("Enter the task number to update: "))
    if 0 < task_no <= len(tasks):
        updated_task = input("Enter the new task: ")
        tasks[task_no - 1] = updated_task
        print(f"Task {task_no} updated successfully!")
    else:
        print("Invalid task number!")

# Function to delete a task
def delete_task():
    show_tasks()
    task_no = int(input("Enter the task number to delete: "))
    if 0 < task_no <= len(tasks):
        removed_task = tasks.pop(task_no - 1)
        print(f"Task '{removed_task}' deleted successfully!")
    else:
        print("Invalid task number!")

# Main function to run the application
def todo_list():
    while True:
        print("\nOptions:")
        print("1. Show Tasks")
        print("2. Add Task")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            show_tasks()
        elif choice == '2':
            add_task()
        elif choice == '3':
            update_task()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            print("Exiting To-Do List Application. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

# Run the To-Do List application
todo_list()
