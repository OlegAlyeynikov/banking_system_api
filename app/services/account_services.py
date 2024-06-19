from app.models import Account, accounts, next_account_id
from app.errors import InvalidUsage
from flask import current_app


def create_account_service(data):
    global next_account_id
    name = data.get('name')
    initial_balance = data.get('initial_balance')
    currency = data.get('currency', 'USD')  # Default to USD if not provided

    if name is None or initial_balance is None:
        raise InvalidUsage('Invalid input', status_code=400)

    account_id = next_account_id
    accounts[account_id] = Account(account_id, name, initial_balance, currency)
    next_account_id += 1

    return {'account_id': account_id, 'name': name, 'balance': initial_balance, 'currency': currency}, 201


def deposit_service(data):
    account_id = data.get('account_id')
    amount = data.get('amount')

    if account_id is None or amount is None:
        raise InvalidUsage('Invalid input', status_code=400)

    account = accounts.get(account_id)
    if account is None:
        raise InvalidUsage('Account not found', status_code=404)

    account.balance += amount

    current_app.logger.info(
        f'Deposit: Account {account_id}, Amount {amount}, New Balance {account.balance}, Currency {account.currency}')

    return {'account_id': account_id, 'balance': account.balance, 'currency': account.currency}, 200


def withdraw_service(data):
    account_id = data.get('account_id')
    amount = data.get('amount')

    if account_id is None or amount is None:
        raise InvalidUsage('Invalid input', status_code=400)

    account = accounts.get(account_id)
    if account is None:
        raise InvalidUsage('Account not found', status_code=404)

    if account.balance < amount:
        raise InvalidUsage('Insufficient funds', status_code=400)

    account.balance -= amount

    current_app.logger.info(
        f'Withdrawal: Account {account_id}, Amount {amount}, New Balance {account.balance}, Currency {account.currency}')

    return {'account_id': account_id, 'balance': account.balance, 'currency': account.currency}, 200
