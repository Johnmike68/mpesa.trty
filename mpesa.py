class mpesa():
    def __init__(self):
        self.phone = "0792355950"
        self.name = "SAM KIP"
        self.balance = 100000

    def get_balance(self):
        print(f"{self.name}, your mpesa balance is {self.balance}")

    def withdraw(self):
        withdr = int(input("how much would u like to withdraw?\n"))
        print(f"{withdr} will be removed from ur balance!!!")
        print(f"your new balance is: {self.balance-withdr}")

    def deposit(self):
        depo = int(input("how much would u like to deposit?\n"))
        print(f"{depo} will be added into ur balance")
        print(f"your new balance is {depo+self.balance}")

sam = mpesa()
sam.deposit()