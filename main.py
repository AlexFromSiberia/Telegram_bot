import selenium_
from t_bot import *
import time
from threading import Thread


def run_selenium():
    """
    Launches selenium every 10 minutes
    :return: None
    """
    while True:
        time.sleep(600)
        selenium_.run_selenium()


th_1, th_2 = Thread(target=run), Thread(target=run_selenium)

if __name__ == '__main__':
    th_1.start(), th_2.start()
    th_1.join(), th_2.join()

