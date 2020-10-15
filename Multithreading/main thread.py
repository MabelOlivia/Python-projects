import threading

print("Current thread that is running is: ", threading.current_thread().getName())

if threading.current_thread() == threading.main_thread():
    print("Main Thread")
else:
    print("Other Thread")
    
