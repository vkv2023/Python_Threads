import random
import threading
import time
from concurrent.futures import ThreadPoolExecutor
from pkgutil import resolve_name

customer_available_condition = threading.Condition()

# Customers waiting to be served by the Teller
customer_queue = []

"""
To summarize, using Condition here has allowed for:

The teller to efficiently wait for customers without busy-waiting
Customers to notify the teller of their arrival
Synchronization of access to the shared customer queue
Condition is commonly used in producer-consumer scenarios. 
In this case, the customers are producers adding to the queue, and the teller
 is a consumer taking from the queue.
"""


def Now():
    return time.strftime("%H:%M:%S")


def serve_customer():
    while True:
        with customer_available_condition:
            # Wait for customer to arrive
            while not customer_queue:
                print(f"{Now()} : Teller is waiting for a customer")
                customer_available_condition.wait()

            # serve the customer
            customer = customer_queue.pop(0)
            print(f"{Now()} : Teller is serving Customer")

        # Simulate the time taken to serve the customer
        time.sleep(random.randint(1,4))
        print(f"{Now()} : Teller has finished serving customer")


def add_customer_to_queue(name):
    with customer_available_condition:
        print(f"{Now()} : {name} has arrived at the bank.")
        customer_queue.append(name)

        customer_available_condition.notify()


customer_names = [
    "Customer1",
    "Customer2",
    "Customer3",
    "Customer4",
    "Customer5",
]


def main():
    with ThreadPoolExecutor(max_workers=5, thread_name_prefix="Worker") as executor:
        teller_thread = executor.submit(serve_customer)
        for name in customer_names:
            time.sleep(random.randint(1,3))
            executor.submit(add_customer_to_queue,name)


if __name__ == '__main__':
    main()
    print("All customer have been served..")



