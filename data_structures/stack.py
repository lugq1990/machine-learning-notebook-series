# -*- coding:utf-8 -*-
"""Stack is similiar with Queue, the only difference is that Queue is first in first out,
but stack is last in first out aka LIFO. By using python list to implement stack is really
easy."""


class Stack:
    def __init__(self):
        self.head = []

    def push(self, value):
        """
        Push one value to the stack
        :param value: object to be pushed
        :return: self
        """
        self.head.append(value)

    def pop(self):
        """
        Remove the last in object first
        :return: self
        """
        return self.head.pop()

    def insert(self, value, position=-1):
        """
        Insert object to the stack
        :param value: object to be inserted
        :param position: where to insert the object
        :return: self
        """
        if position < -1:
            position = -1

        self.head.insert(position, value)

    def remove(self, value):
        """
        Remove the first satisfied value
        :param value: value to be removed
        :return: self, if not exists, raise error
        """
        if value not in self.head:
            raise ValueError("Value %s not in the Stack!" % str(value))
        self.head.remove(value)

    def search(self, value):
        """
        Get the first satisfied value position
        :param value: which value to find
        :return: position of the value
        """
        if value not in self.head:
            raise ValueError("Value %s not in the Stack!" % str(value))
        return self.head.index(value)

    def reverse(self):
        """
        Reverse the stack
        :return: reversed stack
        """
        self.head = list(reversed(self.head))

    def delete(self):
        """
        Remove the stack whole values
        :return: None object
        """
        self.head = None

    def print_val(self):
        """
        Print the whole objects in the stack
        :return: whole objects in the stack
        """
        if self.head is None:
            print("Nothing in the stack!")

        print("Whole values in the stack: ", self.head)

    @property
    def length(self):
        return len(self.head)


if __name__ == '__main__':
    stack = Stack()
    stack.push(0)
    stack.push(1)
    stack.insert(2, -1)
    stack.insert(3, 0)
    stack.insert(4, 1)
    stack.print_val()

    stack.remove(0)
    stack.print_val()

    print("Find value: ", stack.search(1))

    stack.reverse()
    stack.print_val()

    print("How many values: ", stack.length)

    stack.delete()
    stack.print_val()




