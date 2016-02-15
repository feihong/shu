from shu import KanunuMultiVolumeScraper


class MyBookScraper(KanunuMultiVolumeScraper):
    index_url = 'http://www.kanunu8.com/wuxia/201103/2336.html'
    title = '寻秦记'
    author = '黄易'
    index_table_selector = 'table[cellpadding="7"]'


if __name__ == '__main__':
    # 290 chapters, oveeer 2500 pages.
    scraper = MyBookScraper('cache')
    scraper.download()
    scraper.build_ebook('xun qin ji.txt')
