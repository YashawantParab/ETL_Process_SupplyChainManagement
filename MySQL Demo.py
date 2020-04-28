# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 15:52:19 2018

@author: Ashish Chouhan
Connection to MySQL
"""
#########################################################################################
"""
Revision:
  - What is ETL?
    ETL is Extract Transform Load where we extract information from different sources then perform
    Cleaning and transformation as per Business requirement and Load the transformed Data into a Datawarehouse.
    From where it can used for Visualisation or Analaytics Purpose.
    
  - Jobs implemented till now in Talend Data Integration
    1st Job: Database Connection
    2nd Job: Spliting the existing column in different column
    3rd Job: tMap Component Usage for Merge, Join, Transformation
    4th Job: Star Schema Creation
    Job for File Format Changes
    SCD Job Example
    
  - Concepts Behind ETL pipeline  
    Extraction from different Source like CSV, Excel, JSON, Database
    Cleaning process considering the dimensions
    Transforming the Data by joining, splitting, selecting the columns and creating new tables for further analyses
    Loading the Data into Datawarehouse in different schemas such as Star Schemas, Snowflakes Schema and Fact Constellation Schema

  - New Terminologies
    Staging Area
    SMART Data
    Logical Data Map
    Extraction: Logical Data Extraction ( FUll Extraction, Incremental Extraction )
                Physical Data Extraction ( Online Extraction, Offline Extraction )
    Dimensions Table
    Facts Table
    Primary Key/ Surrogate Keys
    Natural Keys
    Slow Changing Dimensions : Type 0, 1, 2, 3, 4, 6
"""    
# If you work with Python 3:
# sudo apt-get install python3-mysqldb
# pip install mysqlclient
#
# If above steps dont work then execute the below steps:
# Download the wheel from link : https://www.lfd.uci.edu/~gohlke/pythonlibs/#mysqlclient
# Execute the command - pip install (ex/dir)/mysqlclient-1.3.13-cp37-cp37m-win_amd64.whl

# Import the Libraries
import sys
import MySQLdb

conn = None # Database Connection

try:
    # Open Database Connection.
    # Parameters are : (server_hostname, username, password, database_name, server_port=3306)
    conn = MySQLdb.connect('localhost', 'root', 'root', 'scd_demo', 3306)
    
    # If Connection is successfull then dsplay the 'Connected' Message on Console
    print('Connected')
    
    # Get a Cursor from the Connection, for traversing the records in result-set
    
    # Cursor from the connection wihtout Dictionary details i.e. Tuple of Column Heading and Column Value
    # cursor = conn.cursor()
    
    # Cursor from the connection with Dictionary Details i.e. Tuple of Column Heading and Column Value
    # Example: 'category': 'coffee'
    cursor = conn.cursor(MySQLdb.cursors.DictCursor)
    
    # Execute MySQL query to fetch the current Database Version via execute()
    cursor.execute('SELECT Version()')
    
    # Fetch one (current) row into a tuple
    version = cursor.fetchone()
    
    # Print the Database Version Fetched from above Execute Query and display on the console
    print('Database Version: %s' % version) # one-item tuple
    
    #########################################################
    
    # Create a table in the Database
    
    # Drop the table if it is already present in the database
    cursor.execute('drop table if exists cafe')
    
    # Execute query to create a table in the database
    cursor.execute('''create table if not exists cafe (
                        id int unsigned not null auto_increment,
                        category enum('tea', 'coffee') not null,
                        name varchar(50) not null,
                        price decimal(5,2) not null,
                        primary key (id))''')
    
    # Insert records into the database
    cursor.execute('''insert into cafe (category, name, price) values 
                       ('coffee', 'Cappuccino', 3.29),
                       ('coffee', 'Caffe Latte', 3.39),
                       ('tea', 'Green Tea', 2.99),
                       ('tea', 'Wulong Tea', 2.89)''')
    
    # Commit all the transaction performed till now in database
    conn.commit()
    
    # Fetch record from the table created above with the help of Select * Query
    cursor.execute('select * from cafe')
    
    # Fetch all rows from results-set i.e. Cursor into 'a tuple of tuples'
    rows = cursor.fetchall()
    
    # Process each row (tuple) to be displayed on the Console
    for row in rows:
        print(row)

# Error handling if any error occur during Database processing
except MySQLdb.Error as e:
    
    # Display the error code number and description occured during executino on console
    print('Error %d: %s' % (e.args[0], e.args[1])) # Error code number, description
    sys.exit(1) # Raise a SystemExit exception for cleanup

finally:
    
    # If connection still exist
    if conn:
        
        # Close the database connection
        conn.close()
        print('Closed..')
