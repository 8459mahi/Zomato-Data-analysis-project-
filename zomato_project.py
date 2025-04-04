# -*- coding: utf-8 -*-
"""Zomato_project.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1OAoMFy8rkyNG0VzmtYul4Z8uNpLRA6D_

**Importing** **Libraries**
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

"""**Read DataSet**"""

dataframe=pd.read_csv("/content/Zomato data .csv")

print(dataframe)

dataframe.head()

"""**convert the data type of column rate**"""

def handlerate(value):
  value=str(value).split("/")
  value=value[0];
  return float(value)

dataframe['rate']=dataframe['rate'].apply(handlerate)
print(dataframe.head())

dataframe.info()

"""1)What type of restaurant do the majority of customers order from?

### Type of restaurant
"""

dataframe.head()

sns.countplot(x=dataframe['listed_in(type)'])
plt.xlabel("type of resturant")

"""### Conclusion: Majority of the resturant falls in dinning category."""

dataframe.head()

"""2) How many votes has each type of restaurant recived from customers?"""

grouped_data=dataframe.groupby('listed_in(type)')['votes'].sum()
result=pd.DataFrame({'Votes':grouped_data})
plt.plot(result, c="green",marker="o")
plt.xlabel("Type of restaurant",c="red",size=20)
plt.ylabel("Votes",c="red",size=20)

"""### conclusion: Dinning resturants has recieved maxium votes."""

dataframe.head()

"""3) What are the ratings that the majority of restaurants have recieved?"""

plt.hist(dataframe['rate'],bins =5)
plt.title("Ratings distribution")
plt.show()

"""### conclusion: The majority resturants received ratings from 3.5 to 4

4) Zomato has observed that most couples order most of their food online.what is their average spending on each order?
"""

couple_data=dataframe['approx_cost(for two people)']
sns.countplot(x=couple_data)

"""### conclusion: The majority of couples prefers restuarants with an approximate cost of 300 rupees.

5) Which mode (online or offline) has received the maximum rating?
"""

plt.figure(figsize=(6,6))
sns.boxplot(x='online_order', y='rate',data=dataframe)

"""### conclusion: offline order recieved lower rating in comparision to online order.

6) Which type of restaurant recieved more offline orders,so that Zomato can prefere
customers with some good offers?
"""

pivot_table=dataframe.pivot_table(index='listed_in(type)', columns='online_order', aggfunc='size', fill_value=0)
sns.heatmap(pivot_table,annot=True, cmap="YlGnBu", fmt='d')
plt.title("Heatmap")
plt.xlabel("Online Order")
plt.ylabel("Listed In (Type)")
plt.show()

"""### Conclusion: Dining restaurants primarily accept offline orders,Where as cafes primarily receive online orders. This suggests that clientd prefer orders in person at restaurants,but prefer online ordering at cafes."""

