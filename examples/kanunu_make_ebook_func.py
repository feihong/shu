from pathlib import Path
from shu.kanunu import make_ebook


def make(**kwargs):
    # Only make the ebook if it doesn't already exist.
    output_file = Path('books') / Path(kwargs.pop('output_file')).with_suffix('.txt')
    print(output_file)
    if not output_file.exists():
        make_ebook(output_file=output_file, **kwargs)


if __name__ == '__main__':
    # 32 chapters.
    make(
        index_url='http://www.kanunu8.com/book3/6633/index.html',
        title='球状闪电',
        author='刘慈欣',
        output_file='qiu zhuang shan dian',
    )
    # 1000+ pages, 101 chapters.
    make(
        index_url='http://www.kanunu8.com/files/old/2011/2448.html',
        title='西游记',
        author='吴承恩',
        output_file='xi you ji',
    )
    # 360 pages, 33 chapters.
    make(
        index_url='http://www.kanunu8.com/files/chinese/201102/1777.html',
        title='明朝那些事儿1',
        author='当年明月',
        output_file='mingchao na xie shi 1',
    )
    # 1200+ pages, 120 chapters.
    make(
        index_url='http://www.kanunu8.com/files/old/2011/2449.html',
        title='红楼梦',
        author='曹雪芹',
        output_file='hong lou meng',
    )
