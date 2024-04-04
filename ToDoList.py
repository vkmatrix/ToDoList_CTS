# To Do List
class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({'task': task, 'completed': False})
        print("Task added successfully.")
    def remove_task(self, task):
            for t in self.tasks:
                if t['task'] == task:
                    self.tasks.remove(t)
                    print("Task removed successfully.")
                    return
            print("Task not found.")
    
        def mark_task_as_complete(self, task):
            for t in self.tasks:
                if t['task'] == task:
                    t['completed'] = True
                    print("Task marked as complete.")
                    return
            print("Task not found.")
    
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
    
            if choice == '1':
                task = input("Enter the task: ")
                todo_list.add_task(task)
            elif choice == '2':
                task = input("Enter the task to remove: ")
                todo_list.remove_task(task)
            elif choice == '3':
                task = input("Enter the task to mark as complete: ")
                todo_list.mark_task_as_complete(task)
            elif choice == '4':
                todo_list.view_all_tasks()
            elif choice == '5':
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")
    
    
    if __name__ == "__main__":
        main()
    
    
          
