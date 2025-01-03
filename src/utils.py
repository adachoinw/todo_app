import json

TASKS_FILE = "todo.json"


def load_tasks():
    """Load tasks from the todo.json file."""
    try:
        with open(TASKS_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_tasks(tasks):
    """Save tasks to the todo.json file."""
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)


def clear_tasks():
    """Clear all tasks from the todo.json file."""
    save_tasks([])


def get_task_count():
    """Return the number of tasks stored."""
    tasks = load_tasks()
    return len(tasks)
