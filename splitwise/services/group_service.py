from .group_service_interface import IGroupService
from models.group import Group
from abc import ABC, abstractmethod


class GroupService(IGroupService):
    groups = {}

    def add_group(self, id, name, members):
        group = Group(id, name, members)
        self.__class__.groups[id] = group

        return group
