class ExpenseMetadata:
    def __init__(self, id, name, img_url, notes):
        self.__id = id
        self.__name = name
        self.__img_url = img_url
        self.__notes = notes

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @id.setter
    def name(self, value):
        self.__name = value

    @property
    def img_url(self):
        return self.__img_url

    @img_url.setter
    def img_url(self, value):
        self.__img_url = value

    @property
    def notes(self):
        return self.__notes

    @notes.setter
    def notes(self, value):
        self.__notes = value
