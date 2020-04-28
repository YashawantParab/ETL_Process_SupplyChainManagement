#!/usr/bin/env python
# coding: utf-8

# In[32]:


import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="root",
)

mycursor = mydb.cursor()


# In[33]:


mycursor.execute("CREATE DATABASE game_sales")


# In[34]:


mycursor.execute("USE game_sales")


# In[24]:





# In[ ]:


'Name', 'Year' , 'Publisher', 'Global_Sales'
'Global_Sales', 'NA_Sales' , 'EU_Sales', 'JP_Sales', 'Other_Sales'
'Name', 'Rank' , 'Platform', 'Genre'


# In[35]:


mycursor.execute("""CREATE TABLE globalSales
(globalSalesId int NOT NULL PRIMARY KEY,
Global_Sales float NULL, 
NA_Sales float NULL,
EU_Sales float NULL,
JP_Sales float NULL,
Other_Sales float NULL)""")


# In[36]:


mycursor.execute("""CREATE TABLE gameDetails
(Game_Rank int NULL ,
gameDetailsId int NOT NULL PRIMARY KEY,
Name varchar (50) NULL, 
Platform varchar (50) NULL,
Genre varchar (50) NULL)""")


# In[39]:


mycursor.execute("""CREATE TABLE facttable
(factid int NOT NULL PRIMARY KEY,
Year int NULL,
Publisher varchar (50) NULL,
gameDetailsId int NOT NULL,
globalSalesId int NOT NULL,
FOREIGN KEY(gameDetailsId) REFERENCES gameDetails(gameDetailsId),
FOREIGN KEY(globalSalesId) REFERENCES globalSales(globalSalesId))""")


# In[ ]:




