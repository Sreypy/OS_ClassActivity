import threading
from threading import Semaphore

# Initialize semaphores
a = Semaphore(1)  # Process 1 starts first
b = Semaphore(0)  # Process 2 waits
c = Semaphore(0)  # Process 3 waits

def process1():
    a.acquire()
    print("H")
    print("E")
    b.release()

def process2():
    b.acquire()
    print("L")
    print("L")
    c.release()

def process3():
    c.acquire()
    print("O")

# Create threads
t1 = threading.Thread(target=process1)
t2 = threading.Thread(target=process2)
t3 = threading.Thread(target=process3)

# Start threads
t1.start()
t2.start()
t3.start()

# Wait until all threads finish
t1.join()
t2.join()
t3.join()
