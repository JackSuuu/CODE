
# 定义一个 class 银行账户
# 包含变量，余额，姓名，账号
# 包含Function: 转账，存款

# 初始化银行账户 A and B

# 执行 A存款
# 执行 A转账给B

class Bank:
    def __init__(self, name, deposit, account):
        self.name = name
        self.deposit = deposit
        self.account = account

    def transfer(self, B, money):
        pass

    def withdraw(self, account, money):
        pass


bankA = Bank('Jack', 100, 101)
print(bankA.name)
