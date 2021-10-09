import threading
import time


def show_info(name, age):
    print(f'name = {name}, age = {age}')


if __name__ == '__main__':
    # sub_thread = threading.Thread(target=show_info, args=("小明", 10))
    sub_thread = threading.Thread(target=show_info, kwargs={'age': 10, 'name': '小明'})
    sub_thread.start()