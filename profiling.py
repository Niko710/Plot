import cProfile
import time


def write():
    for i in range(10 ** 3):
        pass


def read():
    for i in range(10 ** 2):
        pass
    write()


def copy():
    write()
    read()


def main():
    write()
    read()
    copy()


if __name__ == '__main__':
    cProfile.run('main()', sort='cumtime')
    