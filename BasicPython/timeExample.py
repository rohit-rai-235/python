import time
timestamp = time.localtime()
hour = int(timestamp.tm_hour)
min = int(timestamp.tm_min)
sec = int(timestamp.tm_sec)
morning=12
evening=18
if(morning>=hour):
    print("Good Morning.!!!! Its",hour,':',min,':',sec)
elif(morning<=hour and evening>=hour):
    print("Good Afternoon.!!!! Its",hour,':',min,':',sec)
else:
    print("Good Night!!! Its",hour,':',min,':',sec)