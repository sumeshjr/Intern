def print_todo_list(todo_list):
    if not todo_list:
        print("Your to-do list is empty.")
    else:
        print("Your to-do list:")
        for index, task in enumerate(todo_list, start=1):
            print(f"{index}. {task}")

def add_task(todo_list, task):
    todo_list.append({"task": task, "completed": False})
    print(f"Task '{task}' added to your to-do list.")

def remove_task(todo_list, task_number):
    if 1 <= task_number <= len(todo_list):
        removed_task = todo_list.pop(task_number - 1)
        print(f"Task '{removed_task['task']}' removed from your to-do list.")
    else:
        print("Invalid task number.")

def mark_as_completed(todo_list, task_number):
    if 1 <= task_number <= len(todo_list):
        todo_list[task_number - 1]["completed"] = True
        print(f"Task marked as completed.")
    else:
        print("Invalid task number.")

# Example usage with user input:
my_todo_list = []

while True:
    print_todo_list(my_todo_list)

    user_choice = input("Do you want to add a task (A), remove a task (R), mark a task as completed (C), or quit (Q)? ").upper()

    if user_choice == "A":
        new_task = input("Enter the task: ")
        add_task(my_todo_list, new_task)
    elif user_choice == "R":
        task_to_remove = int(input("Enter the task number to remove: "))
        remove_task(my_todo_list, task_to_remove)
    elif user_choice == "C":
        task_to_mark = int(input("Enter the task number to mark as completed: "))
        mark_as_completed(my_todo_list, task_to_mark)
    elif user_choice == "Q":
        print("Quitting the to-do list.")
        break
    else:
        print("Invalid choice. Please enter A, R, C, or Q.")
        