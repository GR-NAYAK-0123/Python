
from threading import Thread


def hello():
    for i in range(5):
        print("Hello", i+1)


def hi():
    for i in range(5):
        print("Hii", i+1)


if __name__ == '__main__':

    t1 = Thread(target=hello)
    t2 = Thread(target=hi)

    t1.start()
    t2.start()