#!/usr/bin/python3


class Task:

    PENDING = 0
    COMPLETED = 1

    def __init__(self, title):
        self.title = title
        self.status = Task.PENDING

    def complete(self):
        self.status = Task.COMPLETED

    def uncomplete(self):
        self.status = Task.PENDING

    def __str__(self):
        status = {
            Task.PENDING: 'Pending',
            Task.COMPLETED: 'Completed',
        }[self.status]
        return f'{self.title} ({status})'


class TodoList:

    def __init__(self):
        self.tasks = []

    def add_task(self, title):
        self.tasks.append(Task(title))

    def remove_task(self, number):
        del self.tasks[number - 1]

    def complete_task(self, number):
        self.tasks[number - 1].complete()

    def uncomplete_task(self, number):
        self.tasks[number - 1].uncomplete()

    def clear(self):
        self.tasks = []

    def show(self):
        for i, task in enumerate(self.tasks, start=1):
            print(f'{i}. {task}')


def main():
    todo_list = TodoList()

    while True:
        print("""
        1. Add task
        2. List all tasks
        3. Mark a task as completed
        4. Mark a task as pending
        5. Remove a single task
        6. Clear the entire to-do list
        7. Quit
        """)

        option = int(input('Option? '))

        if option == 1:
            title = input('Task title? ')
            todo_list.add_task(title)
        elif option == 2:
            todo_list.show()
        elif option == 3:
            task_number = int(input('Task number? '))
            todo_list.complete_task(task_number)
        elif option == 4:
            task_number = int(input('Task number? '))
            todo_list.uncomplete_task(task_number)
        elif option == 5:
            task_number = int(input('Task number? '))
            todo_list.remove_task(task_number)
        elif option == 6:
            todo_list.clear()
            print('To-do list was cleared')
        elif option == 7:
            print('Bye')
            break
        print()


if __name__ == '__main__':
    main()
