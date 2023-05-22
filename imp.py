import time
import pygame

running = True
while running:
    start_time=time.time()
    print("start_time:{}".format(start_time))
    while running:
        now_time=time.time()
        print("Now_time:{}".format(now_time))
        seconds_elapsed = int(now_time - start_time)
        print("Second_elapsed:{}".format(seconds_elapsed))
        if seconds_elapsed == 3:
            start_time = time.time()
            print(start_time)
    