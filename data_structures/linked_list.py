# -*- coding:utf-8 -*-
"""Linked list is a linear data structure, that the data object
is connected with pointer, linked list is really easy to understand
as the next node is connected with previous node, we could get data
from head pointer, then go to next.
Here with basic operations: insert, find, remove, delete, reverse etc.
"""


class Node:
    """Object to store value and pointer to next"""
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value, position=-1):
        """
        insert value to the linked list, position with -1 means to the last,
        position with 0 means head, position with other means that position
        :param value: which value to be inserted
        :param position: where to insert the value
        :return: self
        """
        if self.head is None:
            # if head is none, no matter which position
            self.head = Node(value)
        else:
            if position < -1:
                position = -1

            # make a node to represent the head node
            node = self.head

            if position == 0:
                # if with first position, just create a new head
                # and change the new head next with original head
                self.head = Node(value)
                self.head.next = node
            elif position == -1:
                # add a node to the last, we should change the node until
                # pointer to the last node
                while node.next is not None:
                    node = node.next

                # here node is just the last node
                node.next = Node(value)
            else:
                # with position should insert value, with additional val to store which step
                cur_step = 1
                while node.next is not None and cur_step < position:
                    node = node.next
                    cur_step += 1
                # if node.next node is just None, we could just add one node
                if node.next is None:
                    node.next = Node(value)
                else:
                    # we should change the original next node with new created node
                    # and change the node.next.next to original node.next node
                    next_node = node.next
                    node.next = Node(value)
                    node.next.next = next_node

    def find(self, value):
        """
        find the value position
        :param value: which value to find
        :return: the index of that value, if not exist, raise error
        """
        if self.head is None:
            raise ValueError("Value %s not in the List!" % str(value))
        else:
            node = self.head
            cur_step = 0
            if node.value == value:
                # find the value with first position
                return cur_step
            else:
                # recursively find value
                while node.next is not None:
                    node = node.next
                    cur_step += 1
                    if node.value == value:
                        return cur_step
                # doesn't find value until the last node
                raise ValueError("Value %s not in the List!" % str(value))

    def remove(self, value=None, position=None):
        """
        remove node with satisfied value also could just remove with index
        :param value: which value to be removed
        :param position: which position node to be removed
        :return: self, if value not exists raise error
        """
        if self.head is None:
            raise ValueError("Nothing in the list!")
        else:
            if value is None and position is None:
                raise ValueError("Couldn't set both parameters to be None!")
            elif value is not None and position is not None:
                raise ValueError("Couln't set both parameters!")

            node = self.head
            cur_step = 0
            if (node.value == value) or (position == cur_step):
                # get the head value satisfied with find value or position
                if node.next is None:
                    # with just one node
                    self.head = None
                else:
                    self.head = self.head.next
                return self
            else:
                # find the next node
                while node.next is not None:
                    if (node.next.value == value) or (position == cur_step + 1):
                        if node.next.next is None:
                            # after two node is None, then just remove the next node safely
                            node.next = None
                        else:
                            # after two node is not None, we should link current node with after two node
                            node.next = node.next.next
                        return self
                    else:
                        node = node.next
                        cur_step += 1

                # after whole step finished, still don't find the value, just raise error
                raise ValueError("Value %s not in the list!" % str(value))

    def delete(self):
        """
        delete the whole linked list
        :return: None
        """
        self.head = None

    def reverse(self):
        """
        change whole list order with reverse order
        :return: reversed list
        """
        if self.head is None:
            raise ValueError("Nothing in the list!")
        else:
            # two pointers, one with previous node, the other with current node
            # pre node change to current node, curr node move to next node, and change
            # current node next node with pre node until reach the end of the list
            pre_node, cur_node = None, self.head
            while cur_node is not None:
                cur_node.next, pre_node, cur_node = pre_node, cur_node, cur_node.next

            self.head = pre_node
            return self

    def print_var(self):
        """
        print the linked list value
        :return: value list
        """
        if self.head is None:
            print("Nothing in the list!")
        else:
            node = self.head
            res_list = [node.value]
            while node.next is not None:
                node = node.next
                res_list.append(node.value)
            print("Get Linked List value: ", res_list)


if __name__ == '__main__':
    ll = LinkedList()
    ll.insert(0)
    ll.insert(1)
    ll.insert(2, 0)
    ll.insert(3, 1)
    ll.insert(4, -1)

    ll.print_var()

    print("Find value: ", ll.find(0))

    ll.remove(0)
    ll.print_var()

    ll.reverse()
    ll.print_var()






