from concurrent.futures import ThreadPoolExecutor

def slow_function():
    import time
    time.sleep(2)
    return "I'm done!"

with ThreadPoolExecutor() as executor:
    future = executor.submit(slow_function)
    print("Task submitted!")

    result = future.result()  # Waits until result is ready
    print(result)
