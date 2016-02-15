from collections import deque
from .base import BookScraper, Node
from .kanunu import KanunuScraper, KanunuMultiVolumeScraper


def print_node(node):
    stack = deque()
    stack.append((0, node))

    while stack:
        level, node = stack.pop()
        spaces = '  ' * level
        print('%s%s' % (spaces, node))
        for child in reversed(node.children):
            stack.append((level+1, child))


def make_ebook(scraper_class, output_file, add_page_markers=True):
    scraper = scraper_class()
    scraper.download()
    scraper.build_ebook(output_file, add_page_markers=add_page_markers)
