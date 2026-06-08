
class BankAccount:
    name = ''
    id = 0
    # 定义私有变量
    __balance = 0
    # 静态变量
    _bank = 'China Merchants Bank'
    _transferRate = 0.01

    # 定义构造方法
    def __init__(self, n, id1):
        self.name = n
        self.id = id1

    @staticmethod
    def getRate():
        return f'{BankAccount._bank} requires services fee {BankAccount._transferRate * 100}%'

    def deposit(self, money):
        self.__balance += money
        print(f"存款金额为: {money}, {self.name}的账户余额为: {self.__balance}$")

    def withdraw(self, money):
        if money <= self.__balance:
            self.__balance -= money
            print(f"取款金额为: {money}, {self.name}的账户余额为: {self.__balance}$")

    def get_balance(self):
        return self.__balance

    def transfer(self, account, money):
        if money <= self.__balance:
            self.withdraw(money)
            serviceFee = money * self._transferRate
            if serviceFee > 50:
                self.withdraw(50)
                print("Receive services fee 50$")
            else:
                self.withdraw(serviceFee)
                print(f"Receive services fee {serviceFee}$")
            account.deposit(money)
            print(f"transfer {money}$ to {account.name} successfully")


Sheldon = BankAccount('Sheldon', 1001)
Sheldon.deposit(100000)
Jack = BankAccount('Jack', 1002)
print(Sheldon.getRate())
Sheldon.transfer(Jack, 10000)
