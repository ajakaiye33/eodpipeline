"""
Created on Tuesday June 22 00:59:25 2021
@author:hedgar
"""
# import necessary modules and packages
import pandas as pd
from datetime import datetime
import configparser


URL = 'https://doclib.ngxgroup.com/REST/api/statistics/equities/?market=&sector=&orderby=&pageSize=300&pageNo=0'


# save the days trading stats


def json2csv(URL=URL):
    """
    Extract and update csv
    """
    eod = './docs/eodfrm210621.csv'
    df = pd.read_json(URL)
    df = df.dropna()
    df.to_csv(eod, mode='a', header=False, index=False)
    #print(df.head(2))


def main():
    json2csv()


if __name__ == "__main__":
    main()
