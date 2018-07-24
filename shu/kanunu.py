from urlpath import URL
from .base import BookScraper, Node


def make_ebook(index_url, title, author, output_file, **kwargs):
    # Because of how scoping works in Python, you need to use different variable
    # names. See bit.ly/1Th5SRl.
    args = (index_url, title, author)

    scraper = KanunuScraper(index_url=index_url, title=title, author=author)
    if 'index_table_selector' in kwargs:
        scraper.index_table_selector = kwargs.pop('index_table_selector')
    scraper.download()
    scraper.build_ebook(output_file, **kwargs)
    return scraper


class KanunuScraper(BookScraper):
    # CSS selector for table that contains all the links.
    index_table_selector = 'table[cellpadding="8"]'

    def __init__(self, **kwargs):
        super(KanunuScraper, self).__init__(**kwargs)
        self.base_url = URL(self.index_url).parent

    def get_title_and_links(self, doc):
        table = doc(self.index_table_selector)
        for anchor in table('a'):
            yield (
                anchor.text_content(),
                str(self.base_url / anchor.get('href')))

    def get_links(self, doc):
        for title, link in self.get_title_and_links(doc):
            yield link

    def get_content_tree(self, doc):
        root = Node(title='root')
        for title, link in self.get_title_and_links(doc):
            doc = self.get_doc(link)
            chapter = Node(title=title)
            chapter.content = doc('p')[0].text_content()
            root.append(chapter)
        return root


class KanunuMultiVolumeScraper(KanunuScraper):
    def get_content_tree(self, doc):
        root = Node(title='root')

        table = doc(self.index_table_selector)
        for td in table('td'):
            # Ignore empty cells.
            if not td.getchildren():
                continue

            if td.find('strong') is not None:
                root.append(Node(title=td.text_content()))
            else:
                volume = root.lastchild.title
                title = '%s: %s' % (volume, td.text_content())
                chapter = Node(title=title)

                url = self.base_url / td.find('a').get('href')
                doc = self.get_doc(url)
                chapter.content = doc('p')[0].text_content()

                root.lastchild.append(chapter)

        return root
