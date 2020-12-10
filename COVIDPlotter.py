import matplotlib.pyplot as plt
import pandas as pd
import urllib.request
import os
import time
#The urllib.request module is used to open or download a file over HTTP.
# Specifically, the urlretrieve method of this module is what we'll use for actually retrieving the file.

print('Beginning file download with requests')
url = 'https://www.ecdc.europa.eu/sites/default/files/documents/COVID-19-geographic-disbtribution-worldwide.xlsx'

#gets current working directory
urdirectory = os.getcwd()

#use HTTP to access the link, download the file and then save it in current directory
urllib.request.urlretrieve(url,'%s/Coviddata.xlsx' %urdirectory)

#read in the excel file
covid = pd.read_excel('%s/Coviddata.xlsx' %urdirectory)
covid = covid.drop(columns = ['dateRep', 'geoId', 'countryterritoryCode', 'continentExp'] )
info = input('What would you like to know about COVID-19?:')
if (info == 'total'):
    total = 0
    for i in range(0, len(covid)):
        #this code allows you to get value at index i, in column 'deaths'
        total = total + covid.at[i,'deaths' ]

    print('Global Death Count: %s' %total)
    #sleep() causes the program to wait 10 seconds before continuing
    time.sleep(5)
    ans = input("Would you like to look at the trends? (y/n): ")
    if( ans == 'y'):
        info = "trends"
    else:
        print('Goodbye!')


while(info == 'trends'):
    while (1):
        country = input('Please enter a country (United_States_of_America, Canada, etc):')
        if(country=='goodbye'):
            break
        #Getting every row and and column that has the my specific country

        covidCan = covid.loc[covid["countriesAndTerritories"] == country]
        if( not covidCan.empty):
            break
        print('ur dumb, try again')

    if (country == 'goodbye'):
        break
    covidCan = covidCan.reset_index()
    covidCan = covidCan.drop(columns = ['index'])




    xval = []

    #len(df) returns the number of rows of data
    for i in range(0, len(covidCan)):
        xval.append(i)
    data = input("What would you like to see? (deaths, cases):")
    yval = covidCan[data]
    #converting a Series object to a list and then trying to reverse it
    yval = yval.values.tolist()
    yval.reverse()
    #finding the running total number of deaths
    ytotl = []
    for i in range(0, len(yval)):
        ytotl.append(yval[i])
    #lists are passed by reference apparently

    for i in range (1, len(covidCan)):
        ytotl[i] = ytotl[i-1] + ytotl[i]

    #plotting the data of both total deaths and daily deaths

    fig, axs = plt.subplots(2, figsize = (10,5))
    plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=None, hspace=1.2)
    #fig.tight_layout(pad=10.0)
    fig.suptitle('Covid-19 Data for %s' %country)
    axs[0].plot(xval, ytotl)
    axs[0].set_xlabel('Number of days since first case')
    axs[0].set_ylabel('Total # of Deaths from COVID-19', fontsize =10)
    axs[1].bar(xval, yval, width = 0.8)
    plt.xlabel('Number of days since first case')
    plt.ylabel('Daily COVID-19 Deaths', fontsize =10)

    plt.show()
#this deletes the file that we downloaded
#os.remove('%s/Coviddata.xlsx' %urdirectory)




"Left to do... get all of our data (air quality, light pollution, etc), clean up code into functions, build a map, learn how" \
"to create a GUI"



"can look into using geopandas and Bokeh"
