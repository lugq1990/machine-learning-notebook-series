# -*- coding:utf-8 -*-
"""Binary search tree is the data structure with non-linear structure,
as we could do more actions with binary search tree, the worst search
space is O(h), h is the height of tree. The logic for binary search tree
is for new coming data, if the value is less then the root value, then
go to left, otherwise go to the right.
Here includes with search, insert, delete, remove etc. common actions
implement for binary tree.
Also for binary search tree, there couldn't be same value
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.leftChild = None
        self.rightChild = None

    def insert(self, value):
        """
        insert value into the node
        :param value: which value to be inserted
        :return: self
        """
        if value == self.value:
            raise ValueError("Couldn't insert same value!")
        elif value < self.value:
            # go to the left node
            if self.leftChild:
                # if left node exists, then recursively add
                return self.leftChild.insert(value)
            else:
                # if the left node is None
                self.leftChild = Node(value)
                return True
        else:
            # go the the right node
            if self.rightChild:
                return self.rightChild.insert(value)
            else:
                self.rightChild = Node(value)
                return True

    def get_min_node(self, node):
        """
        as we could get the min value with left child node value
        :param node: which node to start to find the value
        :return: min value node
        """
        while node.leftChild is not None:
            node = node.leftChild
        return node

    def delete(self, value):
        """
        delete value from the tree
        :param value: which value to be removed
        :return: the node to be removed
        """
        if self is None:
            # nothing in the tree
            return None

        if value < self.value:
            # if value less then the current value, then go the left
            self.leftChild = self.leftChild.delete(value)
        elif value > self.value:
            # if value larger then the current value, then go the right
            self.rightChild = self.rightChild.delete(value)
        else:
            # if with just one node on each side
            if self.leftChild is None:
                # create a temperate value to store the right node,
                # change current value to None
                tmp = self.rightChild
                self = None
                return tmp
            elif self.rightChild is None:
                tmp = self.leftChild
                self = None
                return tmp

            # then current node both left and right is not None
            # we should get the right side min value for changing the current node
            tmp = self.get_min_node(self.rightChild)
            self.value = tmp.value
            self.rightChild = self.rightChild.delete(tmp.value)
        return self

    def find(self, value):
        """
        find the value in the tree
        :param value: which value to find
        :return: True if Found, otherwise False
        """
        if value == self.value:
            return True

        elif value < self.value:
            # whether the left node exists
            if self.leftChild:
                return self.leftChild.find(value)
            else:
                return False
        else:
            if self.rightChild:
                return self.rightChild.find(value)
            else:
                return True

    # this is just used to print the value in the tree
    def preorder(self):
        if self:
            print(str(self.value), end=' ')
            if self.leftChild:
                self.leftChild.preorder()
            if self.rightChild:
                self.rightChild.preorder()

    def inorder(self):
        if self:
            if self.leftChild:
                self.leftChild.inorder()
            print(str(self.value), end=' ')
            if self.rightChild:
                self.rightChild.inorder()

    def postorder(self):
        if self:
            if self.leftChild:
                self.leftChild.postorder()
            if self.rightChild:
                self.rightChild.postorder()
            print(str(self.value), end=' ')


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root:
            return self.root.insert(value)
        else:
            # the node doesn't exist
            self.root = Node(value)
            return True

    def delete(self, value):
        if self.root is not None:
            return self.root.delete(value)

    def find(self, value):
        if self.root:
            return self.root.find(value)
        else:
            # don't find the value
            return False

    def preorder(self):
        if self.root is not None:
            print()
            print('preorder: ')
            self.root.preorder()

    def inorder(self):
        if self.root is not None:
            print()
            print("inorder:")
            self.root.inorder()

    def postorder(self):
        if self.root is not None:
            print()
            print("Postorder:")
            self.root.postorder()

    def print_var(self, node=None):
        if node is None:
            node = self.root
            print('root node')

        print(node.value)
        if node.leftChild is not None:
            print("Left node:")
            self.print_var(node.leftChild)
        if node.rightChild is not None:
            print('right node:')
            self.print_var(node.rightChild)


if __name__ == '__main__':
    bst = BinarySearchTree()
    bst.insert(10)
    bst.insert(1)
    bst.insert(11)
    bst.insert(2)

    bst.print_var()

    print("Find: ", bst.find(3))

    bst.delete(11)
    print('*'*10)
    bst.print_var()

