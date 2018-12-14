import time
import datetime



while True:
    now = datetime.datetime.now()
    weekday = datetime.datetime.isoweekday(now)


    print(time.time())
    time.sleep()