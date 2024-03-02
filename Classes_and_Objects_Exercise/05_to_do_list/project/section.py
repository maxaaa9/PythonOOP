from project.task import Task


class Section:

    def __init__(self, name: str):
        self.tasks = []
        self.name = name

    def add_task(self, new_task: Task):
        if new_task in self.tasks:
            return f"Task is already in the section {self.name}"

        self.tasks.append(new_task)
        return f"Task {new_task.details()} is added to the section"

    def complete_task(self, task_name: str):
        try:
            current_task = next(filter(lambda t: t.name == task_name, self.tasks))

        except StopIteration:
            return f"Could not find task with the name {task_name}"

        current_task.completed = True
        return f"Completed task {task_name}"

    def clean_section(self):
        complete_task_counter = 0

        for task in self.tasks:
            if task.completed:
                complete_task_counter += 1
                self.tasks.remove(task)

        return f"Cleared {complete_task_counter} tasks."

    def view_section(self):
        details = "\n".join(task.details() for task in self.tasks)
        return (f"Section {self.name}:\n"
                f"{details}")