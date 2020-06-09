import functions
import os
import time
#The urllib.request module is used to open or download a file over HTTP.
# Specifically, the urlretrieve method of this module is what we'll use for actually retrieving the file.

print('Beginning file download with requests')
url = 'https://www.ecdc.europa.eu/sites/default/files/documents/COVID-19-geographic-disbtribution-worldwide.xlsx'
direct = os.getcwd()
covid_file='%s/Coviddata.xlsx'
covid = functions.get_data(url,covid_file,direct)

info = input('What would you like to know about COVID-19?:')
if (info == 'total'):
    total = 0
    for i in range(0, len(covid)):
        #this code allows you to get value at index i, in column 'deaths'
        total = total + covid.at[i,'deaths' ]

    print('Global Death Count: %s' %total)
    #sleep() causes the program to wait 2 seconds before continuing
    time.sleep(2)
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

    yval = covidCan.iloc[:, 5]
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
    title = 'Covid-19 Data for %s'
    xlbl='Number of days since first case'
    ylbl= 'Total # of Deaths from COVID-19'
    functions.plot(xlbl,ylbl,title,xval,yval,ytotl,country)
#this deletes the file that we downloaded
os.remove('%s/Coviddata.xlsx' %direct)




"Left to do... get all of our data (air quality, light pollution, etc), clean up code into functions, build a map, learn how" \
"to create a GUI"



