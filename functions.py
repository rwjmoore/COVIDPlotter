import matplotlib.pyplot as plt
import pandas as pd
import urllib.request
import os
import time


def get_data(url, file_name,urdirectory):
    #use HTTP to access the link, download the file and then save it in current directory
    # Get Coviddata.xlsx into an arguement in fucntion definition
    urllib.request.urlretrieve(url,file_name %urdirectory)

    #read in the excel file
    data = pd.read_excel(file_name %urdirectory)

    return data


def plot(xtitle,ytitle, title, xval, yval, ytotl, country):

    fig, axs = plt.subplots(2, figsize = (10,5))
    plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=None, hspace=1.2)
    #fig.tight_layout(pad=10.0)
    fig.suptitle(title %country)
    axs[0].plot(xval, ytotl)
    axs[0].set_xlabel(xtitle)
    axs[0].set_ylabel(ytitle, fontsize =10)
    axs[1].bar(xval, yval, width = 0.8)
    plt.xlabel('Number of days since first case')
    plt.ylabel('Daily COVID-19 Deaths', fontsize =10)

    plt.show()
