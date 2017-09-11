#!/usr/bin/python2
from coinbase.wallet.client import Client
import json
import creds
import datetime


def logger(date_time, total_euro_value):
    f = open("log.csv", "a")
    message = "%s,%f\n" %(date_time, total_euro_value)
    f.write(message)
    f.close()

def main():
    current_datetime = datetime.datetime.now()
    print "[+] Current Datetime: %s" %(current_datetime)
    client = Client(creds.api_key, creds.api_secret)
    data = client.get_accounts()
    total_euro_value = 0.00
    for x in range(0,4):
        currency_type = data[x]["balance"]["currency"]
        currency_amount = data[x]["balance"]["amount"]
        euros_amount = data[x]["native_balance"]["amount"]
        print "[+] You have %s %s valued at %s euros" %(currency_amount, currency_type, euros_amount)
        total_euro_value = total_euro_value + float(euros_amount)
    print "[+] Total euro worth is: %f " %(float(total_euro_value))
    logger(current_datetime, total_euro_value)

if __name__ == "__main__":
    main()
