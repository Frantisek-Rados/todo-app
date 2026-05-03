from tasks import add_task, show_tasks, load_tasks, delete_task

load_tasks()

while True:
    print("\n1. Add task")
    print("2. Show tasks")
    print("3. Delete task")
    print("4. Exit")

    choice = input("Choose: ")

    if choice == "1":
        task = input("Enter task: ")
        add_task(task)

    elif choice == "2":
        show_tasks()

    elif choice == "3":
        show_tasks()
        try:
            index = int(input("Enter task number to delete: ")) - 1
            delete_task(index)
        except ValueError:
            print("Invalid input")

    elif choice == "4":
        break