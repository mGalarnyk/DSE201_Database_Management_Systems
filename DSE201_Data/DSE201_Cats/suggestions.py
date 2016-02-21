__author__ = 'hegde.monica'

import csv
import random

#distinct values for login_id = number of tuples in 'logins'
f = csv.reader(open("logins.csv"))
logins = list(f)
V_R_logins = len(logins)

#number of tuples.
T_R = V_R_logins*10

#distinct values for video_id = number of tuples in 'videos'
f = csv.reader(open("videos.csv"))
videos = list(f)
V_R_videos = len(videos)

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
