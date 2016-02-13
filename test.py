from urlpath import URL
from shu import BookScraper

class MyBookScraper(BookScraper):
    index_url = 'http://www.kanunu8.com/wuxia/201103/2336.html'
    title = '寻秦记'
    author = '黄易'

    def get_links(self, doc):
        root = URL(self.index_url).parent
        anchors = doc("td a[href ^= '2336']")
        for anchor in anchors:
            yield str(root / anchor.get('href'))

    # def get_content_tree(self, doc):
    #     pass

if __name__ == '__main__':
    scraper = MyBookScraper('books/xunqinji')
    # scraper.download()
    scraper.build_ebook('xunqinji.txt')
