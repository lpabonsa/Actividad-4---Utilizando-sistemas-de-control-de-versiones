class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def show_tasks(self):
        if not self.tasks:
            print("No hay tareas en la lista.")
        else:
            print("\n=== Tareas ===")
            for i, task in enumerate(self.tasks, 1):
                print(f"{i}. {task}")
