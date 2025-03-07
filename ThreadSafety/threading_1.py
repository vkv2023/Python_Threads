import threading
import time
from concurrent.futures import ThreadPoolExecutor


def threaded_function():
    for number in range(3):
        print(f"Printing from {threading.current_thread().name} .{number=}")
        time.sleep(1)


def main(number, name):
    with ThreadPoolExecutor(max_workers=number, thread_name_prefix=name) as executor:
        for _ in range(2):
            executor.submit(threaded_function)


if __name__ == "__main__":
    main(4, "Worker")



