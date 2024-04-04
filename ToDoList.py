# To Do List

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

