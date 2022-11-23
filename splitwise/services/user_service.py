from .user_service_interface import IUserService
from models.user import User


class UserService(IUserService):
    users = {}

    def add_user(self, id, name):

        user = User(id)
        user.name = name

        self.__class__.users[user.id] = user

        return user
