from shu import KanunuMultiVolumeScraper, make_ebook


def make_single_volume_ebooks():
    from shu.kanunu import make_ebook

    # More than 1000 pages, 101 chapters.
    make_ebook(
        index_url='http://www.kanunu8.com/files/old/2011/2448.html',
        title='西游记',
        author='吴承恩',
        output_file='xi you ji.txt',
    )

    # About 360 pages, 33 chapters.
    make_ebook(
        index_url='http://www.kanunu8.com/files/chinese/201102/1777.html',
        title='明朝那些事儿1',
        author='当年明月',
        output_file='mingchao na xie shi 1.txt',
    )

    # More than 1200 pages, 120 chapters.
    make_ebook(
        index_url='http://www.kanunu8.com/files/old/2011/2449.html',
        title='红楼梦',
        author='曹雪芹',
        output_file='hong lou meng.txt',
    )

if __name__ == '__main__':
    make_single_volume_ebooks()

    class ShiZongZuiScraper(KanunuMultiVolumeScraper):
        index_url = 'http://www.kanunu8.com/book/4514/index.html'
        title = '十宗罪'
        author = '蜘蛛'

    # 60 chapters, almost 300 pages.
    make_ebook(ShiZongZuiScraper, output_file='shi zong zui.txt')

    class ZangDiMiMaScraper(KanunuMultiVolumeScraper):
        index_url = 'http://www.kanunu8.com/files/chinese/201103/1856.html'
        title = '藏地密码全集'
        author = '何马'
        index_table_selector = "table[cellpadding='12']"

    # 75 chapters, almost 2300 pages.
    make_ebook(ZangDiMiMaScraper, output_file='zang di mi ma.txt')
