from tasks import add_task, view_tasks, complete_task, delete_task

def menu():
    print("\n--- Task Manager ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Exit")

while True:
    menu()
    choice = input("Choose an option: ")

    if choice == "1":
        task = input("Enter task: ")
        add_task(task)
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        index = int(input("Task number to complete: ")) - 1
        complete_task(index)
    elif choice == "4":
        index = int(input("Task number to delete: ")) - 1
        delete_task(index)
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice!")
