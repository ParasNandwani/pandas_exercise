#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 14:31:59 2020

@author: parasn
"""

#Step1
# Importing libraries
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt


#step2
#Understand dataset
url='https://raw.githubusercontent.com/justmarkham/DAT8/master/data/u.user'
user=pd.read_csv(url,sep='|')

#Step3
#assign value to user variabale and set user_index as index
print(user.info)
user.index=user['user_id']
print(user.head())

#step4
#See the firts 25 entries
print(user.head(25))

#step5
#see the lastv 10 enteries
print(user.tail(10))

#Step6 
#What is the numbers of observations ?
print("No of Records",user.shape[0])

#Step7
#What is the number of columns in the datset
#Solution1
print("Number Of Columns",len(user.columns))
#Solution 2
print("Number of Columns",user.shape[1])


#Step8
#Print the name of columns
print("name of columns \n",user.columns)

#Step 9
#How is the datset indexed ?
print(user.index)


#Step10
#What is the data type  of column?
print("Columns info \n",user.dtypes)


#Step11
#Print only occupation column
print(user['occupation'])


#Ste12
#How many dfferent occupation ?
print(user['occupation'].unique)



#Step13
#What is the most frequent occcupation?
print(user.occupation.value_counts().head(1).index)

#Step14
#Summerize the dataframe
print(user.describe())


#Step15
#Summerize all the columns
print(user.describe(include='all'))


#Step16
#Summerize only occupation column
print(user.occupation.describe())


#Step17
#What is the mean age ?
print(user.age.mean())


#Step18 
#What is the age with least occurence
print(user.age.value_counts().tail())