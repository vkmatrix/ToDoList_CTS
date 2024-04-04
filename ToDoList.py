# To Do List
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
      
