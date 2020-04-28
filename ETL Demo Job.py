# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 12:22:29 2018

@author: Ashish Chouhan
ETL with Pandas
"""
# Import Libraries required for Processing
import pandas as pd

# Setting file names used during execution process
# Input File :  Master file consists of Basic Information of Person and ID associated with it
#               Country_Code file consist of Country information associated with the ID
file_masters = 'masters.csv'
file_incoming = 'country_code.csv'

# Output File : Mastes_Dups file will hold the duplicate record present in the Master File if any
#               Output file will hold the complete informaiton of Person and Country for that ID. 
file_masters_dups = 'masters_dups.csv'
file_out = 'output.csv'

# Read Master File to fetch Person Information 

# Read the Masters.csv file using pandas.read_csv function and populate the records into a Master Dataframe
df_masters = pd.read_csv('masters.csv')
print(df_masters)

# Sort records by IDs which are present in the Dataframe in Ascending Order
df_masters.sort_values('ID', ascending = True, inplace = True)
print(df_masters)

# Master Dataframe is having records which are arranged in the ascending order of ID

# Extract Duplicate record from Master Dataframe into a new dataframe 
df_dups = df_masters[df_masters.duplicated(keep = 'first')]
print(df_dups)

# Export the output of duplicates to spreadsheet before deleting the duplicate record
df_dups.to_csv(file_masters_dups)
# Remove Duplicate record based on ID from the Master Data Frame keeping only the first Record
df_masters.drop_duplicates(subset='ID', keep='first', inplace=True)
print(df_masters)

# Master Dataframe is having only Unique records and also is arranged in Ascending Order of ID

# Read Country_Code File to fetch Country Information
# Read the Country_Code.csv file using pandas.read_csv function and populate the records into a secondary Dataframe
df_incoming = pd.read_csv(file_incoming)
print(df_incoming)

# Process to Merge(Join) Two Tables present in two different dataframe

# Join dataframe and populate into a new dataframe with Right Outer Join such that Master Dataframe (df_masters) is on left, Secondary Dataframe (df_incoming) is on right
df_join_right = pd.merge(df_masters, df_incoming, how='right', on=['ID'])
print(df_join_right)

# Join dataframe and populate into a new dataframe with Left Outer Join such that Master Dataframe (df_masters) is on left, Secondary Dataframe (df_incoming) is on right
df_join_left = pd.merge(df_masters, df_incoming, how = 'left', on=['ID'])
print(df_join_left)

# Drop the column 'Name' from the dataframe  
df_join_left.drop(['Name'], axis = 1, inplace = True)
print(df_join_left)

# Export the result of Left Outer Join into a CSV file
df_join_left.to_csv(file_out)