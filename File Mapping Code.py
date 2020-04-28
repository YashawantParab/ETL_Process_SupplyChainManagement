# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 12:22:29 2018

@author: Ashish Chouhan
ETL with Pandas
"""
# Import Libraries
import pandas as pd

# Setting file names used during execution process
# Input File :  Person File consists of Basic Personal Information of Person
#               Address file consist of Address information associated with the Specific Address ID
file_person = 'Person File.txt'
file_address = 'Address File.txt'

# Output File : Duplicate file will hold the duplicate record present in the Person File if any
#               PersonAddressMapped file will hold the complete informaiton about
#               Person and Address information for that person. 
file_masters_dups = 'Duplicate.csv'
file_out = 'PersonAddressMapped.xlsx'

# Read Person File to fetch Person Information 

# Read the Person.txt file using pandas.read_table function and populate the records
# into a Person Dataframe
df_person = pd.read_table(file_person, delimiter = ';', header = 0) 
print(df_person)
                      
# Sort records present in Person Dataframe by Person IDs in Ascending Order
df_person.sort_values('Id', ascending = True, inplace = True)
print(df_person)

# Person Dataframe is having records which are arranged in the ascending order of Person ID

# Extract Duplicate record from the Person dataframe into a new dataframe 
df_dups = df_person[df_person.duplicated(keep = 'first')]
print(df_dups)

# Export the output of duplicates to spreadsheet before deleting the duplicate record
df_dups.to_csv(file_masters_dups)

# Remove Duplicate record based on Person ID from the Person  DataFrame keeping only the first Record
df_person.drop_duplicates(subset='Id', keep='first', inplace=True)
print(df_person)

# Delete the record having NaN or Null Values for Address ID field in the Person Dataframe
df_person.dropna(subset = ['AddressId'],inplace = True)
print(df_person)

# Person Dataframe will have Unique Person ID records arranged in Ascending order
# with no record having null or Nan Address ID

# Read Address File to fetch Address Information associated with specific Address ID
# Read the Address File.txt file using pandas.read_table function and populate 
# the records into a Address Dataframe
df_address = pd.read_table(file_address, delimiter = ';',header = 0)
print(df_address)

# Delete the record having NaN or Null Values for Address ID field in the Address Dataframe
df_address.dropna(subset = ['Id'],inplace = True)
print(df_address)

# Process to Merge(Join) Two Tables present in two different dataframe

# Join dataframe and populate into a new dataframe with Left Join such that 
# Person Dataframe (df_person) is on left, Address Dataframe (df_address) is on right
df_join_left = pd.merge(df_person, df_address, how = 'left', left_on='AddressId', right_on = 'Id')
print(df_join_left)

# Formatting the final Dataframe

# Drop the column 'Id_y' from the dataframe as Address ID and Id_y represent 
# same set of values i.e. Address ID 
df_join_left.drop(columns =["Id_y"], inplace = True)
print(df_join_left)

# Rename the column 'Id_x' from the dataframe with a relevant name i.e. Person Id
df_join_left.rename(columns = {'Id_x':'Person Id'}, inplace = True) 
print(df_join_left)

# Requirement is to have First Name and Last Name in Upper Case as a Output.
# Convert the First Name and Last Name present in Dataframe into an Upper Case 
df_join_left['FirstName'] = df_join_left['FirstName'].str.upper()
df_join_left['LastName'] = df_join_left['LastName'].str.upper()
print(df_join_left)

# Another requirement is to having only those record which are having 'Heidelberg' as Town and 
# Whose First Name Length is greater than 5

# From the final dataframe extract record having Town as Heidelberg into a new dataframe
df_filtered_town = df_join_left.loc[df_join_left['Town'] == 'Heidelberg']
print(df_filtered_town)

# Filter record from Dataframe which are having firstname length greater than 5
df_filtered_town_firstname = df_filtered_town.loc[df_join_left['FirstName'].str.len() > 5]
print(df_filtered_town_firstname)

# Export the formatted dataframe which satisfies all requirement into an Excel File
writer = pd.ExcelWriter(file_out)
df_filtered_town_firstname.to_excel(writer, 'output')
writer.save()