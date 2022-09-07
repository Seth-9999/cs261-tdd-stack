# Stack: A stack.
# Your implementation should pass the tests in stack.py.
# Jon Riemer

class Stack:
    """
    LIFO data structures. First item added to structure will be last item to be removed.
    """
    def __init__(self):
        """Setup stack data structure"""
        self._structure = []

    def pop(self):
        """Removes last element within the Stack and returns"""
        val = self._structure[-1]
        self._structure.pop()
        return val

    def is_empty(self):
        """Returns True/False if no elements within stack"""
        if len(self._structure) == 0:
            return True
        else:
            return False

    def peek(self):
        """Looks at last element in stack and returns it. Value will still be present in the Stack"""
        val = self._structure[-1]
        return val

    def push(self, value):
        """Add item to the top of the stack"""
        self._structure.append(value)
