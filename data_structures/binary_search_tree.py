# -*- coding:utf-8 -*-
"""Binary search tree is the data structure with non-linear structure,
as we could do more actions with binary search tree, the worst search
space is O(h), h is the height of tree. The logic for binary search tree
is for new coming data, if the value is less then the root value, then
go to left, otherwise go to the right.
Here includes with search, insert, delete, remove etc. common actions
implement for binary tree.
"""


class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.head = None

    def insert(self, value, node=None):
        """
        insert value to the tree
        :param value: which value to be inserted
        :param node: which node to compare
        :return: self
        """
        if self.head is None:
            # if the head is None
            self.head = Node(value)
        else:
            # tree root node isn't None, then we should compare current value
            # with root value, if the value is smaller than root value, then
            # we should go left, otherwise should go right
            if node is None:
                # if node is None, then just change the node to head node
                node = self.head

            if value < node.value:
                # then we should go to left
                if node.left is None:
                    # if there isn't any node on current left node
                    # then just create a new node
                    node.left = Node(value)
                else:
                    # left node is not none, then we should compare current value
                    # with left node recursively
                    # have to use return!
                    return self.insert(value, node.left)
            else:
                # if value is bigger than current value, then move to right,
                # even if the value is same with current value
                if node.right is None:
                    # right node is just None, create a new one
                    node.right = Node(value)
                else:
                    # right node is not None, go to right node and compare
                    return self.insert(value, node.right)

    def search(self, value, node=None):
        """
        search value from the tree, the time complexity is O(h), h is the tree height.
        :param value: which value to be searched
        :param node: which node to compare
        :return: value if found, else return None means not found
        """
        if self.head is None:
            # if root is None, just return None
            return None
        else:
            if node is None:
                # if this is called for head
                node = self.head

            if value < node.value:
                if node.left is None:
                    # nothing could be found, return None
                    return None
                else:
                    # recursively to find the left node
                    return self.search(value, node.left)
            elif value > node.value:
                # go to the right node
                if node.right is None:
                    # nothing in the tree! just return None
                    return None
                else:
                    return self.search(value, node.left)
            elif value == node.value:
                # we found the value, so great
                return value
            else:
                # even if recursively search the tree, we don't find that value
                return None

    def _find_min_node(self, node):
        # recursively to get the left node
        while node.left is not None:
            node = node.left
        return node

    def remove(self, value, node=None, parent_node=None):
        """
        remove satisfied value from the tree, as we will face with 3 cases:
        1. remove value is just leaf node
        2. remove value with just one leaf, then just change the removed node to the leaf node
        3. remove value has two nodes, then we have to find that node's right node's minimum value
        to change the current node
        :param value: which value to be removed
        :param node: which node to find
        :return: the node to be removed
        """
        if self.head is None:
            # nothing in the tree
            return None
        else:
            if node is None:
                node = self.head

            if parent_node is None:
                parent_node = self.head

            if value < node.value:
                parent_node = node
                node = node.left
                return self.remove(value, node, parent_node)
            elif value > node.value:
                parent_node = node
                node = node.right
                return self.remove(value, node, parent_node)
            else:
                # we get the value
                if node.left is None:
                    parent_node = node.right
                elif node.right is None:
                    parent_node = node.left
                else:
                    # both node have left and right node
                    min_node = self._find_min_node(node)
                    node.value = min_node.value
                    min_node = None
                    parent_node = node
                return self

    def delete(self):
        """
        delete the whole tree
        :return: None
        """
        self.head = None

    def print_var(self, node=None):
        """
        print the values in tree to console
        :param node: which node value to print
        :return: Nothing
        """
        if node is None:
            node = self.head
            print("Root:", node.value)

        if node.left is not None:
            print("Left node value:", node.left.value)
            self.print_var(node.left)
        if node.right is not None:
            print("Right node value: ", node.right.value)
            self.print_var(node.right)


if __name__ == '__main__':
    tree = BinarySearchTree()
    tree.insert(10)
    tree.insert(8)
    tree.insert(11)
    tree.insert(0)
    tree.print_var()

    print("Find :", tree.search(0))

    print('*'*20)

    tree.remove(0)
    tree.print_var()

