import time
from concurrent.futures import ThreadPoolExecutor


# Each time execution gives different result
class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def withdraw(self, amount):
        if self.balance >= amount:
            new_balance = self.balance - amount
            print(f"Withdrawing Amount..{amount}...")
            # simulate a delay
            time.sleep(0.1)
            self.balance = new_balance
        else:
            raise ValueError("Insufficient Balance..")

    def deposit(self, amount):
        new_balance = self.balance + amount
        print(f"Depositing Amount..{amount}...")
        # Simulating Delay
        time.sleep(0.1)
        self.balance = new_balance


def main(num):
    account = BankAccount(1000)
    # Create a ThreadPoolExecutor and submit tasks
    with ThreadPoolExecutor(max_workers=num) as executor:
        executor.submit(account.withdraw, 900)
        executor.submit(account.withdraw, 700)
        executor.submit(account.withdraw, 500)
        executor.submit(account.withdraw, 800)
    print(f"Final Account Balance...{account.balance}")


if __name__ == "__main__":
    print("Calling Before main..")
    # Create 4 threads and submit
    main(4)
    print("Calling After main..")
