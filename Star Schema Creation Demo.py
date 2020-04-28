# -*- coding: utf-8 -*-
"""
Created on Sat Oct 20 21:46:06 2018

@author: Ashish Chouhan
Star Schema Creation
"""
# Import Libraries required for Processing
import pandas as pd
import numpy as np

# Setting file names used during execution process
# Input File :  Movie details and User Information Excel file consists of raw information about User
#               and Movies along with the ratings provided by User to a specific Movie
file_input = 'Movie details and User Information.xls'

# Output File : Pre-Processed Movie Lens Data CSV file will hold the information, after input file
#               is being pre-processed; so as to remove Null Value and InConsistent value.
file_pre_processed = 'Pre-Processed Movie Lens Data.csv'

# Output File : User_Details.xlsx file will hold only the User Information.
#               Movie_Details.xlsx file will hold only the Movie Information.
#               Movie_Ratings_for_Users.xlsx file will hold the factual information of 
#               Movie Ratings provided by User.
file_user_output = 'User_Details.xlsx'
file_movie_output = 'Movie_Details.xlsx'
file_fact_output = 'Movie_Ratings_for_Users.xlsx'

# Read Input File to fetch Raw Information of User and Ratings provided to specific movie 

# Read the Movie details and User Information Excel file using pandas.read_excel function and 
# populate the records into an input Dataframe
df_input = pd.read_excel(file_input, header = 0)
print(df_input)

# Pre-Processing of Input Dataframe

# Replace invalid value present in the columns with NaN or Null Values
df_input['Occupation'] = df_input.Occupation.replace(11413, np.nan)
df_input['Title'] = df_input.Title.replace(1682, np.NaN)
df_input['Genres'] = df_input.Genres.replace([1523648,'1 - 000 - 000 Duck (1971)'], np.NaN)
df_input['Ratings'] = df_input.Ratings.replace('Super', np.NaN)

# Processed Input Dataframe will now have only valid values present in column or Null Values

# Delete record from input dataframe (df_input) having NaN or Null Values for any of the column present in
# the dataframe
df_input.dropna(axis = 'rows', inplace = True)
  
# Save the Pre-Processed DataFrame into a CSV file 
df_input.to_csv(file_pre_processed, encoding='utf-8', index=False)

"""
Staging Area
"""

# Creation of Star Schema

# Read Pre-processed Movie Lens Data CSV File which is populated above using pandas.read_csv function 
# and populate the records into a new dataframe (df_pre_processed) 
df_pre_processed = pd.read_csv(file_pre_processed, header = 0)
print(df_pre_processed)

# Split the columns as per requirement from df_pre_processed dataframe into different dataframes.
 
# Select columns which are relevant to user information from df_pre_processed dataFrame
# and populate it into a new subset DataFrame (df_users)
df_users = df_pre_processed.loc[ : , ['User_ID', 'Gender', 'Zip_Code', 'Occupation', 'Age_Min_Value', 'Age_Max_Value'] ]
print(df_users)

# Select columns which are relevant to movie information from df_pre_processed dataFrame
# and populate it into a new subset DataFrame (df_movies)
df_movies = df_pre_processed.loc[ : , ['Movie_ID', 'Title', 'Genres'] ]
print(df_movies)

# Select columns which are relevant to factual information about Movie Rating from df_pre_processed
# dataFrame and populate it into a new subset DataFrame (df_user_movie_fact)
df_user_movie_fact = df_pre_processed.loc[ : , ['User_ID', 'Movie_ID', 'Ratings', 'TimeStamp'] ]
print(df_user_movie_fact)

# df_users dataframe represent User Dimension Table,
# df_movies dataframe represent Movie Dimension Table,
# df_user_movie_fcat represent Movie Rating Fact Table.

# Requirement states that all table must have uniqe records and they must be sorted.

# Sort the df_users dataframe in ascending order based on User ID and 
# remove duplicate User ID records
df_users = df_users.sort_values(by = ['User_ID'], ascending = True, na_position = 'last').drop_duplicates(['User_ID'],keep = 'first')
print(df_users)

# Sort the df_movies dataframe in ascending order based on Movie ID and 
# remove duplicate Movie ID records
df_movies = df_movies.sort_values(by = ['Movie_ID'], ascending = True, na_position = 'last').drop_duplicates(['Movie_ID'],keep = 'first')
print(df_movies)

# Sort the df_user_movie_fact dataframe in ascending order based on User ID and Movie ID, also 
# remove duplicate record for User ID and Movie ID Combination
df_user_movie_fact = df_user_movie_fact.sort_values(by = ['User_ID', 'Movie_ID'], ascending = True, na_position = 'last').drop_duplicates(['User_ID', 'Movie_ID'],keep = 'first')
print(df_user_movie_fact)

# Export the Star Schema and save them in Excel File respectively
df_users.to_excel(pd.ExcelWriter(file_user_output),'Users', index = False)
df_movies.to_excel(pd.ExcelWriter(file_movie_output),'Movies', index = False)
df_user_movie_fact.to_excel(pd.ExcelWriter(file_fact_output),'Ratings', index = False)