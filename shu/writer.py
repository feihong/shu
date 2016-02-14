class PagedFileWriter:
    """
    File-like writer that adds page markers at specific intervals.

    """
    limit = 700

    def __init__(self, filename):
        self.fp = None
        self.filename = filename
        self.page = 1

    def write(self, text):
        if text.startswith('#'):
            self.fp.write(text)
            return

        for chunk in self._get_chunks(text):
            self.fp.write(chunk)
            self.fp.write('\n\n-%d-\n\n' % self.page)
            self.page += 1

    def __enter__(self):
        self.fp = open(self.filename, 'w')
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.fp.close()

    def _get_chunks(self, text):
        if len(text) < self.limit:
            yield text
            raise StopIteration

        while len(text):
            yield text[:self.limit]
            text = text[self.limit:]
