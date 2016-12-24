# Threads using class
import time
import random
import threading


class CustThread(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)

        self.name = name

    def run(self):
        getTime(self.name)

        print("Thread ", self.name, "Execution Ends")


def getTime(name):
    print("\n")
    print("Thread {} sleeps at {}".format(name, time.strftime("%H:%M:%S", time.gmtime())))

    random_sleep_time = random.randint(1, 5)

    time.sleep(random_sleep_time)


thread1 = CustThread("1")
thread2 = CustThread("2")
thread3 = CustThread("3")

thread1.start()
thread2.start()
thread3.start()

print("Thread 1 is Alive: ", thread1.is_alive())
print("Thread 2 is Alive: ", thread2.is_alive())
print("Thread 3 is Alive: ", thread3.is_alive())

print("Thread 1 Name: ", thread1.getName())
print("Thread 2 Name: ", thread2.getName())
print("Thread 3 Name: ", thread3.getName())

thread1.join()
thread2.join()
thread3.join()

print("Execution ends")
