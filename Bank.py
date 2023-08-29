class Account:
    def __init__(self, type, balance):
        self.type = type
        self.balance = balance


class Customer:
    def __init__(self, name):
        self.name = name
        self.customers = []


class Manager:
    def __init__(self, name):
        self.name = name
        self.admin = []


class Bank:
    def __init__(self):
        self.customers = []
        self.admin = Manager('John')

    def run(self):

        choice = input("Start Banking(d/w/s/x): ")

        balance = float(1000)

        while choice != 'x':
            match choice:
                case 'd':
                    deposit = float(input("Amount to deposit $"))
                    balance += deposit
                    print(f'>> Amount deposited ${deposit}')

                case 'w':
                    withdraw = float(input("Amount to withdraw $"))
                    if withdraw <= balance:
                        balance -= withdraw
                        print(f'>> Amount withdrawn ${withdraw}')
                    else:
                        print('>> Insufficient funds')

                case 's':
                    print(f">> Starting Balance ${balance}")

                case _: print(">> Unknown choice!")

            print()
            choice = input("Start Banking(d/w/s/x): ")


b1 = Bank()
b1.run()
