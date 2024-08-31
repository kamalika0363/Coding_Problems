"""
Given a binary tree, write a function to determine whether it is a binary search tree (BST).
A binary search tree is defined as a binary tree in which, for every node,
the left subtree contains only nodes with values less than the node's value,
and the right subtree contains only nodes with values greater than the node's value.
Additionally, both the left and right subtrees must also be binary search trees.
How would you implement a solution to check if the given tree is a BST? (DO NOT USE RECURSION)
"""


class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def is_bst(root):
    if not root:
        return True

    stack = []
    current = root
    prev_value = float('-inf')

    while stack or current:
        while current:
            stack.append(current)
            current = current.left

        current = stack.pop()
        if current.value <= prev_value:
            return False
        prev_value = current.value
        current = current.right

    return True


def test_is_bst():
    # Create a BST:
    root1 = TreeNode(5)
    root1.left = TreeNode(3)
    root1.right = TreeNode(7)
    root1.left.left = TreeNode(2)
    root1.left.right = TreeNode(4)
    root1.right.right = TreeNode(8)

    # Create a non-BST:
    root2 = TreeNode(5)
    root2.left = TreeNode(3)
    root2.right = TreeNode(7)
    root2.left.left = TreeNode(2)
    root2.left.right = TreeNode(8)
    root2.right.left = TreeNode(6)

    # Create an empty tree
    root3 = None

    # Test cases
    assert is_bst(root1) == True, "Test case 1 failed"
    assert is_bst(root2) == False, "Test case 2 failed"
    assert is_bst(root3) == True, "Test case 3 failed"

    print("All test cases passed.")


if __name__ == "__main__":
    test_is_bst()
