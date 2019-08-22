# -*- coding:utf-8 -*-
"""
Doubly Linked List is really similar with Linked List,
the only difference is that Linked List is just connected
with next pointer, but with doubly linked list is connected
with previous and next pointer. Doubly linked list is more
efficient for querying, but will cost more space to store
the linked list connections.
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.pre = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.nums = 0

    def insert(self, value, position=-1):
        """
        insert value into doubly linked list with that position
        :param value: which value to be inserted
        :param position: where the value should be inserted, -1 means the last position,
        0 means first position, otherwise with that position
        :return: self
        """
        self.nums += 1

        if self.head is None:
            self.head = Node(value)
        else:
            if position < -1:
                position = -1

            node = self.head
            if position == 0:
                # if insert at head position, then create new head with next node with previous head
                # but the previous node's previous should be new head node
                self.head = Node(value)
                self.head.next = node
                node.pre = self.head
            elif position == -1:
                # if with last position that should go to the last node, change last node next with new node
                # and link added last node with previous last node
                while node.next is not None:
                    node = node.next
                node.next = Node(value)
                node.next.pre = node
            else:
                cur_step = 1
                while node.next is not None and cur_step < position:
                    node = node.next
                    cur_step += 1

                if node.next is None:
                    # if next node is None, just create a new one
                    node.next = Node(value)
                    node.next.pre = node
                else:
                    # otherwise, store next node object, then change current node next node
                    # with new created node, linked the new created node previous with current node
                    # and next with next node, also link with stored next node linked with new created node
                    next_node = node.next
                    node.next = Node(value)
                    node.next.pre = node
                    node.next.next = next_node
                    next_node.pre = node.next

    def find(self, value):
        """
        get the satisfied value position
        :param value: which value to be found
        :return: the position of that value, if not found raise error
        """
        if self.head is None:
            raise ValueError("Nothing in the list!")
        else:
            cur_step = 0
            node = self.head
            if node.value == value:
                # if get the value from first position
                return cur_step
            else:
                # go to next node if next node is not None
                while node.next is not None:
                    node = node.next
                    cur_step += 1
                    if node.value == value:
                        return cur_step
                raise ValueError("Doesn't find value %s from the list!" % str(value))

    def remove(self, value=None, position=None):
        """
        remove satisfied value or position node
        :param value: which value to be removed
        :param position: which position node should be removed
        :return: returned satisfied value node or that position node
        """
        if value is None and position is None:
            raise ValueError("Couldn't set both value and position to be None!")
        if value is not None and position is not None:
            raise ValueError("Couldn't set both value and position at same time!")

        if self.head is None:
            # if nothing in the list, just return with None
            return None
        else:
            node = self.head
            cur_step = 0
            if (node.value == value) or (cur_step == position):
                # should just remove the head
                remove_value = node.value
                if node.next is None:
                    # if there is just one node
                    self.head = None
                else:
                    # just change head node with next node
                    self.head = self.head.next
                return remove_value
            else:
                # not find value or position with first position
                while node.next is not None:
                    if (node.next.value == value) or (cur_step + 1 == position):
                        remove_value = node.next.value
                        # get next satisfied value or with that position satisfied
                        if node.next.next is None:
                            # node.next is last node, then just remove the next node
                            node.next = None
                        else:
                            # removed node is between two nodes, then just remove that
                            # node, and change current node next node with next_next node
                            # and change next_next node previous node with current node
                            next_next_node = node.next.next
                            node.next = None
                            node.next = next_next_node
                            next_next_node.pre = node
                        return remove_value
                    else:
                        # doesn't find that value, change node to next node
                        node = node.next
                        cur_step += 1

                # during while loop doesn't get the removed node
                raise ValueError("Doesn't find the value or position in the list!")

    def delete(self):
        """
        remove the whole linked list
        :return: None
        """
        self.head = None

    def reverse(self):
        """
        change whole linked list value order with reverse
        :return: reversed doubly linked list
        """
        if self.head is None:
            # nothing to do
            pass
        else:
            pre_node, cur_node = None, self.head
            while cur_node is not None:
                # iterate util the cur_node goes to last null pointer
                # change curr node's next to be pre_node, pre_node's previous node to cur_node
                # change pre_node to cur_node, change cur_node to next node
                cur_node.next, pre_node, cur_node = pre_node, cur_node, cur_node.next
            self.head = pre_node
            return self

    def print_var(self):
        """
        print the whole doubly linked list values
        :return: whole values in the doubly linked list
        """
        if self.head is None:
            print("Nothing in the list!")
        else:
            node = self.head
            res_list = [node.value]

            while node.next is not None:
                node = node.next
                res_list.append(node.value)

            print("Get Doubly Linked List values: ", res_list)

    @property
    def length(self):
        return self.nums


if __name__ == '__main__':
    dll = DoublyLinkedList()
    dll.insert(0)
    dll.insert(1, -1)
    dll.insert(2, -1)
    dll.print_var()

    print("Get position:", dll.find(2))

    dll.remove(0)
    dll.print_var()

    dll.reverse()
    dll.print_var()
