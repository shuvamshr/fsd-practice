class In:
    def nextLine(inputText):
        return input(inputText)

    def nextInt(inputText):
        return int(input(inputText))

    def nextDouble(inputText):
        return float(input(inputText))

    def nextChar():
        return chr(input("Start banking(d/w/s/x/help): "))


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
        self.choice = In.nextChar
        self.balance = float(1000)

    def deposit(self):
        deposit = In.nextDouble("Amount to deposit $")
        self.balance += deposit
        print(f'>> Amount deposited ${deposit}')

    def withdraw(self):
        withdraw = float(input("Amount to withdraw $"))
        if withdraw <= self.balance:
            self.balance -= withdraw
            print(f'>> Amount withdrawn ${withdraw}')
        else:
            print('>> Insufficient funds')

    def viewBalance(self):
        print(f'>> Current balance ${self.balance}')

    def help(self):
        print("d: Make a deposit")
        print("w: Withdraw fund")
        print("s: Show current balance")
        print("x: Exit system")

    def run(self):

        while self.choice != 'x':
            match self.choice:
                case 'd':
                    self.deposit()
                case 'w':
                    self.withdraw()
                case 's':
                    self.viewBalance()
                case 'help':
                    self.help()
                case _:
                    print(">> Unknown choice!")

            print()
            self.choice = input("Start Banking(d/w/s/x/help): ")


b1 = Bank()
b1.run()
