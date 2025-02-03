__author__ = 'https://github.com/SwairIt/To-Do-List/blob/main/main.py'
import os

# Файл для хранения задач
TODO_FILE = "todolist.txt"

# Загрузка задач из файла
def load_tasks():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, "r") as file:
            tasks = file.readlines()
        return [task.strip() for task in tasks]
    return []

# Сохранение задач в файл
def save_tasks(tasks):
    with open(TODO_FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n")

# Добавление задачи
def add_task(task):
    tasks = load_tasks()
    tasks.append(task)
    save_tasks(tasks)

# Удаление задачи
def remove_task(task_index):
    tasks = load_tasks()
    if 0 <= task_index < len(tasks):
        del tasks[task_index]
        save_tasks(tasks)
        print("Задача удалена.")
    else:
        print("Некорректный номер задачи.")

# Показать все задачи
def show_tasks():
    tasks = load_tasks()
    if tasks:
        print("Список задач:")
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")
    else:
        print("Нет задач!")

# Основная логика
def main():
    while True:
        print("\n1. Показать все задачи")
        print("2. Добавить задачу")
        print("3. Удалить задачу")
        print("4. Выйти")

        choice = input("Выберите действие (1-4): ")

        if choice == "1":
            show_tasks()
        elif choice == "2":
            task = input("Введите задачу: ")
            add_task(task)
        elif choice == "3":
            show_tasks()
            task_number = int(input("Введите номер задачи для удаления: ")) - 1
            remove_task(task_number)
        elif choice == "4":
            print("Выход...")
            break
        else:
            print("Неверный выбор. Пожалуйста, выберите снова.")

if __name__ == "__main__":
    main()
