from urlpath import URL
from shu import KanunuScraper, Node


class MyBookScraper(KanunuScraper):
    index_url = 'http://www.kanunu8.com/wuxia/201103/2336.html'
    title = '寻秦记'
    author = '黄易'
    index_table_selector = 'table[cellpadding="7"] a'

    def get_content_tree(self, doc):
        root = Node(title='root')

        # The table that contains the scroll and chapter titles.
        table = doc('table[cellpadding="7"]')

        for td in table('td'):
            # Ignore empty cells.
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
                chapter.content = doc('p')[0].text_content()

                root.lastchild.append(chapter)

        return root


if __name__ == '__main__':
    scraper = MyBookScraper('books/xunqinji')
    scraper.download()
    scraper.build_ebook('xun qin ji.txt', add_page_markers=True)
