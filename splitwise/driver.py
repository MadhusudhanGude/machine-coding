
from controllers.user_controller import UserController
from controllers.group_controller import GroupController
from controllers.bill_controller import BillController

from services.bill_service import BillService
from services.user_service import UserService
from services.group_service import GroupService

user_controller = UserController(UserService())
group_controller = GroupController(GroupService())
bill_controller = BillController(BillService())

user1 = user_controller.add_user('user1', 'pawan')
user2 = user_controller.add_user('user2', 'gyan')
user3 = user_controller.add_user('user3', 'abhi')
user4 = user_controller.add_user('user4', 'nishant')
user5 = user_controller.add_user('user5', 'ds')

members = [user1, user2, user3, user4, user5]
group1 = group_controller.add_group('group1', 'avengers', members)

paidBy = {'user1': 200, 'user2': 100, 'user3': 50, 'user4': 50, 'user5': 100}
contribution = {'user1': 100, 'user2': 100,
                'user3': 100, 'user4': 100, 'user5': 100}

bill1 = bill_controller.add_bill('bill1', 'group1', 500, contribution, paidBy)

balance = bill_controller.get_user_balance('user1')
print(balance)
