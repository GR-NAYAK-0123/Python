
# Return the total time required to execute by using a decorator

from datetime import datetime

def timer(func):
    def wrapper(*args, **kwargs):
        start = datetime.now()
        func(*args, **kwargs)
        end = datetime.now()
        return end - start
    return wrapper

@timer
def run_a_loop():
    for i in range(0, 100):
        pass

print(run_a_loop())