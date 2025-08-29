# todo_list.py
class TodoList:
    def __init__(self):
        self.tasks = []
    
    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})
        print("Task added! ✅")
    
    def show_tasks(self):
        print("\n--- Your Tasks ---")
        for i, task in enumerate(self.tasks, 1):
            status = "✓" if task["completed"] else " "
            print(f"{i}. [{status}] {task['task']}")
    
    def complete_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index]["completed"] = True
            print("Task completed! 🎯")
        else:
            print("Invalid task number!")
    
    def remove_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks.pop(task_index)
            print("Task removed! ❌")
        else:
            print("Invalid task number!")

def main():
    todo = TodoList()
    
    while True:
        print("\n--- To-Do List Menu ---")
        print("1. Add task")
        print("2. View tasks")
        print("3. Complete task")
        print("4. Remove task")
        print("5. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            task = input("Enter task: ")
            todo.add_task(task)
        elif choice == '2':
            todo.show_tasks()
        elif choice == '3':
            todo.show_tasks()
            try:
                index = int(input("Task number to complete: ")) - 1
                todo.complete_task(index)
            except ValueError:
                print("Please enter a valid number!")
        elif choice == '4':
            todo.show_tasks()
            try:
                index = int(input("Task number to remove: ")) - 1
                todo.remove_task(index)
            except ValueError:
                print("Please enter a valid number!")
        elif choice == '5':
            print("Goodbye! 👋")
            break
        else:
            print("Invalid option!")

if __name__ == "__main__":
    main()