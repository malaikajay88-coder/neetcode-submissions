class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        # Add new element to the back of the queue
        self.stack1.append(x)

    def pop(self) -> int:
        self.move_elements()
        return self.stack2.pop()

    def peek(self) -> int:
        self.move_elements()
        return self.stack2[-1]

    def empty(self) -> bool:
        return len(self.stack1) == 0 and len(self.stack2) == 0

    def move_elements(self) -> None:
        # Move only when stack2 is empty
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())