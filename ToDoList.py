# To Do List
def view_all_tasks(self):
        if not self.tasks:
            print("No tasks found.")
        else:
            print("All tasks:")
            for index, t in enumerate(self.tasks, start=1):
                status = "Completed" if t['completed'] else "Incomplete"
                print(f"{index}. {t['task']} - {status}")


def main():
    todo_list = TodoList()

    while True:
        print("\nTodo List Application")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Mark Task as Complete")
        print("4. View All Tasks")
        print("5. Exit")

        choice = input("Enter your choice: ")
