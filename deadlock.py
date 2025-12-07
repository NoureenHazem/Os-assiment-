import threading
import time
resource_1=threading.Lock()
resource_2=threading.local()
def thread_1():
with resource_1():
print("thread 1 acquire res 1")
time.sleep(1)
print("thread 1 waiting for res 2")
with resource_2:
print("thread 1 acquire res 2 complete")
def thread_2():
with resource_2:
print("thread 2 acquire res 2")
time.sleep(1) print("thread 2 waiting for res 1")
with resource_1:
print("thread 2 acquire res i complete")
threading.Thread(target-thread 1)
b=threading. Thread(target-thread_2)
s.start()
b.start()
