__author__ = 'hegde.monica'
import string
import csv
import random
from collections import defaultdict

#number of tuples for state.
T_R = 50

states = ["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut",
                "Delaware", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas",
                "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota", "Mississippi",
                "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey", "New Mexico", "New York",
                "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island",
                "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Vermont", "Virginia", "Washington",
                "West Virginia", "Wisconsin", "Wyoming"]

f = csv.writer(open("states.csv","wb"))

for i in range(0,T_R):
    f.writerow([i+1,states[i]])

#number of tuples for customers.
T_R = 1000

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

#number of tuples for categories.
T_R = 40

f = csv.writer(open("categories.csv","wb"))

for i in range(1,T_R+1):
    desc_length = random.randint(5,32)
    name_length = random.randint(5,8)
    name = ''.join([random.choice(string.ascii_letters) for n in xrange(name_length)])
    desc = ''.join([random.choice(string.ascii_letters+" ") for n in xrange(desc_length)])
    f.writerow([i,name,desc])

#number of tuples for products.
T_R = 1000

f = csv.reader(open("categories.csv"))
category = list(f)

prefix = ["Re","Ad","Par","Tru","Thru","In","Bar","Cip","Dop","End","Em","Fro","Gro","Hap","Kli","Lom","Mon","Qwi","Rap","Sup","Sur","Tip","Tup","Un","Up","Var","Win","Zee","cad","dud","dim","er","frop","glib","hup","jub","kil","mun","nip","peb","pick","quest","rob","sap","sip","tan","tin","tum","ven","wer","werp","zapil","ic","im","in","up","ad","ack","am","on","ep","ed","ef","eg","aqu","ef","edg","op","oll","omm","ew","an","ex","pl"]
suffix =["icator","or","ar","ax","an","ex","istor","entor","antor","in","over","ower","azz","fax","kin","in","aire","are","ine","cle"]

f = csv.writer(open("products.csv","wb"))

product_dict = defaultdict(list)

i = 0
#uniform distruibution of distinct values of category
while i < T_R:
    random.shuffle(category)
    k = random.randint(0, len(prefix)-1)
    j = random.randint(0, len(suffix)-1)
    for ca in category:
        if j not in product_dict[k]:
            i += 1
            product_dict[k].append(j)
            product_name = prefix[k]+suffix[j]
            list_price = round(random.uniform(5, 120), 2)
            f.writerow([i, product_name, ca[0], list_price])
            if i >= T_R:
                break

#number of tuples for sales.
T_R = 20000

#distinct values for customer_id = number of tuples in 'customers'
f = csv.reader(open("customers.csv"))
customers = list(f)
V_R_customers = len(customers)

#distinct values for product_id = number of tuples in 'products'
f = csv.reader(open("products.csv"))
products = list(f)
V_R_products = len(products)

f = csv.writer(open("sales.csv","wb"))

i=0
#uniform distruibution of distinct values
while i<T_R:
    random.shuffle(products)
    random.shuffle(customers)
    for j in range(0,V_R_customers/2):
        for k in range(0,V_R_products/2):
            i=i+1
            quantity = random.randint(1,15)
            price = round(random.uniform(5,1000),2)
            f.writerow([i, customers[j][0],products[k][0],quantity,price])
            if(i>=T_R):
                break
        if(i>=T_R):
            break
    if(i>=T_R):
        break
    for j in range(V_R_customers/2,V_R_customers):
        for k in range(V_R_products/2,V_R_products):
            i=i+1
            quantity = random.randint(1,15)
            price = round(random.uniform(5,1000),2)
            f.writerow([i, customers[j][0],products[k][0],quantity,price])
            if(i>=T_R):
                break
        if(i>=T_R):
            break
