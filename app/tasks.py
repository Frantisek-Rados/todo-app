tasks = []

def load_tasks():
    try:
        with open("tasks.txt", "r") as f:
            for line in f:
                tasks.append(line.strip())
    except FileNotFoundError:
        pass


def save_tasks():
    with open("tasks.txt", "w") as f:
        for task in tasks:
            f.write(task + "\n")


def add_task(task):
    tasks.append(task)
    save_tasks()


def show_tasks():
    for i, task in enumerate(tasks):
        print(f"{i+1}. {task}")


def delete_task(index):
    if 0 <= index < len(tasks):
        tasks.pop(index)
        save_tasks()
    else:
        print("Invalid task number")