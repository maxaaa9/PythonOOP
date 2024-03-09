class User:

    def __init__(self, user_id: int, username: str):
        self.books = []
        self.user_id = user_id
        self.username = username

    def info(self) -> str:
        user_books = ', '.join(x for x in sorted(self.books))
        return user_books

    def __str__(self):
        return f"{self.user_id}, {self.username}, {self.books}"
