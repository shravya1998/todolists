import os
import json
from datetime import datetime, timedelta

class Todolist:

    def __init__(self):
        self.tasks_list = {}

    def load_tasks_from_file(self):
        file_name = "tasks.json"
        if os.path.exists(file_name):
            try:
                with open("tasks.json", "r") as f:
                    self.tasks_list = json.load(f)
            except json.JSONDecodeError:
                print(f"Error decoding JSON from {file_name}. Initializing with an empty dict")
                self.tasks_list = {}

    def add_task(self, task, days):
        due_date = datetime.now() + timedelta(days=days)
        self.tasks_list[task] = {
            "status": "Not Started",
            "created_on": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "due_date": due_date.strftime("%Y-%m-%d %H:%M"),
            "over_due": None,
            "last_updated_on": datetime.now().strftime("%Y-%m-%d %H:%M")
        }
        print(f"Task '{task}' added.")

    def change_status(self, task, new_status):
        if task in self.tasks_list:
            if self.tasks_list[task]["status"] != new_status:
                self.tasks_list[task]["status"] = new_status
                self.tasks_list[task]["last_updated_on"] = datetime.now().strftime("%Y-%m-%d %H-%M")
                print(f"Task {task} marked as {new_status}.")
            else:
                print(f"Task {task} is already marked as {new_status}.")
        else:
            print("Task not found.")

    def mark_inprogress(self, task):
        self.change_status(task, "In Progress")

    def mark_completed(self, task):
        self.change_status(task, "Completed")

    def mark_overdue(self):
        for task, info in self.tasks_list.items():
            due_date = datetime.strptime(info["due_date"], "%Y-%m-%d %H:%M")
            if info["status"] != "Completed" and due_date < datetime.now():
                info["over_due"] = "YES - TAKE ACTION NOW!!!!!"
            else:
                info["over_due"] = "NO"

    def delete_task(self, task):
        if task in self.tasks_list:
            del self.tasks_list[task]
            print(f"Deleted Task - {task}")
        else:
            print("Task not found.")

    def search_tasks(self, *tasks):
        for task in tasks:
            if task in self.tasks_list:
                print(f"{task} - Task found.")
            else:
                print(f"{task} - Task not found.")

    def save_in_file(self):
        with open("tasks.json", "w") as f:
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
            Over Due - {info["over_due"]}
            Updated Status on - {info["last_updated_on"]}          
                 """)

t = Todolist()
t.load_tasks_from_file()

while True:

    menu = """1. Add task \n2. Delete task \n3. Mark In progress \n4. Mark completed \n5. Search Tasks \n6. Show tasks \n7. Exit"""

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
        task = input("Which task needs to be marked in progress?: ")
        t.mark_inprogress(task)

    elif selected_option == 4:
        task = input("Which task needs to be marked completed?: ")
        t.mark_completed(task)

    elif selected_option == 5:
        tasks = input("List the tasks to be searched in a comma separated way: ").split(", ")
        t.search_tasks(*tasks)

    elif selected_option == 6:
        t.mark_overdue()
        t.show_tasks()

    elif selected_option == 7:
        t.save_in_file()
        break

    else:
        print("Invalid option")