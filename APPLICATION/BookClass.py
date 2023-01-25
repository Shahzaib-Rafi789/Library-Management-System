


class Book:
        # self.isbn=isbn
    def __init__(self,title,authors,language,publisher,publishYear,fileFormat,fileSize):
        self.title=title
        self.authors=authors
        self.language=language
        # self.pages=pages
        # self.edition=edition
        self.publisher = publisher
        self.publishYear=publishYear
        # self.isbn=isbn
        self.fileFormat=fileFormat
        self.fileSize=fileSize
    def __str__(self):
        return f"Title is {self.title}, Author(s) is {self.authors},Language is {self.language},Publisher is {self.publisher}, PublishYear is {self.publishYear},FileFormat is {self.fileFormat}, FileSize is {self.fileSize}"
        