# Banking System API

## Introduction

This is a simple banking system API implemented using Flask. The API allows users to create accounts, deposit money, withdraw money, and send money between accounts. It includes features such as JWT authentication, support for multiple currencies, transaction logging, and rate limiting to prevent abuse.

## Features

- Account creation
- Deposit money
- Withdraw money
- Transfer money between accounts
- JWT authentication
- Multiple currency support
- Transaction logging
- Rate limiting

## Requirements

- Python 3.8+
- Flask
- Flask-JWT-Extended
- Flask-Limiter
- Other dependencies listed in `requirements.txt`

## Setup

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/banking_system_api.git
   cd banking_system_api
   ```

2. **Create a virtual environment and install dependencies:**

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```
   
3. **Initialize and run the application:**

   ```bash
   python3 run.py
   ```
   This will start the Flask application on http://127.0.0.1:5000.

## Testing Using curl

1. **Register a User**

   ```bash
   curl -X POST http://127.0.0.1:5000/auth/register -H "Content-Type: application/json" -d '{"username":"test_user", "password":"test_pass"}'
   ```

2. **Login to Get JWT Token**

   ```bash
   TOKEN=$(curl -X POST http://127.0.0.1:5000/auth/login -H "Content-Type: application/json" -d '{"username":"test_user", "password":"test_pass"}' | jq -r '.access_token')
   ```
3. **Create an Account**
   
   ```bash
   curl -X POST http://127.0.0.1:5000/account/create_account -H "Content-Type: application/json" -H "Authorization: Bearer $TOKEN" -d '{"name": "Alice", "initial_balance": 100.0, "currency": "USD"}'
   ```

4. **Deposit Money**

   ```bash
   curl -X POST http://127.0.0.1:5000/account/deposit -H "Content-Type: application/json" -H "Authorization: Bearer $TOKEN" -d '{"account_id": 1, "amount": 50.0}'
   ```
   
5. **Withdraw Money**

   ```bash
   curl -X POST http://127.0.0.1:5000/account/withdraw -H "Content-Type: application/json" -H "Authorization: Bearer $TOKEN" -d '{"account_id": 1, "amount": 30.0}'
   ```

6. **Create another account to transfer money**

   ```bash
   curl -X POST http://127.0.0.1:5000/account/create_account -H "Content-Type: application/json" -H "Authorization: Bearer $TOKEN" -d '{"name": "Bob", "initial_balance": 50.0, "currency": "USD"}'
   ```
7. **Perform the transfer**

   ```bash
   curl -X POST http://127.0.0.1:5000/transaction/transfer -H "Content-Type: application/json" -H "Authorization: Bearer $TOKEN" -d '{"from_account_id": 1, "to_account_id": 2, "amount": 20.0}'
      ```

## Running Unit Tests

1. **You can run unit tests using unittest. Ensure you have a virtual environment activated and dependencies installed.**

   ```bash
   python3 -m unittest discover tests
    ```
This command will discover and run all the unit tests in the tests directory.

## Rate Limiting The API has rate limits to prevent abuse:

    Account creation: 10 requests per minute
    Deposit: 20 requests per minute
    Withdraw: 20 requests per minute
    Transfer: 10 requests per minute

## Logging

Transaction logs are saved in logs/transactions.log. You can check this file to see logs for deposits, withdrawals, and transfers.
