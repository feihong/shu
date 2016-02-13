class PagedFileWriter:
    def __init__(self, filename):
        self.fp = None
        self.filename = filename
        self.buffer = ''

    def write(self, text):
        self.fp.write(text)

    def __enter__(self):
        self.fp = open(self.filename, 'w')
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.fp.close()
