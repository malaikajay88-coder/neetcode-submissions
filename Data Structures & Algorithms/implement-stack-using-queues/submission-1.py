from collections import deque

class MyStack:

    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x: int) -> None:
        # Put new element into q2
        self.q2.append(x)
        # Move all old elements from q1 to q2
        while self.q1:
            self.q2.append(self.q1.popleft())

        # Swap queues
        self.q1, self.q2 = self.q2, self.q1

    def pop(self) -> int:
        # Front of q1 is the stack top
        return self.q1.popleft()

    def top(self) -> int:
        # Return front element without removing it
        return self.q1[0]

    def empty(self) -> bool:
        return len(self.q1) == 0