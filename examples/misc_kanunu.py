from shu.kanunu import make_ebook


if __name__ == '__main__':
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
