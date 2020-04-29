# -*- coding: utf-8 -*-
"""
Pandas Exercise Getting and Know Your Data
"""




#Step 1
#Import the Required Libraries


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Step2
#Import Data Set and assign to variable chipo
url='https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv'
chipo=pd.read_csv(url,sep='\t');#.tsv is tab seperated file 

#Step3 
#Read firrt 10 records from  database
print(chipo.head(10))

#Step4 
#Number of observatiopns in dataset
print(chipo.shape[0])

print(chipo.info())

#Step5
# no of column in dataset
print(chipo.shape[1])

#Step6
#Print name  of all the columns
print(chipo.columns)

#Step7
#How is the dataset inddexed
print(chipo.index)#(start=0;stop=4622,step=1)

#Step8
#Which was the most ordered item
print(chipo.info())


#Step9
#which was the most ordered item ?


c= chipo.groupby('item_name')
c=c.sum()
c=c.sort_values(['quantity'],ascending=False)
print(c.head())

#Step 9
#What was the most ordered item iin the choice_descrition column
choice=chipo.groupby('choice_description').sum()
choice=choice.sort_values(['quantity'],ascending=False)
print(choice.head(1))

#Step 10
#How many items were ordered total
total_order=chipo['quantity'].sum()
print(total_order)


#Step11
#Turn item price  into float
print(chipo['item_price'].dtype)
print(chipo.loc[0,'item_price'][1:-1])
dollarizer=lambda x:float(x[1:])
chipo.item_price=chipo.item_price.apply(dollarizer)
print(chipo['item_price'].dtype)

#Step12
#How much was the revenue for the period in the datset ?
revenue=(chipo['quantity']* chipo['item_price']).sum()
print('Revenue was: $'+str(np.round(revenue,2)))




#Step13
#How many order were made in period
orders=chipo.order_id.value_counts().sum()


#step14
# What is the average revenue ammount per order
#Solution1
chipo['revenue']=chipo['quantity']*chipo['item_price']
order_grouped=chipo.groupby('order_id').sum()
print(order_grouped.mean()['revenue'])
#Solution2
print(chipo.groupby(['order_id']).sum().mean()['revenue'])

#Step15
#How many different items sold?
print(chipo.item_name.value_counts().count())

