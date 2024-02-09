class Account:
  def __init__(self, owner, balance):
    self.owner = owner
    self.balance = balance
  def info(self):
    print(self.owner)
    print(self.balance)
  def deposit(self, amount):
    self.balance += amount
  def withdraw(self, amount):
    if self.balance - amount < 0:
      print('no enough money to withdraw')
    else:
      self.balance -= amount
rob = Account('Rob', 25000)
rob.info()
rob.withdraw(26000)
rob.deposit(1000)
rob.withdraw(26000)
rob.info()