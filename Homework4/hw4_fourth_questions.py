###############
# Use the data in covid.csv for this exercise
#
# 10) In a separate file, write a piece of code that
# loads the covid.csv file and prints the list of countries
#  and the total average of death/confirmed among those countries
# for those countries that have more than 500, 1000 and 5000
# respectively.
# Follow DRY principles in order to complete this exercise.
#
#
# #
import pandas as pd
import numpy as np

df = pd.read_csv('covid.csv')
df.head(20)


def avg_death_confir(how_many):
    countries = list()
    for i in df.index:
        if df.iloc[i]['Confirmed'] > how_many:
            countries.append(df.iloc[i]['Country'])
    
    tot_mean = np.mean(df.loc[df['Country'].isin(countries),'Deaths'] /   df.loc[df['Country'].isin(countries),'Confirmed'])    
    print(countries, tot_mean)
        
avg_death_confir(500)
        