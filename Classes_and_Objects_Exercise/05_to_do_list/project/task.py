class Task:

    def __init__(self, name: str, due_date: str):
        self.comments = []
        self.completed = False
        self.name = name
        self.due_date = due_date

    def change_name(self, new_name: str):
        if self.name == new_name:
            return "Name cannot be the same."

        self.name = new_name
        return new_name

    def change_due_date(self, new_date: str):
        if new_date == self.due_date:
            return "Date cannot be the same."

        self.due_date = new_date
        return new_date

    def add_comment(self, comment: str):
        self.comments.append(comment)

    def edit_comment(self, comment_number: int, new_comment: str):
        comment_index = comment_number
        if comment_index >= len(self.comments):
            return "Cannot find comment."

        self.comments[comment_index] = new_comment
        return ', '.join(self.comments)

    def details(self):
        return f"Name: {self.name} - Due Date: {self.due_date}"


