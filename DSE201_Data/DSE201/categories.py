__author__ = 'hegde.monica'

import csv
import random
import string

#number of tuples.
T_R = 40

f = csv.writer(open("categories.csv","wb"))

for i in range(1,T_R+1):
    desc_length = random.randint(5,32)
    name_length = random.randint(5,8)
    name = ''.join([random.choice(string.ascii_letters) for n in xrange(name_length)])
    desc = ''.join([random.choice(string.ascii_letters+" ") for n in xrange(desc_length)])
    f.writerow([i,name,desc])


