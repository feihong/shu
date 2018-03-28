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


def make_ebook(scraper_class, index_url=None, title=None, author=None, **kwargs):
    scraper = scraper_class(index_url=index_url, title=title, author=author)
    scraper.download()
    scraper.build_ebook(**kwargs)
    return scraper
