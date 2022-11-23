from controllers.user_controller import UserController
from controllers.split_controller import SplitController
from controllers.expense_controller import ExpenseController

from services.user_service import UserService
from services.split.percent_split_service import PercentSplitService
from services.split.equal_split_service import EqualSplitService
from services.split.exact_split_service import ExactSplitService
from services.expense.percent_expense_service import PercentExpenseService
from services.expense.equal_expense_service import EqualExpenseService
from services.expense.exact_expense_service import ExactExpenseService

user_controller = UserController(UserService())
user1 = user_controller.add_user('u1', 'User1', 'user1@gmail.com',
                                 mobile_number='+911111')
user2 = user_controller.add_user('u2', 'User2', 'user2@gmail.com',
                                 mobile_number='+912222')
user3 = user_controller.add_user('u3', 'User3', 'user3@gmail.com',
                                 mobile_number='+913333')
user4 = user_controller.add_user('u4', 'User4', 'user4@gmail.com',
                                 mobile_number='+914444')
user_objs = [user1, user2, user3, user4]

while True:

    input_command = input("Enter something: ")
    if input_command == "quit":
        break
    else:
        user_input = input_command.split(' ')
        input_type = user_input[0]
        if input_type == 'SHOW':
            if len(user_input) > 1:
                user_id = user_input[1]
                ExpenseController.get_user_balance(user_id)
            else:
                for each_user in user_objs:
                    ExpenseController.get_user_balance(
                        each_user.id, lending_enabed=False)

        elif input_type == 'EXPENSE':
            paid_by = user_input[1]
            amount = int(user_input[2])
            num_of_users = int(user_input[3])
            users_end_idx = 3+num_of_users
            users_list = user_input[4:users_end_idx+1]
            expense_type = user_input[users_end_idx+1]
            splits_array = []

            if expense_type == 'EQUAL':
                # EXPENSE u1 1000 4 u1 u2 u3 u4 EQUAL
                # splits = user_input[users_end_idx+2:]
                split_controller = SplitController(EqualSplitService())
                expense_controller = ExpenseController(EqualExpenseService())
                split_objects = []
                for each_user_id in users_list:
                    user_obj = user_controller.user_service.users.get(
                        each_user_id)
                    split_obj = split_controller.add_split(
                        user_obj, amount=amount/num_of_users)
                    split_objects.append(split_obj)
                expense_controller.add_expense(
                    amount, paid_by, split_objects, None)
            elif expense_type == 'EXACT':
                # EXPENSE u3 1250 2 u1 u3 EXACT 370 880
                splits = user_input[users_end_idx+2:]
                split_controller = SplitController(ExactSplitService())
                expense_controller = ExpenseController(
                    ExactExpenseService())
                split_objects = []
                for split_num, each_split in enumerate(splits):
                    user_obj = user_controller.user_service.users.get(
                        users_list[split_num])
                    split_obj = split_controller.add_split(
                        user_obj, amount=int(each_split))
                    split_objects.append(split_obj)

                expense_controller.add_expense(
                    amount, paid_by, split_objects, None)

            elif expense_type == 'PERCENT':
                # EXPENSE u3 1200 4 u1 u2 u3 u4 PERCENT 40 20 20 20
                splits = user_input[users_end_idx+2:]
                split_controller = SplitController(PercentSplitService())
                expense_controller = ExpenseController(PercentExpenseService())
                split_objects = []
                for split_num, each_split in enumerate(splits):
                    user_obj = user_controller.user_service.users.get(
                        users_list[split_num])
                    split_obj = split_controller.add_split(
                        user_obj, percent=int(each_split), total_amount=amount)
                    split_objects.append(split_obj)

                expense_controller.add_expense(
                    amount, paid_by, split_objects, None)

            # ExpenseController(PercentExpenseService()).get_user_balance('u1')
            print('-------------')

    # import pdb
    # pdb.set_trace()
