import time

i = 30
while i >= 1:
    print(i)
    i = i - 1
    time.sleep(0.2)
    if i == 0:
        print("Launch!")