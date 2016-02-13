from shu import KanunuScraper


class MyBookScraper(KanunuScraper):
    index_url = 'http://www.kanunu8.com/files/yuanchuang/200806/627.html'
    title = '鬼吹灯（盗墓者的经历）'
    author = '本物天下霸唱'


if __name__ == '__main__':
    scraper = MyBookScraper('books/gui chui deng')
    scraper.download()
    scraper.build_ebook('gui chui deng.txt')
