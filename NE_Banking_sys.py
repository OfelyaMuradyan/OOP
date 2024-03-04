class CustomerAccount:
    def __init__(self, customer_id, customer_name, account_balance):
        self.customer_id = customer_id
        self.customer_name = customer_name
        self.account_balance = account_balance
        self.transaction_log = TransactionLog()

    def deposit(self, amount):
        self.account_balance += amount 
        self.transaction_log.log_transaction(['deposit', amount])

    def withdraw(self, amount):
        self.account_balance -= amount
        self.transaction_log.log_transaction(['withdraw', amount])

class TransactionLog:
    def __init__(self):
        self.ls = []

    def log_transaction(self,transaction_details):
        self.ls.append(transaction_details)

cust_account = CustomerAccount(5,'James', 700)
cust_account.deposit(5000)
cust_account.withdraw(-800)

print(cust_account.transaction_log.ls)