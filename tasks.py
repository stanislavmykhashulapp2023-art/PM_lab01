from storage import save_tasks, load_tasks

class TaskManager:
    def __init__(self):
        self.tasks = load_tasks()

    def add_task(self, title: str):
        self.tasks.append(title)
        save_tasks(self.tasks)

    def show_tasks(self):
        if not self.tasks:
            print("No tasks yet.")
            return

        print("\nYour tasks:")
        for i, task in enumerate(self.tasks, start=1):
            print(f"{i}. {task}")

    def remove_task(self, index):
        try:
            index = int(index) - 1
            removed = self.tasks.pop(index)
            save_tasks(self.tasks)
            print(f"🗑 Removed: {removed}")
        except:
            print("❌ Invalid number!")
