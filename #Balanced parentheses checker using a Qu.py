#Balanced parentheses checker using a Queue. 

class Queue:
    def __init__(self):
        # Initializes an empty list to act as the queue.
        self.items = []

    def is_empty(self):
        # Checks if the queue is empty.
        return len(self.items) == 0

    def enqueue(self, item):
        # Adds an item to the end of the queue.
        self.items.append(item)

    def dequeue(self):
        # Removes and returns the item from the front of the queue, or None if empty.
        return self.items.pop(0) if not self.is_empty() else None


def is_balanced(expression):
   
    # Creates a queue to keep track of opening parentheses.
    queue = Queue()

    # Defines matching pairs for parentheses.
    opening = "({["
    closing = ")}]"
    matches = {')': '(', '}': '{', ']': '['}

    for char in expression:
        if char in opening:
            # Enqueues opening parentheses.
            queue.enqueue(char)
        elif char in closing:
            # If the queue is empty or the dequeued item does not match, it returns as False.
            if queue.is_empty() or queue.dequeue() != matches[char]:
                return False

    # If the queue is empty, all parentheses are balanced.
    return queue.is_empty()


def main():
    # Test cases
    expression1 = "({X+Y}*Z)"    # Balanced
    expression2 = "{X+Y}*Z)"     # Unbalanced (extra closing parenthesis)
    expression3 = "({X+Y}*Z"     # Unbalanced (missing closing parenthesis)
    expression4 = "[A+B]*({X+Y}]*Z)"  # Unbalanced (mismatched parenthesis)

    # Prints results for each test case.
    print(is_balanced(expression1))  # Expected: True
    print(is_balanced(expression2))  # Expected: False
    print(is_balanced(expression3))  # Expected: False
    print(is_balanced(expression4))  # Expected: False


# Executes the program.
main()
