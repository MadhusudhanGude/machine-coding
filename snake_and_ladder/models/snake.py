class Snake:
    def __init__(self, id, start, end):
        self.__id = id
        self.__start = start
        self.__end = end

    @property
    def id(self):
        return self.__id

    @property
    def start(self):
        return self.__start

    @property
    def end(self):
        return self.__end

    # @start.setter
    # def name(self, value):
    #     self.__start = value

    # @end.setter
    # def end(self, value):
    #     self.__end = value
