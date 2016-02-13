from collections import deque
from .base import BookScraper, Node


def print_node(node):
    stack = deque()
    stack.append((0, node))

    while stack:
        level, node = stack.pop()
        spaces = '  ' * level
        print('%s%s' % (spaces, node))
        for child in reversed(node.children):
            stack.append((level+1, child))
