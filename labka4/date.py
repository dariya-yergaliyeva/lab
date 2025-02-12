import datetime
#1
now=datetime.datetime.today()
ago=now-datetime.timedelta(days=5)
print(ago.strftime("%Y-%m-%d"))

#2
current=datetime.datetime.now()
yesterday=current-datetime.timedelta(days=1)
nextday=current+datetime.timedelta(days=1)
print(yesterday.strftime("%Y-%m-%d"))
print(current.strftime("%Y-%m-%d"))
print(nextday.strftime("%Y-%m-%d"))

#3
now1=datetime.datetime.today()
wm=now1.replace(microsecond=0)
print(wm)
#4
date1=datetime.datetime.now()
date2=date1-datetime.timedelta(days=115)
insec=(date1-date2).total_seconds()
print(insec)
