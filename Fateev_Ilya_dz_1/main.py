from datetime import datetime, timedelta

def GetTime():
    while True:
        try:
            sec = timedelta(seconds=int(input('Enter the number of seconds: ')))
            break
        except ValueError:
            print("It`s not a number. Try again: ")
    d = datetime(1,1,1,1,1) + sec

    print("YEARS:MOUNTH:DAYS:HOURS:MIN:SEC")
    print("%d:%d:%d:%d:%d:%d" % (d.year-1, d.month-1,d.day-1, d.hour, d.minute, d.second))


GetTime()