# PANDAS-Exercise 1: ---------------------------------------------------------------------------------------------------
# From the given dataset print the first and last five rows
#Expected Output:


#Python Pandas printing first 5 rows
#Python Pandas printing first 5 rows
#Python Pandas printing last 5 rows
#Python Pandas printing last 5 rows

#ANSWER CODE:-
##PRINT FIRST FIVE ROWS:-
import pandas as pd
df = pd.read_csv("D:\\Python\\Articles\\pandas\\automobile-dataset\\Automobile_data.csv")
df.head(5)
##PRINT  LAST FIVE ROWS:-
import pandas as pd
df = pd.read_csv("D:\\Python\\Articles\\pandas\\automobile-dataset\\Automobile_data.csv")
df.tail(5)
# PANDAS-Exercise 2:----------------------------------------------------------------------------------------------------
# Clean the dataset and update the CSV file
#Replace all column values which contain ?, n.a, or NaN.
#CODE:-
df = pd.read_csv("D:\\Python\\Articles\\pandas\\automobile-dataset\\Automobile_data.csv", na_values={
'price':["?","n.a"],
'stroke':["?","n.a"],
'horsepower':["?","n.a"],
'peak-rpm':["?","n.a"],
'average-mileage':["?","n.a"]})
print (df)

df.to_csv("D:\\Python\\Articles\\pandas\\automobile-dataset\\Automobile_data.csv")
#PANDAS-EXERCISE-3:-----------------------------------------------------------------------------------------------------
#Find the most expensive car company name
#Print most expensive car’s company name and price.

#Expected Output:

#Python Pandas printing most costly car name
#Python Pandas printing most costly car name
#CODE:-
import pandas as pd
df = pd.read_csv("D:\\Python\\Articles\\pandas\\automobile-dataset\\Automobile_data.csv")
df = df [['company','price']][df.price==df['price'].max()]
df
#PANDAS-EXERCISE-4:-----------------------------------------------------------------------------------------------------
#Print All Toyota Cars details
#Expected Output:


#Python Pandas printing all Toyota cars data
#Python Pandas printing all Toyota cars data
#CODE:-
import pandas as pd
df = pd.read_csv("D:\\Python\\Articles\\pandas\\automobile-dataset\\Automobile_data.csv")
car_Manufacturers = df.groupby('company')
toyotaDf = car_Manufacturers.get_group('toyota')
toyotaDf
#PANDAS-EXERCISE-5:-----------------------------------------------------------------------------------------------------
#Count total cars per company
#Expected Outcome:

#Python Pandas count total cars per company
#Python Pandas count total cars per company
#CODE:-
import pandas as pd
df = pd.read_csv("D:\\Python\\Articles\\pandas\\automobile-dataset\\Automobile_data.csv")
df['company'].value_counts()
#PANDAS-EXERCISE-6:-----------------------------------------------------------------------------------------------------
#Find each company’s Higesht price car
#CODE:-
import pandas as pd
df = pd.read_csv("D:\\Python\\Articles\\pandas\\automobile-dataset\\Automobile_data.csv")
car_Manufacturers = df.groupby('company')
priceDf = car_Manufacturers['company','price'].max()
priceDf
#pandas-exercise-7:-----------------------------------------------------------------------------------------------------
#Find the average mileage of each car making company

#Expected Output:

#Python Pandas printing average mileage of each car making company
#Python Pandas printing average mileage of each car making company
#code:-
import pandas as pd
df = pd.read_csv("D:\\Python\\Articles\\pandas\\automobile-dataset\\Automobile_data.csv")
car_Manufacturers = df.groupby('company')
mileageDf = car_Manufacturers['company','average-mileage'].mean()
mileageDf
#PANDAS-EXERCISE-8:-----------------------------------------------------------------------------------------------------
#Sort all cars by Price column
#xpected Output:


#Python Pandas sort all cars by price column
#Python Pandas sort all cars by price column
#CODE:-
import pandas as pd
carsDf = pd.read_csv("D:\\Python\\Articles\\pandas\\automobile-dataset\\Automobile_data.csv")
carsDf = carsDf.sort_values(by=['price', 'horsepower'], ascending=False)
carsDf.head(5)
#PANDAS-EXERCISE-9:-----------------------------------------------------------------------------------------------------
#Concatenate two data frames using the following conditions
#Create two data frames using the following two dictionaries.

GermanCars = {'Company': ['Ford', 'Mercedes', 'BMV', 'Audi'], 'Price': [23845, 171995, 135925 , 71400]}
japaneseCars = {'Company': ['Toyota', 'Honda', 'Nissan', 'Mitsubishi '], 'Price': [29995, 23600, 61500 , 58900]}
#Expected Output:

#Python Pandas concatenate two data frames and create key for each data frame
#Python Pandas concatenate two data frames and create a key for each data frame
#CODE:-
import pandas as pd

GermanCars = {'Company': ['Ford', 'Mercedes', 'BMV', 'Audi'], 'Price': [23845, 171995, 135925 , 71400]}
carsDf1 = pd.DataFrame.from_dict(GermanCars)

japaneseCars = {'Company': ['Toyota', 'Honda', 'Nissan', 'Mitsubishi '], 'Price': [29995, 23600, 61500 , 58900]}
carsDf2 = pd.DataFrame.from_dict(japaneseCars)

carsDf = pd.concat([carsDf1, carsDf2], keys=["Germany", "Japan"])
carsDf
#PANDAS-EXERCISES-10:---------------------------------------------------------------------------------------------------
#Merge two data frames using the following condition
#Create two data frames using the following two Dicts, Merge two data frames, and append the second data frame as a new column to the first data frame.

Car_Price = {'Company': ['Toyota', 'Honda', 'BMV', 'Audi'], 'Price': [23845, 17995, 135925 , 71400]}
car_Horsepower = {'Company': ['Toyota', 'Honda', 'BMV', 'Audi'], 'horsepower': [141, 80, 182 , 160]}
#Expected Output:

#Python Pandas merge two data frames and append new data frame as new column
#Python Pandas merge two data frames and append new data frame as a new column
#CODE:-
import pandas as pd

Car_Price = {'Company': ['Toyota', 'Honda', 'BMV', 'Audi'], 'Price': [23845, 17995, 135925 , 71400]}
carPriceDf = pd.DataFrame.from_dict(Car_Price)

car_Horsepower = {'Company': ['Toyota', 'Honda', 'BMV', 'Audi'], 'horsepower': [141, 80, 182 , 160]}
carsHorsepowerDf = pd.DataFrame.from_dict(car_Horsepower)

carsDf = pd.merge(carPriceDf, carsHorsepowerDf, on="Company")
carsDf







