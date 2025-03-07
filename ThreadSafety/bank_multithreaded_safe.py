import time
import threading
from concurrent.futures import ThreadPoolExecutor


"""
A threading.Lock() object is stored in the attribute .account_lock, 
which is used to synchronize access to the account balance.
Both the .withdraw() and .deposit() methods use a with self.account_lock: block. 
This ensures that only one thread at a time can execute the code inside these blocks.
"""

"""
The with self.account_lock: statement acquires the lock before entering the block and releases 
it after exiting. This solves the race condition problem.
"""


class BankAccount:
    def __init__(self, balance):
        self.balance = balance
        # Ensures that only one thread can modify the balance at a time
        self.account_lock = threading.Lock()

    def withdraw(self, amount):
        with self.account_lock:
            if self.balance >= amount:
                new_balance = self.balance - amount
                print(f"Withdrawing Amount..{amount}...")
                # Time Delay
                time.sleep(0.1)
                self.balance = new_balance
            else:
                ValueError("Balance is not sufficient...")

    def deposit(self, amount):
        with self.account_lock:
            new_balance = self.balance + amount
            print(f"Depositing Amount..{amount}...")
            # Time Delay
            time.sleep(0.1)
            self.balance = new_balance


def main(num):
    account = BankAccount(1000)
    # Create a ThreadPoolExecutor and submit tasks
    with ThreadPoolExecutor(max_workers=num, thread_name_prefix="Worker") as executor:
        executor.submit(account.withdraw, 600)
        executor.submit(account.deposit, 700)
        executor.submit(account.withdraw, 800)
        executor.submit(account.withdraw, 200)
    print(f"Final Account Balance...{account.balance}")


if __name__ == "__main__":
    print(f"Calling Before main..")
    # Pass number of threads
    main(5)
    print(f"Calling After main..")
