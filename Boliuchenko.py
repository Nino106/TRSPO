from datetime import datetime
import threading
import time

if __name__ == '__main__':

    def do(i, t):
        print(f'Thread {i} start')
        time.sleep(t)
        print(f'Tread {i} end')


    def run_threads(t):
        threads = [
            threading.Thread(target=do, args=(i, t[i - 1]))
            for i in range(1, 4)
        ]
        for thread in threads:
            thread.start()

    time_delay = [3, 2, 5]

    t1 = datetime.now()

    run_threads(time_delay)
    while threading.active_count() > 1:
        pass
    t2 = datetime.now()

    print(t2 - t1)
