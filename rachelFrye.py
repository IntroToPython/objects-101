import math
import datetime
'''
Exercise 2.3
1.   8
2.   8.5
3.   4.0
4.   11
5.   .....
'''

#Exercise 2.4 - number 1
radius = 5
vol = (4/3) * math.pi * math.pow(radius, 3)
print 'Volume: ', vol

#Exercise 2.4 - number 2
numCopies = 60
price = 24.95*0.40 + 3.00 + .75*(numCopies - 1)
print 'Wholesale cost: ', price

#Exercise 2.4 - number 3
#Assuming you run in a circle,
startTime = datetime.datetime(2014, 10,2, 6, 52, 0)
endTime = startTime + 2 * datetime.timedelta(minutes=8, seconds = 15) + 3 * datetime.timedelta(minutes = 7, seconds = 12)
print 'Start Time: ', startTime
print 'End Time: ', endTime
