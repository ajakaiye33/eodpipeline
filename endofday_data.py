"""
Created on Tuesday June 22 00:59:25 2021
@author: hedgar
"""
# import necessary modules and packages
import boto3
import pandas as pd
from datetime import datetime
import configparser
import pandas as pd


# save the days trading stats
URL = URL


def json2csv(URL=URL):
    """
    Exctract and update csv
    """
    URL = str(URL)
    eod = './docs/eodfrm210621.csv'
    df = pd.read_json(URL)
    df = df.dropna()
    df.to_csv(eod, mode='a', header=False, index=False)

    # load the aws_boto credentials
    # parser = configparser.ConfigParser()
    # parser.read("eod.conf")
    # AWS_SECRET_ACCESS_KEY = parser.get("aws_cred", "AWS_SECRET_ACCESS_KEY")
    # AWS_ACCESS_KEY_ID = parser.get("aws_cred", "AWS_ACC_KEY_ID")
    # AWS_S3_BUCKET = parser.get("aws_cred", "AWS_S3_BUCKET")

    s3 = boto3.client('s3', aws_access_key_id=AWS_ACCESS_KEY_ID,
                      aws_secret_access_key=AWS_SECRET_ACCESS_KEY)

    s3_file = eod

    s3.upload_file(eod, AWS_S3_BUCKET, s3_file)


def main():
    json2csv()


if __name__ == "__main__":
    main()
