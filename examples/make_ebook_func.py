from pathlib import Path
from shu import KanunuMultiVolumeScraper, make_ebook


def make(**kwargs):
    # Only make the ebook if it doesn't already exist.
    output_file = Path('books') / Path(kwargs.pop('output_file')).with_suffix('.txt')
    if not output_file.exists():
        class MyScraper(KanunuMultiVolumeScraper):
            index_url = kwargs['index_url']
            title = kwargs['title']
            author = kwargs['author']

        if 'index_table_selector' in kwargs:
            MyScraper.index_table_selector = kwargs['index_table_selector']

        make_ebook(MyScraper, output_file=output_file)



if __name__ == '__main__':
    # 60 chapters, <300 pages.
    make(
        index_url = 'http://www.kanunu8.com/book/4514/index.html',
        title = '十宗罪',
        author = '蜘蛛',
        output_file='shi zong zui',
    )

    # 75 chapters, <2300 pages.
    make(
        index_url = 'http://www.kanunu8.com/files/chinese/201103/1856.html',
        title = '藏地密码全集',
        author = '何马',
        index_table_selector = "table[cellpadding='12']",
        output_file='zang di mi ma',
    )
