import tkinter as tk
from tkinter import messagebox

class TodoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Application")

        self.tasks = []

        # Create GUI elements
        self.task_entry = tk.Entry(root, width=40)
        self.task_entry.pack(pady=10)

        self.task_listbox = tk.Listbox(root, width=50, height=10, selectbackground="yellow")
        self.task_listbox.pack(pady=20)

        self.add_task_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_task_button.pack()

        self.delete_task_button = tk.Button(root, text="Delete Task", command=self.delete_task)
        self.delete_task_button.pack(pady=10)

        self.quit_button = tk.Button(root, text="Quit", command=root.quit)
        self.quit_button.pack()

        # Load any saved tasks from file (if needed)
        # self.load_tasks()

        # Display existing tasks
        self.display_tasks()

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
            # Save tasks to file (if needed)
            # self.save_tasks()
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def delete_task(self):
        try:
            task_index = self.task_listbox.curselection()[0]
            self.task_listbox.delete(task_index)
            del self.tasks[task_index]
            # Save tasks to file (if needed)
            # self.save_tasks()
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to delete.")

    def display_tasks(self):
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

    # Optional: Save and load tasks from a file
    # def save_tasks(self):
    #     with open("tasks.txt", "w") as f:
    #         for task in self.tasks:
    #             f.write(task + "\n")

    # def load_tasks(self):
    #     try:
    #         with open("tasks.txt", "r") as f:
    #             for line in f:
    #                 self.tasks.append(line.strip())
    #     except FileNotFoundError:
    #         pass

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoListApp(root)
    root.mainloop()
