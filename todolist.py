import json
from datetime import datetime, timedelta

class Todolist:
    def __init__(self):
        self.tasks_list = {}

    def add_task(self, task, days):
        due_date = datetime.now() + timedelta(days=days)
        self.tasks_list[task] = {
            "status": "Not Started",
            "created_on": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "due_date": due_date.strftime("%Y-%m-%d %H:%M"),
            "completed_on": None
        }
        print(f"Task '{task}' added.")

    def delete_task(self, task):
        if task in self.tasks_list:
            del self.tasks_list[task]
            print(f"Deleted Task - {task}")
        else:
            print("Task not found.")

    def mark_completed(self, task):
        if task in self.tasks_list:
            self.tasks_list[task]["status"] = "Completed"
            self.tasks_list[task]["completed_on"] = datetime.now().strftime("%Y-%m-%d %H-%M")
            print(f"Task {task} marked completed.")
        else:
            print("Task not found.")

    def search_tasks(self, *tasks):
        for task in tasks:
            if task in self.tasks_list:
                print(f"{task} - Task found.")
            else:
                print(f"{task} - Task not found.")

    def save_in_file(self):
        with open("file1.json", "w") as f:
            json.dump(self.tasks_list, f, indent=4)
        print("Tasks saved successfully.")

    def show_tasks(self):
        print("Current tasks:")
        for task, info in self.tasks_list.items():
            print(f"""
            Task - {task}
            Status - {info["status"]}
            Created on - {info["created_on"]}
            Due on - {info["due_date"]}
            Completed on - {info["completed_on"]}          
                 """)

t = Todolist()

while True:

    menu = """1. Add task \n2. Delete task \n3. Mark completed \n4. Search Tasks \n5. Show tasks \n6. Save in file \n7. Exit"""

    print(menu)

    try:
        selected_option = int(input("Enter Choice:"))
    except ValueError:
        print("Please enter a number")
        continue

    if selected_option == 1:
        task = input("Add a task: ")
        days = int(input("Add the no. of days required to complete the task: "))
        t.add_task(task, days)

    elif selected_option == 2:
        task = input("Which task needs to be deleted?: ")
        t.delete_task(task)

    elif selected_option == 3:
        task = input("Which task needs to be marked completed?: ")
        t.mark_completed(task)

    elif selected_option == 4:
        tasks = input("List the tasks to be searched separated by comma: ").split(", ")
        t.search_tasks(*tasks)

    elif selected_option == 5:
        t.show_tasks()

    elif selected_option == 6:
        t.save_in_file()

    elif selected_option == 7:
        break

    else:
        print("Invalid option")