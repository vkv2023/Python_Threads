import threading
import time
from concurrent.futures import ThreadPoolExecutor


"""
Reentrant Lock : RLock
RLock is helpful in scenarios like this, where you have nested lock acquisitions within the same thread. 
RLock also keeps a count of how many times it’s been acquired, 
and it must be released the same number of times to be fully unlocked.
"""


class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance
        # Ensures that only one thread can modify the balance at a time
        self.account_lock = threading.RLock()

    def deposit(self, amount):
        print(f"Thread {threading.current_thread().name} "
              "Waiting to acquire the lock for .deposit()"
        )
        with self.account_lock:
            print(f"Thread {threading.current_thread().name} "
                  "acquired lock for .deposit()"
            )
            time.sleep(0.1)
            self._update_balance(amount)

    def _update_balance(self, amount):
        print(f"Thread {threading.current_thread().name} "
              "Waiting to acquire the lock for .update_balance()"
        )
        with self.account_lock:  # This will cause a deadlock
            print(f"Thread {threading.current_thread().name} "
                  "acquired lock for .update_balance()"
            )
            self.balance += amount


def main(num):
    account = BankAccount(1000)
    with ThreadPoolExecutor(max_workers=num, thread_name_prefix="Worker") as executor:
        for _ in range(num):
            executor.submit(account.deposit, 200)
    print(f"Final Account Balance...{account.balance} ")


if __name__ == "__main__":
    main(3)





