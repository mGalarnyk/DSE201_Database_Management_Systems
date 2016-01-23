
CREATE TABLE products 
(
        ID              SERIAL PRIMARY KEY,
	Name		TEXT,
	List_Price	DECIMAL
)

CREATE TABLE customers 
(
	ID		SERIAL PRIMARY KEY,
	Name		TEXT
)

CREATE TABLE states 
(
        ID              SERIAL PRIMARY KEY,
	Name		TEXT,
)

— Customer needs to have a category
CREATE TABLE categories 
(
        ID              SERIAL PRIMARY KEY,
	Name		TEXT NOT NULL,
	Description	TEXT NOT NULL
)


CREATE TABLE location 
(
        ID              SERIAL PRIMARY KEY,
	Costumer_ID	INTERGER REFERENCES costumers (ID),
	State_ID	INTEGER REFERENCES states (ID) 
)

CREATE TABLE sales 
(
        ID              SERIAL PRIMARY KEY,
	Quantity	INTEGER,
	Price_Paid	DECIMAL,
	Costumer_ID	INTEGER REFERENCES costumers (ID) NOT NULL,
	Product_ID	INTEGER REFERENCES products (ID) NOT NULL
)

CREATE TABLE type 
(
        ID              SERIAL PRIMARY KEY,
	Category_ID	INTEGER REFERENCES category (ID) UNIQUE,
	Product_ID	INTEGER REFERENCES products (ID) NOT NULL
)	
	
