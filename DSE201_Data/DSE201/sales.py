__author__ = 'hegde.monica'
import csv
import random

#number of tuples.
T_R=20000

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
