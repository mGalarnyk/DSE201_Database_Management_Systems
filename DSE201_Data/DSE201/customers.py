__author__ = 'hegde.monica'
import string
import csv
import random

#number of tuples.
T_R=1000

f = csv.reader(open("states.csv"))
states = list(f)

f = csv.writer(open("customers.csv","wb"))

i=0
#uniform distruibution of distinct values
while i<T_R:
    random.shuffle(states)
    for st in states:
        i=i+1
        name_length = random.randint(5,8)
        customer_name = ''.join([random.choice(string.ascii_letters) for n in xrange(name_length)])
        print(i, customer_name, st[0])
        f.writerow([i, customer_name, st[0]])
        if(i>=T_R):
            break
