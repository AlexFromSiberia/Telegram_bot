import selenium_
from t_bot import *
from multiprocessing import Process
import os
from time import sleep


# def run_selenium():
    # # launch selenium
    # while True:
    #     time.sleep(20)
    #     selenium_.run_selenium()
    #     print('selen started')


if __name__ == '__main__':
    teleg = run()
    selen = selenium_.run_selenium()

    p1 = Process(target=teleg)
    p2 = Process(target=selen)
    p1.start()
    p2.start()

    p1.join()
    p2.join()
