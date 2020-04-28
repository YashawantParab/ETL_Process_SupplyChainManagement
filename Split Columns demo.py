# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 15:09:31 2018

@author: Ashish Chouhan
Split column further
"""
# Import Libraries
import pandas as pd
import numpy as np

# Read the TalendDemoFile1.txt file using pandas.read_table function and populate the records
# into an Input Dataframe; specify the field separator present in file also define the Schema for the file
df_input = pd.read_table('TalendDemoFile1.txt', delimiter = ';',
                         header = 0,
                         dtype={'emp_no': np.int64, 'emp_name': np.str, 'emp_skills': np.str})
print(df_input)

# Delete the record having NaN or Null Values for any of the fields present in the input dataframe
df_input.dropna(inplace = True)
print(df_input)

# Requirement is to split the Employee Skill Column further into different column having only one skill in it

# Split the column Employee Skills (emp_skills) present in input dataframe (df_input) into 4 different
# employee skill column based on field separator ',' and populate it into a new dataframe
df_middle = df_input["emp_skills"].str.split(",", n = 3, expand = True)
print(df_middle)

# Create a Seperate Employee Skills column in Input Dataframe (df_input) from df_middle data frame 
df_input["Employee Skills 1"]= df_middle[0] 
df_input["Employee Skills 2"]= df_middle[1] 
df_input["Employee Skills 3"]= df_middle[2] 
df_input["Employee Skills 4"]= df_middle[3]

# Formatting of Dataframe
  
# Delete the old column Employee Skills (emp_skills) from the input dataframe (df_input)
# Since old column is splitted into 4 new employee skill column
df_input.drop(columns =["emp_skills"], inplace = True)

# Rename the column name 'emp_no' and 'emp_name' prsent in the dataframe with relevant column headings
df_input.rename(columns = {'emp_no':'Employee Number', 'emp_name':'Employee Name'}, inplace = True) 
print(df_input)

# Export the formatted dataframe satisfying the requirement into a CSV File
df_input.to_csv('out.csv', encoding='utf-8', index=False)
