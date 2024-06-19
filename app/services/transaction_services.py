from app.models import accounts
from app.errors import InvalidUsage
from flask import current_app


def transfer_service(data):
    from_account_id = data.get('from_account_id')
    to_account_id = data.get('to_account_id')
    amount = data.get('amount')

    if from_account_id is None or to_account_id is None or amount is None:
        raise InvalidUsage('Invalid input', status_code=400)

    from_account = accounts.get(from_account_id)
    to_account = accounts.get(to_account_id)

    if from_account is None or to_account is None:
        raise InvalidUsage('Account not found', status_code=404)

    if from_account.currency != to_account.currency:
        raise InvalidUsage('Currency mismatch', status_code=400)

    if from_account.balance < amount:
        raise InvalidUsage('Insufficient funds', status_code=400)

    from_account.balance -= amount
    to_account.balance += amount

    current_app.logger.info(
        f'Transfer: From Account {from_account_id} to Account {to_account_id}, Amount {amount}, From Balance {from_account.balance}, To Balance {to_account.balance}, Currency {from_account.currency}')

    return {'from_account_id': from_account_id, 'from_balance': from_account.balance, 'to_account_id': to_account_id, 'to_balance': to_account.balance}, 200
