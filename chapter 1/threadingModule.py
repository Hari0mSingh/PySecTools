# Concurrency and Parallelism
# Libraries: threading, concurrent.futures

# Concepts: Running multiple scans concurrently, managing threads, ensuring thread safety.


import threading

# Define a function that prints numbers with a given label
def print_numbers(label):
    for i in range(10):
        with print_lock:
            print(f"{label} {i}")

# Create a lock object for thread-safe printing
print_lock = threading.Lock()

# Create and start threads
thread1 = threading.Thread(target=print_numbers, args=('Hariom',))
thread2 = threading.Thread(target=print_numbers, args=('Singh',))

# Start the threads
thread1.start()
thread2.start()

# Wait for both threads to complete
thread1.join()
thread2.join()
