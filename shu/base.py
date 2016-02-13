from collections import OrderedDict
from pathlib import Path
import requests
import lxml.html
from pyquery import PyQuery


class BookScraper:
    title = 'TITLE'
    author = 'AUTHOR'
    index_url = ''

    def __init__(self, working_dir):
        self.working_dir = Path(working_dir)
        if not self.working_dir.exists():
            self.working_dir.mkdir(parents=True)

        self._session = requests.Session()

        # Map of URLs to file names.
        self._files = OrderedDict()

    def download(self):
        doc = self.get_index_page()

        for link in self.get_links(doc):
            self.download_page(link)

        self.write_links_page()

    def get_page(self, url):
        """
        Given a URL, get the cached contents of the page converted to a PyQuery
        object.
        """
        path = self.working_dir / self._files[url]
        return get_doc_from_file(path)

    def get_index_page(self):
        """
        Download the index page if necessary and return it as a PyQuery object.
        """
        index_file = self.working_dir / 'index.html'
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

        print('Downloading %s to %s' % (url, filename))

        (self.working_dir / filename).write_bytes(response.content)

        if not filename in self._files:
            self._files[url] = filename

    def write_links_page(self):
        output_file = self.working_dir / 'links.html'
        with output_file.open('w') as fp:
            fp.write('<meta charset="utf-8"><ul>\n')
            for url, filename in self._files.items():
                path = str(self.working_dir / filename)
                tree = lxml.html.parse(path)
                title = tree.find('//title').text_content()
                html = """<li>
                    <a href="%s">%s</a> - %s - %s
                </li>""" % (filename, url, title, filename)
                fp.write(html.strip() + '\n')
            fp.write('</ul>')

    def build_ebook(self, output_file):
        if not self._files:
            self._files = self.import_links_page()
        tree = self.get_content_tree()
        # write tree to file

    def import_links_page(self):
        doc = get_doc_from_file(self.working_dir / 'links.html')
        res = OrderedDict()
        for anchor in doc('a'):
            res[anchor.text_content()] = anchor.get('href')
        return res

    def get_content_tree(self):
        raise NotImplementedError


def get_doc_from_file(path):
    """
    Given the path to an HTML file, return a PyQuery object that provides an
    interface to its DOM.
    """
    if isinstance(path, Path):
        path = str(path)
    tree = lxml.html.parse(path)
    return PyQuery(tree.getroot())


class Node:
    def __init__(self, title):
        self.title = title
        self.content = None
        self.children = []

    def __str__(self):
        res = self.title
        if self.children:
            res += ' (%d children)' % len(self.children)
        return res
