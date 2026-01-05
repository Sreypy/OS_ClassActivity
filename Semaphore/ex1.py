import threading
import time
import random

# Buffer capacity (100 particles = 50 pairs)
BUFFER_SIZE = 100
buffer = []

# Semaphores
space = threading.Semaphore(BUFFER_SIZE)  # counts free slots (initially 100)
full = threading.Semaphore(0)             # counts filled slots (initially 0)
lock = threading.Semaphore(1)             # mutual exclusion

# Producer function
def producer(pid):
    while True:
        # produce a pair
        P1, P2 = f"P{pid}-A", f"P{pid}-B"

        # need 2 spaces
        space.acquire()
        space.acquire()

        # lock buffer for atomic insertion
        lock.acquire()
        buffer.append(P1)
        buffer.append(P2)
        print(f"Producer {pid} produced pair: {P1}, {P2} | Buffer size = {len(buffer)}")
        lock.release()

        # signal 2 particles available
        full.release()
        full.release()

        time.sleep(random.uniform(0.5, 1.5))  # simulate work

# Consumer function
def consumer():
    while True:
        # need 2 particles
        full.acquire()
        full.acquire()

        # lock buffer for atomic removal
        lock.acquire()
        P1 = buffer.pop(0)
        P2 = buffer.pop(0)
        print(f"Consumer packaged pair: {P1}, {P2} | Buffer size = {len(buffer)}")
        lock.release()

        # signal 2 spaces freed
        space.release()
        space.release()

        time.sleep(random.uniform(1, 2))  # simulate packaging time

# Start threads
producers = [threading.Thread(target=producer, args=(i,)) for i in range(3)]  # 3 producers
consumer_thread = threading.Thread(target=consumer)

for p in producers:
    p.start()
consumer_thread.start()
