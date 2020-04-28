import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="927429268@Yp",
)

mycursor = mydb.cursor()


mycursor.execute("CREATE DATABASE etlprocess")

mycursor.execute("USE etlprocess")

mycursor.execute("""CREATE TABLE country
(manufacturing_site1 varchar(15) NOT NULL PRIMARY KEY,
country varchar(15) NULL, 
manufacturing_country varchar(15) NULL)""")

mycursor.execute("""CREATE TABLE productgroup
(product_group varchar(15) NULL ,
item_description varchar(50) NOT NULL PRIMARY KEY,
sub_classification varchar(50) NULL)""")

mycursor.execute("""CREATE TABLE description
(item_description varchar(50) NOT NULL,
molecule_test_type varchar(25) NULL ,
brand varchar(10) NULL,
dosage varchar(20) NOT NULL PRIMARY KEY,
FOREIGN KEY(item_description) REFERENCES productgroup(item_description))""")

mycursor.execute("""CREATE TABLE dosage_description
(dosage varchar(20) NOT NULL,
dosage_form varchar(30) NULL ,
FOREIGN KEY(dosage) REFERENCES description(dosage))""")

mycursor.execute("""CREATE TABLE unit
(unit_price int NOT NULL PRIMARY KEY,
pack_price int NULL,
weight int NULL)""")

mycursor.execute("""CREATE TABLE pricepack
(unit_price int NOT NULL,
unit_of_measure int NULL,
line_item_quantity int NULL,
line_item_value int NULL,
FOREIGN KEY(unit_price) REFERENCES unit(unit_price))""")

mycursor.execute("""CREATE TABLE facttablesys 
(factid int NOT NULL PRIMARY KEY, 
shipment_mode varchar (5) NULL,
freight_cost int NULL,
manufacturing_site1 varchar (15) NOT NULL,
item_description varchar (50) NOT NULL,
unit_price int NOT NULL, 
FOREIGN KEY(manufacturing_site1) REFERENCES country(manufacturing_site1),
FOREIGN KEY(item_description) REFERENCES productgroup(item_description),
FOREIGN KEY(unit_price) REFERENCES unit(unit_price))""")