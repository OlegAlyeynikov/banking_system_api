class Account:
    def __init__(self, account_id, name, initial_balance, currency):
        self.account_id = account_id
        self.name = name
        self.balance = initial_balance
        self.currency = currency


class User:
    def __init__(self, user_id, username, password):
        self.user_id = user_id
        self.username = username
        self.password = password


accounts = {}
next_account_id = 1
users = {}
next_user_id = 1
