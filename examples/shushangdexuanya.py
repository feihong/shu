from urlpath import URL
from shu import BookScraper, Node


class MyBookScraper(BookScraper):
    index_url = 'http://www.xiaoshuocity.com/book/01613/ssdxy_806879/chapter.html'
    title = '树上的悬崖'
    author = '宋毓建'
    base_url = URL(index_url)

    def get_title_and_links(self, doc):
        anchors = doc('.con a')
        for anchor in anchors:
            yield (
                anchor.text_content(),
                str(self.base_url.joinpath(anchor.get('href')))
            )

    def get_links(self, doc):
        for title, link in self.get_title_and_links(doc):
            yield link

    def get_content_tree(self, doc):
        root = Node(title='root')

        for title, link in self.get_title_and_links(doc):
            chapter = Node(title)
            doc = self.get_doc(link)
            texts = (p.text_content() for p in doc('.content p'))
            chapter.content = '\n\n'.join(
                t.strip('\n') for t in texts if t.strip())
            root.append(chapter)

        return root


if __name__ == '__main__':
    # 66 chapters, about 200 pages.
    scraper = MyBookScraper('cache')
    scraper.download()
    scraper.build_ebook('shu shang de xuan ya.txt', add_page_markers=True)
