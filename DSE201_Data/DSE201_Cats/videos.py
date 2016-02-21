__author__ = 'hegde.monica'

import csv
import random
import string

#number of tuples.
T_R = 1000

f = csv.writer(open("videos.csv","wb"))

for i in range(1,T_R+1):
    name_length = random.randint(8,18)
    name = ''.join([random.choice(string.ascii_letters+"_"+string.digits) for n in xrange(name_length)])
    f.writerow([i,name])
