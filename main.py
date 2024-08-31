import os

# File to store tasks
TASKS_FILE = 'tasks.txt'

# Function to load tasks from the file
def load_tasks():
    tasks = []
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as file:
            for line in file:
                task, completed = line.strip().split('|')
                tasks.append({'task': task, 'completed': completed == 'True'})
    return tasks

# Function to save tasks to the file
def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as file:
        for task in tasks:
            file.write(f"{task['task']}|{task['completed']}\n")

# Function to add a task
def add_task(tasks, task):
    tasks.append({'task': task, 'completed': False})
    save_tasks(tasks)
    print(f"Task '{task}' added to the list.")

# Function to view all tasks
def view_tasks(tasks):
    if tasks:
        print("Your tasks:")
        for i, task in enumerate(tasks, start=1):
            status = "Completed" if task['completed'] else "Not Completed"
            print(f"{i}. {task['task']} [{status}]")
    else:
        print("No tasks in the list.")

# Function to delete a task
def delete_task(tasks, task_number):
    if 0 < task_number <= len(tasks):
        removed_task = tasks.pop(task_number - 1)
        save_tasks(tasks)
        print(f"Task '{removed_task['task']}' removed from the list.")
    else:
        print("Invalid task number.")

# Function to mark a task as completed
def complete_task(tasks, task_number):
    if 0 < task_number <= len(tasks):
        tasks[task_number - 1]['completed'] = True
        save_tasks(tasks)
        print(f"Task '{tasks[task_number - 1]['task']}' marked as completed.")
    else:
        print("Invalid task number.")

# Main program loop in a function (Kaggle notebooks execute cells individually)
def main():
    tasks = load_tasks()
    while True:
        print("\nTo-Do List Menu:")
        print("1. Add a task")
        print("2. View tasks")
        print("3. Delete a task")
        print("4. Mark a task as completed")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            task = input("Enter the task: ")
            add_task(tasks, task)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            view_tasks(tasks)
            try:
                task_number = int(input("Enter the task number to delete: "))
                delete_task(tasks, task_number)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == "4":
            view_tasks(tasks)
            try:
                task_number = int(input("Enter the task number to mark as completed: "))
                complete_task(tasks, task_number)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == "5":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

# Call the main function to run the program
if __name__ == "__main__":
    main()
