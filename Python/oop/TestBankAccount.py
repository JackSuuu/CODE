from BankAccount import BankAccount

Jack = BankAccount("Jack", 1001)
Sheldon = BankAccount("Sheldon", 1001)

Jack.deposit(20)
Jack.transfer(Sheldon, 10)
