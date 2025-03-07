import random
import threading
import time
from concurrent.futures import ThreadPoolExecutor

# Semaphore with a maximum of 2 resources (tellers)
teller_semaphore = threading.Semaphore(2)


def Now():
    return time.strftime("%H:%M:%S")


def serve_customer(name):
    print(f"{Now()}: {name} is waiting for a teller..")
    with teller_semaphore:
        print(f"{Now()}: {name} is being served by a teller..")
        # Simulating the time taken for the teller to server the customer
        time.sleep(random.randint(1, 3))
        print(f"{Now()}: {name} is done being served..")


customers = [
    "Customer 1",
    "Customer 2",
    "Customer 3",
    "Customer 4",
    "Customer 5",
    "Customer 6",
]


def main():
    with ThreadPoolExecutor(max_workers=6, thread_name_prefix="Worker") as executor:
        for customer_name in customers:
            thread = executor.submit(serve_customer, customer_name)
    print(f"{Now()}: All customers have been served.")


if __name__ == "__main__":
    main()
