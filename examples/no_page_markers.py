"""
Generate the ebook without any page markers.

"""

from shu import KanunuScraper


class MyBookScraper(KanunuScraper):
    index_url = 'http://www.kanunu8.com/book3/7065/index.html'
    title = '黄金时代'
    author = '王小波'


if __name__ == '__main__':
    # Very short, has 11 chapters.
    scraper = MyBookScraper()
    scraper.download()
    scraper.build_ebook('huangjin shidai.txt', add_page_markers=False)
