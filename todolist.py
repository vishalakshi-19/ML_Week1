import json
import os

TODO_FILE = "todo.json"

def load_tasks():
    if not os.path.exists(TODO_FILE):
        return []
    with open(TODO_FILE, "r") as file:
        return json.load(file)

def save_tasks(tasks):
    with open(TODO_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

def show_tasks(tasks):
    if not tasks:
        print("📭 No tasks found.")
        return
    print("\n📋 Your To-Do List:")
    for i, task in enumerate(tasks, 1):
        status = "✔️" if task["completed"] else "❌"
        print(f"{i}. [{status}] {task['title']}")

def add_task(title):
    tasks = load_tasks()
    tasks.append({"title": title, "completed": False})
    save_tasks(tasks)
    print(f"✅ Task '{title}' added.")

def complete_task(index):
    tasks = load_tasks()
    try:
        tasks[index - 1]["completed"] = True
        save_tasks(tasks)
        print("✅ Task marked as completed.")
    except IndexError:
        print("❗ Invalid task number.")

def delete_task(index):
    tasks = load_tasks()
    try:
        removed = tasks.pop(index - 1)
        save_tasks(tasks)
        print(f"🗑️ Task '{removed['title']}' deleted.")
    except IndexError:
        print("❗ Invalid task number.")

def menu():
    while True:
        print("\n====== To-Do CLI Menu ======")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            show_tasks(load_tasks())
        elif choice == "2":
            title = input("Enter task description: ")
            add_task(title)
        elif choice == "3":
            index = int(input("Enter task number to complete: "))
            complete_task(index)
        elif choice == "4":
            index = int(input("Enter task number to delete: "))
            delete_task(index)
        elif choice == "5":
            print("👋 Exiting To-Do CLI. Goodbye!")
            break
        else:
            print("❗ Invalid choice. Please try again.")

if __name__ == "__main__":
    menu()
