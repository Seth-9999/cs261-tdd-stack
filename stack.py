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
        self._size = 0
        self._capacity = 1

    def pop(self):
        """Removes last element within the Stack and returns
           Returns IndexError if no items in Stack"""

        if self._size == 0:
            raise IndexError

        val = self._structure[self._size - 1]
        self._size -= 1
        return val

    def is_empty(self):
        """Returns True/False if no elements within stack"""
        return self._size == 0

    def peek(self):
        """Looks at last element in stack and returns it. Value will still be present in the Stack. Returns None
        if no items in the stack raise IndexError
        """
        if self._size == 0:
            raise IndexError
        else:
            val = self._structure[self._size - 1]
        return val

    def push(self, value):
        """Add item to the top of the stack"""

        is_first_use_of_stack = True if (self._size == 0 and self._capacity == 1) else False
        stack_at_capacity = True if self._capacity == self._size else False

        if is_first_use_of_stack:
            self._size += 1
            self._structure.append(value)
        elif stack_at_capacity:
            self._size += 1
            self.__increase_stack_capacity()
            self._structure.append(value)
        else:
            self._size += 1
            self._structure[self._size - 1] = value

    def __increase_stack_capacity(self):
        """Doubles stack capacity. If capacity was 2 elements, is now 4 elements."""
        self._capacity *= 2

    def __str__(self):
        """Overwrite print method in python"""
        count = 0
        string = ""
        for i in range(self._size):
            string = string + str(self._structure[i])
            count += 1
            if count != self._size:
                string += " "
        return string

# temp = Stack()
# temp.push(50)
# temp.push(75)
# temp.push(100)
# print(temp.pop())
# print(temp.pop())
# print(temp.pop())
# temp.push(5)
# temp.push(10)
# print("Peek : " + str(temp.peek()))
# print(temp)
