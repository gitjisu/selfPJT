import time
import datetime
import schedule

def printtest():
    now_time = '({})'.format(datetime.datetime.now().strftime('%y/%m/%d %H:%M:%S'))
    print(now_time+"Test!")

if __name__ == '__main__':

    schedule.every(60).seconds.do(printtest)

    while True:
        schedule.run_pending()
        time.sleep

