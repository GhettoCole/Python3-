# Threads - running multiple programs
import time
import random
import threading


def executeThread(i):
    print("Thread {} sleeps at {}".format(i, time.strftime("%H:%M:%S", time.gmtime())))

    random_sleep_time = random.randint(1, 10)
    time.sleep(random_sleep_time)

    print("Thread {} stops at {}".format(i, time.strftime("%H:%M:%S", time.gmtime())))


for i in range(10):
    thread = threading.Thread(target=executeThread, args=(i,))
    thread.start()

    print("Active Threads: ", threading.activeCount())
    print("Thread Objects: ", threading.enumerate())
