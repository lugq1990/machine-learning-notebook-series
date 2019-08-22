# -*- coding:utf-8 -*-
"""This is to implement the basic data structure using python list,
Queue is known as first in first out aka FIFO.
The implement includes: push, pop, remove, insert, delete, search...
One thing to notice that using list to implement the queue is really time consuming
if you have lots of objects!
The reason is that with insert or delete object from list, then list will move the
whole objects with position, so you will notice that with more data will be hard!
I will also use deque module to implement more efficient ways."""

from collections import deque

class Queue:
    def __init__(self):
        self.head = []

    def push(self, value):
        """
        Push one value to the queue.
        :param value: object for the queue
        :return: self
        """
        self.head.append(value)

    def pop(self):
        """
        Remove the first income object in queue
        :return: first income object
        """
        return self.head.remove(self.head[0])

    def remove(self, value):
        """
        Remove the value that needed to be removed.
        :param value: object to be removed
        :return: self, if not exists, raise error
        """
        if value not in self.head:
            raise ValueError("Value %s not in the Queue!" % str(value))
        self.head.remove(value)

    def search(self, value):
        """
        Get the index of the value
        :param value: needed to get the index of value in queue
        :return: self, if not exists, raise error
        """
        if value not in self.head:
            raise ValueError("Value %s not in the Queue!" % str(value))
        return self.head.index(value)

    def delete(self):
        """
        Remove the whole queue.
        :return: self
        """
        self.head = None

    def insert(self, value, position=-1):
        """
        Insert object at some position
        :param value: value to be inserted
        :param position: which position to insert value, if -1 then means the last position,
        if 0 means the head, otherwise with that position
        :return: self
        """
        if position < -1:
            position = -1
        self.head.insert(position, value)

    def reverse(self):
        """
        Reverse the Queue
        :return: self
        """
        self.head = list(reversed(self.head))

    def print_var(self):
        """
        Print the whole Queue values
        :return: values print result
        """
        if self.head is None:
            print("Nothing in the Queue!")
        print("Get Queue:", self.head)


class QueueWithDeque:
    """
    This is a more efficient way to make the Queue structure.
    """
    def __init__(self):
        self.head = deque()

    def push(self, value):
        self.head.append(value)

    def pop(self):
        """
        Remove the first income value will be more efficient!
        :return: self
        """
        self.head.popleft()

    def search(self, value):
        if value not in self.head:
            raise ValueError("Value %s not in the Queue!" % str(value))
        return self.head.index(value)

    def remove(self, value):
        if value not in self.head:
            raise ValueError("Value %s not in the Queue!" % str(value))
        self.head.remove(value)

    def delete(self):
        self.head = None

    def insert(self, value, position=-1):
        if position < -1:
           position = -1
        self.head.insert(position, value)


if __name__ == '__main__':
    q = Queue()
    q.push(0)
    q.push(1)
    q.insert(2, -1)
    q.insert(3, 0)
    q.insert(4, 1)
    q.print_var()

    q.remove(0)
    q.print_var()

    print("Get position: ", q.search(1))

    q.reverse()
    q.print_var()

    q.delete()
    q.print_var()
