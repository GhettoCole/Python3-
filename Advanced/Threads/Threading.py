import threading
import time
import random


class BankAccount(threading.Thread):
    accBalance = 10000

    def __init__(self, name, moneyRequest):
        threading.Thread.__init__(self)
        self.name = name
        self.moneyRequest = moneyRequest

    def run(self):
        threadLock.acquire()

        BankAccount.getMoney(self)

        threadLock.release()

    @staticmethod
    def getMoney(customer):
        print("{} tries to withdraw ${} at {}".format(customer.name, customer.moneyRequest,
                                                      time.strftime("%H:%M:%S", time.gmtime())))

        if BankAccount.accBalance - customer.moneyRequest >= 0:
            BankAccount.accBalance -= customer.moneyRequest
            print("New account balance: ${}".format(BankAccount.accBalance))
        else:
            print("Sorry {} Not enough money in the account".format(customer.name))
            print("Current balance: ${}".format(BankAccount.accBalance))

        time.sleep(5)


threadLock = threading.Lock()

given = BankAccount("Given Lepita", 3500)
golddigger = BankAccount("Gold digger", 100000)
lerato = BankAccount("Lerato", 350)
remo = BankAccount("Remoneilwe", 790)

given.start()
golddigger.start()
lerato.start()
remo.start()

given.join()
golddigger.join()
lerato.join()
remo.join()

print("The execution has ended!")
