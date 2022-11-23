from models.user import User


class UserService:
    users = {}

    def add_user(self, id, name, email, mobile_number):

        user = User(id, name, email, mobile_number)
        user.name = name
        self.__class__.users[user.id] = user
        return user
