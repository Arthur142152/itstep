class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def info(self):
        print(self.name,self.price,' грн, в наявності: ',self.stock,' шт.')


class Cart:
    def __init__(self):
        self.items = []

    def add_product(self, product, quantity):
        if product.stock >= quantity:
            self.items.append((product, quantity))
            product.stock -= quantity
            print('Додано' ,quantity, ' шт.',product.name,' до кошика.')
        else:
            print("Недостатньо товару в наявності.")

    def remove_product(self, product):
        self.items = [item for item in self.items if item[0] != product]
        print('Товар',product.name,' видалено з кошика.')

    def total_price(self):
        total = sum(product.price * quantity for product, quantity in self.items)
        print('Загальна вартість: ',total,' грн ')

    def show_cart(self):
        for product, quantity in self.items:
            print(product.name,quantity,' шт.',product.price * quantity,' грн ')
        self.total_price()
product1 = Product("Ноутбук", 30000, 5)
product2 = Product("Смартфон", 15000, 10)

cart = Cart()
cart.add_product(product1, 2)
cart.add_product(product2, 1)
cart.show_cart()


class BankAccount:
    def __init__(self, owner, account_number, balance=0):
        self.owner = owner
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(' Поповнено ',amount,' грн. Новий баланc: ',self.balance,' грн ')

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(' Знято ',amount,' грн.  Новий баланс: ',self.balance, ' грн ')
        else:
            print("Недостатньо коштів на рахунку.")

    def info(self):
        print(' Рахунок ',self.account_number,' власник: ',self.owner,' баланс: ',self.balance,' грн ')


class Bank:
    def __init__(self):
        self.accounts = {}

    def add_account(self, account):
        self.accounts[account.account_number] = account
        print(' Рахунок ',account.account_number,' додано до банку.')

    def transfer(self, from_acc, to_acc, amount):
        if from_acc in self.accounts and to_acc in self.accounts:
            if self.accounts[from_acc].balance >= amount:
                self.accounts[from_acc].withdraw(amount)
                self.accounts[to_acc].deposit(amount)
                print(' Переказ ',amount,' грн з рахунку ',from_acc,' на рахунок ',to_acc,'успішний.')
            else:
                print("Недостатньо коштів для переказу.")
        else:
            print("Один або обидва рахунки не знайдені.")
account1 = BankAccount("Іван", "888", 1000)
account2 = BankAccount("Марія", "777", 500)
bank = Bank()
bank.add_account(account1)
bank.add_account(account2)
bank.transfer("888", "777", 300)
account1.info()
account2.info()