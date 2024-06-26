import time

def countdown(t):

    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end = "\n")
        time.sleep(1)
        t -= 1
    
    print('Lift off!')

t = input("Enter starting time in seconds: ")
countdown(int(t))