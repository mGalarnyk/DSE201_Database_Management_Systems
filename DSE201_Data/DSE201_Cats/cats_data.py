__author__ = 'hegde.monica'

import time
import csv
import random
import string
from collections import defaultdict

#number of tuples for user.
T_R = 1000

f = csv.writer(open("users.csv","wb"))

for i in range(1,T_R+1):
    name_length = random.randint(8,18)
    name = ''.join([random.choice(string.ascii_letters+"_"+string.digits) for n in xrange(name_length)])
    fb_length = random.randint(8,18)
    fb = ''.join([random.choice(string.ascii_letters+"_"+string.digits) for n in xrange(name_length)])
    f.writerow([i,name,fb])

#number of tuples for videos.
T_R = 1000

f = csv.writer(open("videos.csv","wb"))

for i in range(1,T_R+1):
    name_length = random.randint(8,18)
    name = ''.join([random.choice(string.ascii_letters+"_"+string.digits) for n in xrange(name_length)])
    f.writerow([i,name])

#number of tuples for logins.
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

#number of tuples for watch.
T_R=50000

#distinct values for video_id = number of tuples in 'videos'
f = csv.reader(open("videos.csv"))
videos = list(f)
V_R_videos = len(videos)

f = csv.writer(open("watch.csv","wb"))

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

#number of tuples for likes.
T_R=50000

f = csv.writer(open("likes.csv","wb"))

i=0
#uniform distruibution of distinct values
while i<T_R:
    random.shuffle(users)
    random.shuffle(videos)
    for j in range(0,V_R_users/2):
        for k in range(0,V_R_videos/2):
            i=i+1
            timestamp = randomDate("2014-1-31 00:00:00", "2016-1-1 23:59:00", random.random())
            f.writerow([i, users[j][0], videos[k][0], timestamp])
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
            f.writerow([i, users[j][0], videos[k][0], timestamp])
            if(i>=T_R):
                break
        if(i>=T_R):
            break

#number of tuples for friends.
T_R=40000

f = csv.writer(open("friends.csv","wb"))
i = 0
#dictionary to make sure we do not have repetitions
user_dict = defaultdict(list)

while i < T_R:
    random.shuffle(users)
    for u in users:
        friend_index = random.randint(0,V_R_users-1)
        #if (u1,u2) is present, do not add (u2,u1).
        if users[friend_index][0] not in user_dict[u[0]] and u[0] not in user_dict[users[friend_index][0]]:
            #user cannot be a friend of himself
            if u[0] != users[friend_index][0]:
                i += 1
                user_dict[u[0]].append(users[friend_index][0])
                f.writerow([u[0],users[friend_index][0]])
                if i >= T_R:
                    break

#distinct values for login_id = number of tuples in 'logins'
f = csv.reader(open("logins.csv"))
logins = list(f)
V_R_logins = len(logins)

#number of tuples for suggestions.
T_R = V_R_logins*10

f = csv.writer(open("suggestions.csv","wb"))

i=0
while i<T_R:
    random.shuffle(logins)
    for j in range(0,V_R_logins):
        random.shuffle(videos)
        for k in range(0,10):
            i=i+1
            f.writerow([i, logins[j][0], videos[k][0]])
            if(i>=T_R):
                break
    if(i>=T_R):
        break
