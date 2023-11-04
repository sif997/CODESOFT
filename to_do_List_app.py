class Task:
    def __init__(self, name, description, due_date, priority):
        self.name = name
        self.description = description
        self.due_date = due_date
        self.priority = priority

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def delete_task(self, task_name):
        for task in self.tasks:
            if task.name == task_name:
                self.tasks.remove(task)

    def mark_task_as_complete(self, task_name):
        for task in self.tasks:
            if task.name == task_name:
                task.is_complete = True

    def print_to_do_list(self):
        print("To-Do List:")
        for task in self.tasks:
            print(f"{task.name} ({task.priority})")

def main():
    to_do_list = ToDoList()

    while True:
        print("What do you want to do?")
        print("1. Add a task")
        print("2. Delete a task")
        print("3. Mark a task as complete")
        print("4. Print to-do list")
        print("5. Exit")

        choice = input("Your choice: ")

        if choice == "1":
            task_name = input("Task name: ")
            task_description = input("Task description: ")
            task_due_date = input("Task due date: ")
            task_priority = input("Task priority: ")

            task = Task(task_name, task_description, task_due_date, task_priority)
            to_do_list.add_task(task)
        elif choice == "2":
            task_name = input("Task name to delete: ")
            to_do_list.delete_task(task_name)
        elif choice == "3":
            task_name = input("Task name to mark as complete: ")
            to_do_list.mark_task_as_complete(task_name)
        elif choice == "4":
            to_do_list.print_to_do_list()
        elif choice == "5":
            break

if __name__ == "__main__":
    main()
