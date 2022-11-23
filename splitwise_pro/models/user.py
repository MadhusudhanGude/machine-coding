class User:
    def __init__(self, id, name, email, mobile_number):
        self.__id = id
        self.__name = name
        self.__email = email
        self.__mobile_number = mobile_number

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
    def email(self):
        return self.__email

    @email.setter
    def email(self, value):
        self.__email = value

    @property
    def mobile_number(self):
        return self.__mobile_number

    @mobile_number.setter
    def mobile_number(self, value):
        self.__mobile_number = value
