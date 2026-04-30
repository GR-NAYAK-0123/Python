
from datetime import datetime

def time_required(insert):
    def wrap():
        start_time = datetime.now()
        insert()
        end_time = datetime.now()

        return end_time - start_time
    return wrap


@time_required
def insert():
    values = []
    for i in range(1000):
        values.append(i)
    

# insert = time_required(insert)

# print(insert())
    
total_time = insert()
print("Required time is :", total_time)