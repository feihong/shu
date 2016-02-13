from urlpath import URL
from shu import BookScraper, Node, print_node


class MyBookScraper(BookScraper):
    index_url = 'http://www.kanunu8.com/book/4600/index.html'
    title = '书剑恩仇录'
    author = '金庸'
    base_url = URL(index_url).parent

    def get_title_and_links(self, doc):
        anchors = doc("table[cellpadding='8'] a")
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


if __name__ == '__main__':
    scraper = MyBookScraper('books/shu jian en chou lu')
    scraper.download()
    scraper.build_ebook('shu jian en chou lu.txt')
