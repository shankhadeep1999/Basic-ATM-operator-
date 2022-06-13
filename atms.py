class Atm:

    def __init__(self) -> None:
        self.balence=0
        self.pin=""

    def manu(self):
        user=input("""What you want?
        1)Creat pin
        2)check Balence
        3)Deposit
        4)Withdraw
        5)Exit
""")

        if user=="1":
            self.creat_pin()
        elif user=="2":
            self.balance_check()
        elif user=="3":
            self.deposit()
        elif user=="4":
            pass
        else:
            print("Exit")

    def creat_pin(self):
        self.pin=input("Enter your pin")
        print("Pin generate Sucessfull")


    def deposit(self):
        cus=input("Emter your pin")
        if self.pin==cus:
            amount=int(input("Enter your amount: "))
            self.balence +=amount
        else:
            print("please check your pin")


    def balance_check(self):
        cus=input("Emter your pin")
        if self.pin==cus:
            print(self.balence)
        else:
            print("please check your pin")

    def withdraw(self):
        cus=input("Emter your pin")
        if self.pin==cus:
            amounts=int(input("Enter your amount"))
            if amounts<=self.balence:
                self.balence=self.balence-amounts
                print("Transctions Sucessfull")
            else:
                print("Insufficent Balence")
        else:
            print("Please Check your pin")

sbi = Atm()

sbi.manu()