class Bank:
    def __init__(self, account_number, balance= 0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f'{amount}deposited successfully')
        else:
            print('deposit must be positive')

    def withdraw(self, amount):
        if amount > self.balance:
            print('insufficient balance')
        elif amount > 0:
            self.balance -= amount
            print(f'{amount} has been withdrawn')
        else:
            print('withdrawal must be positive')

    def show_balance(self):
        print(f'account {self.account_number} balance {self.balance}')

account = Bank(account_number='2098756551', balance=0)
account.deposit(100)
account.withdraw(65)
account.show_balance()


def names(people):
    qualified_names = []

    for individual in people:
        if individual.get('age', 0) > 25 and individual.get('city') == 'New York':
            qualified_names.append(individual.get('name'))

    return qualified_names


people_list = [
    {'name': 'Phillips', 'age': 50, 'city': 'New York'},
    {'name': 'Kenny', 'age': 22, 'city': 'Los Angeles'},
    {'name': 'Ola', 'age': 28, 'city': 'New York'},
    {'name': 'Gideon', 'age': 23, 'city': 'New York'},
    {'name': 'Dele', 'age': 45, 'city': 'Los Angeles'}
]

result = names(people_list)
print(result)
