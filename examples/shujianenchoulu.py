from shu import KanunuScraper


class MyBookScraper(KanunuScraper):
    index_url = 'http://www.kanunu8.com/book/4600/index.html'
    title = '书剑恩仇录'
    author = '金庸'


if __name__ == '__main__':
    scraper = MyBookScraper('books/shu jian en chou lu')
    scraper.download()
    scraper.build_ebook('shu jian en chou lu.txt', add_page_markers=True)
