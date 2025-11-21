import time


def counter(t):
    while t:
        minutes, seconds = divmod(t, 60)
        timer = "{:02d}:{:02d}".format(minutes, seconds)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1

    print("Time is over!")


t = input("Type the time in seconds: ")

counter(int(t))
