import threading
import time

"""
This runs say_hello in a separate thread, 
so print("Main program continues...") happens while the thread is running.
"""

def say_hello():
    print("Hello from thread!")
    time.sleep(1)
    print("Thread finished")

# Create and start a thread
t = threading.Thread(target=say_hello)
t.start()

print("Main program continues...")
t.join()
