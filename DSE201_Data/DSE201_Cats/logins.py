__author__ = 'hegde.monica'

import csv
import random
import time

#number of tuples.
T_R=40000

#distinct values for user_id = number of tuples in 'users'
f = csv.reader(open("users.csv"))
users = list(f)
V_R_users = len(users)

f = csv.writer(open("logins.csv","wb"))

##
#generates random timestamp
def strTimeProp(start, end, format, prop):
    stime = time.mktime(time.strptime(start, format))
    etime = time.mktime(time.strptime(end, format))
    ptime = stime + prop * (etime - stime)
    return time.strftime(format, time.localtime(ptime))
def randomDate(start, end, prop):
    return strTimeProp(start, end, '%Y-%m-%d %H:%M:%S', prop)
##

i=0
while i<T_R:
    random.shuffle(users)
    for u in users:
        i=i+1
        timestamp = randomDate("2014-1-31 00:00:00", "2016-1-1 23:59:00", random.random())
        f.writerow([i, u[0], timestamp])
        if(i>=T_R):
            break
