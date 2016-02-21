__author__ = 'hegde.monica'

import csv
import random
from collections import defaultdict

#number of tuples.
T_R=40000

#distinct values for user_id = number of tuples in 'users'
f = csv.reader(open("users.csv"))
users = list(f)
V_R_users = len(users)

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
