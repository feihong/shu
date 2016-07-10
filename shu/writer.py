class PagedFileWriter:
    """
    File-like writer that adds page markers at specific intervals.

    """
    limit = 700         # break every 700 characters

    def __init__(self, output_file):
        self.fp = None
        self.output_file = output_file
        self.page = 1

    def write(self, text):
        # Never page break on headers.
        if text.startswith('#'):
            self.fp.write(text)
            return

        for chunk in self._get_chunks(text):
            self.fp.write(chunk)
            self.fp.write('\n\n-%d-\n\n' % self.page)
            self.page += 1

    def __enter__(self):
        self.fp = self.output_file.open('w')
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
