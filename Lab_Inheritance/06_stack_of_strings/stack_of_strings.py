class Stack:

    def __init__(self):
        self.data = []

    def push(self, element: str) -> None:
        self.data.append(element)

    def pop(self) -> str or int:
        popped = self.data.pop()
        return popped

    def top(self):
        return self.data[-1]

    def is_empty(self):
        return True if not self.data else False

    def __str__(self):
        result = ', '.join(str(x) for x in reversed(self.data))
        return f"[{result}]"




