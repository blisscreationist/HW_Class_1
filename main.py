class Task:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, deadline):
        task = {'description': description, 'deadline': deadline, 'status': 'Не выполнено'}
        self.tasks.append(task)
        print(f"Задача '{description}' добавлена.")

    def complete_task(self, description):
        for task in self.tasks:
            if task['description'] == description:
                task['status'] = 'Задача выполнена'
                print(f"Задача '{description}' Отмечена как выполненная.")
                return
        print(f"Задача '{description}' не найдена.")

    def show_current_tasks(self):
        print("Текущие задачи:")
        for task in self.tasks:
            if task['status'] == 'Не выполнено':
                print(f"{task['description']} - до {task['deadline']}")


task_manager = Task()

task_manager.add_task("Сделать домашнее задание", "05-30-2024")
task_manager.add_task("Сходить в бассейн", "05-30-2024")
task_manager.complete_task("Сделать домашнее задание")
task_manager.show_current_tasks()