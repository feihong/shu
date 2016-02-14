from urlpath import URL
from .base import BookScraper, Node


class KanunuScraper(BookScraper):
    # CSS selector for table that contains all the links.
    index_table_selector = 'table[cellpadding="8"] a'

    def __init__(self, working_dir):
        super(KanunuScraper, self).__init__(working_dir)
        self.base_url = URL(self.index_url).parent

    def get_title_and_links(self, doc):
        anchors = doc(self.index_table_selector)
        for anchor in anchors:
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
