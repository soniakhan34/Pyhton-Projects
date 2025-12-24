#--------------------------To Do list Application Project-----------------------
#Create file2--------------
# file name..........(file2.py)

#-----------------Handle save loading data--------------------

def save(tasks, filename="tasks.json"):
    """Save tasks to a file."""

    try:
        with open(filename, "w") as file:
            for task in tasks:
                file.write(task["title"] + "\n")
        print("Tasks are saved successfully!")

    except Exception as e:
        print(f"Error saving tasks: {e}")


def load(filename="tasks.json"):
    """Load tasks from a file."""
    tasks = []

    try:
        with open(filename, "r") as file:
            for line in file:
                tasks.append({"title": line.strip(), "completed": False})
        print("Tasks are loaded successfully!")
        return tasks

    except FileNotFoundError:
        print("No file found. Starting with an empty list.")
        return []

    except Exception as e:
        print(f"Error loading tasks: {e}")
        return []
