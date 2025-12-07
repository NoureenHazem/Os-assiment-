import threading
import time
def print 1():
print("start of thread", threading.current_thread().name)
time.sleep(2)
print("end of thread", threading.current_thread().name)
def print 2():
print("start of thread", threading.current thread().name)
print("end of thread", threading.current_thread().name)
a=threading.Thread(target print_1, nase "Thread 1")
b=threading.Thread(target-print_2, name "Toread 2")
a.start()
b.start()
