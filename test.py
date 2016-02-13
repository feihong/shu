from urlpath import URL
from shu import BookScraper, Node, print_node

class MyBookScraper(BookScraper):
    index_url = 'http://www.kanunu8.com/wuxia/201103/2336.html'
    title = '寻秦记'
    author = '黄易'
    base_url = URL(index_url).parent

    def get_links(self, doc):
        anchors = doc("td a[href ^= '2336']")
        for anchor in anchors:
            yield str(self.base_url / anchor.get('href'))

    def get_content_tree(self, doc):
        root = Node(title='root')

        table = doc('table[cellpadding="7"]')
        for td in table('td'):
            if not td.getchildren():
                continue
            if td.find('strong') is not None:
                root.append(Node(title=td.text_content()))
            else:
                scroll = root.lastchild.title
                title = '%s: %s' % (scroll, td.text_content())
                chapter = Node(title=title)

                url = self.base_url / td.find('a').get('href')
                doc = self.get_doc(url)
                chapter.content = doc('p')[0].text_content().strip()

                root.lastchild.append(chapter)

        return root


if __name__ == '__main__':
    scraper = MyBookScraper('books/xunqinji')
    scraper.download()
    scraper.build_ebook('xunqinji.txt')
