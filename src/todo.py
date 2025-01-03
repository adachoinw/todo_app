import json

TASKS_FILE = "todo.json"


def load_tasks():
    try:
        with open(TASKS_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)


def add_task(task):
    tasks = load_tasks()
    tasks.append({"task": task, "done": False})
    save_tasks(tasks)
    print(f"Task added: {task}")


def list_tasks():
    tasks = load_tasks()
    for index, task in enumerate(tasks):
        status = "✔" if task["done"] else "✘"
        print(f"{index + 1}. {task['task']} - {status}")
