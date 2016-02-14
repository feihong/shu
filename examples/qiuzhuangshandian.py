from shu import KanunuScraper


class MyBookScraper(KanunuScraper):
    index_url = 'http://www.kanunu8.com/book3/6633/index.html'
    title = '球状闪电'
    author = '刘慈欣'


if __name__ == '__main__':
    # Has 32 chapters.
    scraper = MyBookScraper()
    scraper.download()
    scraper.build_ebook('qiu zhuang shan dian.txt', add_page_markers=True)
