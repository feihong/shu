from shu import KanunuMultiVolumeScraper, make_ebook


class ShiZongZuiScraper(KanunuMultiVolumeScraper):
    index_url = 'http://www.kanunu8.com/book/4514/index.html'
    title = '十宗罪'
    author = '蜘蛛'


# 60 chapters, almost 300 pages.
make_ebook(ShiZongZuiScraper, output_file='books/shi zong zui')


class ZangDiMiMaScraper(KanunuMultiVolumeScraper):
    index_url = 'http://www.kanunu8.com/files/chinese/201103/1856.html'
    title = '藏地密码全集'
    author = '何马'
    index_table_selector = "table[cellpadding='12']"


# 75 chapters, almost 2300 pages.
make_ebook(ZangDiMiMaScraper, output_file='books/zang di mi ma')
