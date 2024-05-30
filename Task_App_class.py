import tkinter as tk
from tkinter import simpledialog

class TaskApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Менеджер задач")
        self.master.configure(bg='#f0f0f0')

        self.task_manager = Task()

        self.lst_box = tk.Listbox(self.master, width=50, height=10, bg='#ffffff', fg='#333333', selectbackground='#cccccc')
        self.lst_box.pack(pady=20)


        tk.Button(self.master, text="Добавить задачу", command=self.add_task, bg='#4CAF50', fg='white').pack(side=tk.LEFT, padx=10)
        tk.Button(self.master, text="Задача выполнена", command=self.complete_task, bg='#F44336', fg='white').pack(side=tk.LEFT, padx=10)
        tk.Button(self.master, text="Показать текущие задачи", command=self.show_current_tasks, bg='#2196F3', fg='white').pack(side=tk.LEFT, padx=10)

        self.show_current_tasks()

    def add_task(self):
        description = simpledialog.askstring("Добавление задачи", "Описание задачи:")
        deadline = simpledialog.askstring("Добавление задачи", "Срок выполнения (ГГГГ-ММ-ДД):")
        if description and deadline:
            self.task_manager.add_task(description, deadline)
            self.show_current_tasks()

    def complete_task(self):
        description = self.lst_box.get(tk.ACTIVE).partition(" - до ")[0]
        if description:
            self.task_manager.complete_task(description)
            self.show_current_tasks()

    def show_current_tasks(self):
        self.lst_box.delete(0, tk.END)
        for task in self.task_manager.tasks:
            if task['status'] == 'Не выполнено':
                self.lst_box.insert(tk.END, f"{task['description']} - до {task['deadline']}")

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
                print(f"Задача '{description}' отмечена как выполненная.")
                return
        print(f"Задача '{description}' не найдена.")

if __name__ == "__main__":
    root = tk.Tk()
    app = TaskApp(root)
    root.mainloop()