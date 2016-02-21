import csv
import random
from collections import defaultdict

#number of tuples.
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
