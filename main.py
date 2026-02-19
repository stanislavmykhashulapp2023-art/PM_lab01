from tasks import TaskManager

def main():
    manager = TaskManager()

    while True:
        print("\n=== Task Manager ===")
        print("1. Add task")
        print("2. Show tasks")
        print("3. Remove task")
        print("4. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            title = input("Task title: ")
            manager.add_task(title)
            print("✅ Task added!")

        elif choice == "2":
            manager.show_tasks()

        elif choice == "3":
            manager.show_tasks()
            index = input("Enter task number to remove: ")
            manager.remove_task(index)

        elif choice == "4":
            print("Bye 👋")
            break

        else:
            print("❌ Wrong option!")

if __name__ == "__main__":
    main()
