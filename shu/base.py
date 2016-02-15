import xml.etree
from collections import OrderedDict, deque
from pathlib import Path
import requests
import lxml.html
import html5lib
from pyquery import PyQuery
from .writer import PagedFileWriter


class BookScraper:
    title = 'TITLE'
    author = 'AUTHOR'
    index_url = ''

    def __init__(self, cache_root_dir=None):
        if cache_root_dir is None:
            cache_root_dir = get_default_cache_root_dir()
        self._cache_dir = Path(cache_root_dir) / self.title
        if not self._cache_dir.exists():
            self._cache_dir.mkdir()

        self._session = requests.Session()

        # Map of URLs to file names.
        self._files = OrderedDict()

    def download(self, preview=False):
        doc = self.get_index_doc()

        for link in self.get_links(doc):
            if preview:
                print(link)
            else:
                self.download_page(link)

        self.write_links_page()

    def get_doc(self, url):
        """
        Given a URL, get the cached contents of the page converted as a PyQuery
        object.
        """
        path = self._cache_dir / self._files[str(url)]
        return get_doc_from_file(path)

    def get_index_doc(self):
        """
        Download the index page if necessary and return it as a PyQuery object.
        """
        index_file = self._cache_dir / 'index.html'
        if not index_file.exists():
            self.download_page(self.index_url, 'index.html')
        return get_doc_from_file(str(index_file))

    def get_links(self, doc):
        """
        Given an index document, return the links to all its sections.
        """
        raise NotImplementedError

    def download_page(self, url, filename=None):
        """
        Download contents of the given URL.
        """
        response = self._session.get(url)
        # Try to use the existing filename for this URL.
        if filename is None:
            filename = self._files.get(url)
        # If that doesn't work, just use the next number.
        if filename is None:
            filename = '%d.html' % len(self._files)

        output_path = self._cache_dir / filename
        print('Downloading %s to %s' % (url, output_path))
        output_path.write_bytes(response.content)

        if not filename in self._files:
            self._files[url] = filename

    def write_links_page(self):
        output_file = self._cache_dir / 'links.html'
        with output_file.open('w') as fp:
            fp.write('<meta charset="utf-8"><ul>\n')
            for url, filename in self._files.items():
                path = str(self._cache_dir / filename)
                tree = html5lib.parse(open(path, 'rb'), namespaceHTMLElements=False)
                title = tree.find('.//title').text
                html = """<li>
                    <a href="%s">%s</a> - %s - %s
                </li>""" % (filename, url, title, filename)
                fp.write(html.strip() + '\n')
            fp.write('</ul>')

    def build_ebook(self, output_file, add_page_markers=True):
        if not self._files:
            self._files = self.import_links_page()
        root_node = self.get_content_tree(self.get_index_doc())

        if add_page_markers:
            fp = PagedFileWriter(output_file)
        else:
            fp = open(output_file, 'w')

        # Write tree to file.
        with fp:
            fp.write('# %s\n\n' % self.title)
            fp.write('作者：%s\n\n' % self.author)

            stack = deque()
            stack.append((1, root_node))

            while stack:
                level, node = stack.pop()
                if node.title != 'root':
                    hashes = '#' * level
                    fp.write('%s %s\n\n' % (hashes, node.title))
                    if node.content:
                        # Strip any leading and trailing newlines.
                        fp.write(node.content.strip('\n') + '\n\n')

                for child in reversed(node.children):
                    stack.append((level+1, child))


    def import_links_page(self):
        doc = get_doc_from_file(self._cache_dir / 'links.html')
        res = OrderedDict()
        for anchor in doc('a'):
            res[anchor.text_content()] = anchor.get('href')
        return res

    def get_content_tree(self, doc):
        """
        Given the index document as a PyQuery object, return content tree.
        """
        raise NotImplementedError


def get_doc_from_file(path):
    """
    Given the path to an HTML file, return a PyQuery object that provides an
    interface to its DOM.
    """
    if isinstance(path, Path):
        path = str(path)

    # First get an xml.etree object.
    tree = html5lib.parse(open(path, 'rb'), namespaceHTMLElements=False)

    # Convert to lxml.html object so that we can take advantage of the
    # .text_content() method, which captures whitespace.
    tree2 = lxml.html.fromstring(xml.etree.ElementTree.tostring(tree))
    return PyQuery(tree2)


def get_default_cache_root_dir():
    import os.path as op
    import tempfile
    if op.exists('/tmp'):
        return Path('/tmp')
    else:
        return Path(tempfile.gettempdir())


class Node:
    def __init__(self, title):
        self.title = title
        self.content = None
        self.children = []

    def append(self, node):
        self.children.append(node)

    @property
    def lastchild(self):
        return self.children[-1]

    def __str__(self):
        res = self.title
        if self.content:
            res += ' (%d characters)' % len(self.content)
        if self.children:
            res += ' (%d children)' % len(self.children)
        return res
