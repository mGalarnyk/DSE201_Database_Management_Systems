__author__ = 'hegde.monica'

import csv
import random
import time

#number of tuples.
T_R=5000

#distinct values for user_id = number of tuples in 'users'
f = csv.reader(open("users.csv"))
users = list(f)
V_R_users = len(users)

#distinct values for video_id = number of tuples in 'videos'
f = csv.reader(open("videos.csv"))
videos = list(f)
V_R_videos = len(videos)

f = csv.writer(open("watch.csv","wb"))

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
#uniform distruibution of distinct values
while i<T_R:
    random.shuffle(users)
    random.shuffle(videos)
    for j in range(0,V_R_users/2):
        for k in range(0,V_R_videos/2):
            i=i+1
            timestamp = randomDate("2014-1-31 00:00:00", "2016-1-1 23:59:00", random.random())
            f.writerow([i, videos[k][0], users[j][0], timestamp])
            if(i>=T_R):
                break
        if(i>=T_R):
            break
    if(i>=T_R):
        break
    for j in range(V_R_users/2,V_R_users):
        for k in range(V_R_videos/2,V_R_videos):
            i=i+1
            timestamp = randomDate("2014-1-31 00:00:00", "2016-1-1 23:59:00", random.random())
            f.writerow([i, videos[k][0], users[j][0], timestamp])
            if(i>=T_R):
                break
        if(i>=T_R):
            break
