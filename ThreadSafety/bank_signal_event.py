import threading
from concurrent.futures import ThreadPoolExecutor
import time

"""
bank_open: Signals when the bank is open.
transactions_open: Signals when transactions are allowed.
"""

bank_open = threading.Event()
transactions_open = threading.Event()


def serve_customers(customer_data):
    print(f"{customer_data['name']} is waiting for the bank to open.")

    bank_open.wait()
    print(f"{customer_data['name']} entered the bank")
    if customer_data['type'] == 'WITHDRAW_MONEY':
        print(f"{customer_data['name']} is waiting for transactions to open.")
        transactions_open.wait()
        print(f"{customer_data['name']} is starting their transactions.")

        # Simulating the time taken for performing the transactions
        time.sleep(2)

        print(f"{customer_data['name']} is done transaction.")

    else:
        # Simulating the time taken for performing the transactions
        time.sleep(2)
        print(f"{customer_data['name']} is exited the Bank.")


customers = [
    {"name": "Customer1", "type": "WITHDRAW_MONEY"},
    {"name": "Customer2", "type": "WITHDRAW_MONEY"},
    {"name": "Customer3", "type": "CHECK_BALANCE"},
    {"name": "Customer4", "type": "WITHDRAW_MONEY"},
]


def main():
    with ThreadPoolExecutor(max_workers=4, thread_name_prefix="Worker") as executor:
        for customer_data in customers:
            executor.submit(serve_customers, customer_data)

        print("Bank Manager is prepared to open the Bank.")
        time.sleep(2)
        print("Bank is now open...")
        # Signal that Bank is open
        bank_open.set()

        time.sleep(2)
        print("Transactions are open now...")
        # Signal that Transactions is open
        transactions_open.set()

    print("All customers are done serving.....")


if __name__ == "__main__":
    main()
