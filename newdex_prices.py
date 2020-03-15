
# Uses cmc_prices.txt to estimate newdex asset usd prices

import requests
import csv

import time
import datetime

ts = time.time()
print "Newdex price query USD ... " + datetime.datetime.fromtimestamp(ts).strftime('%m-%d %H:%M:%S')

with open('cmc_prices.txt', mode='r') as file:
    csv_reader = csv.reader(file,delimiter=' ')
    cmc_prices = dict((rows[0],rows[1]) for rows in csv_reader)


eos_usd_price=float(cmc_prices["EOS"])

#url = "https://api.newdex.io/v1/candles?symbol=betdicetoken-dice-eos&time_frame=4%20hours&size=1"
#data = requests.get(url).json()
#high=data['data'][0][3]
#low=data['data'][0][4]
#dice_eos_price=((high+low)/2.0)

with open('./newdex_prices.txt', 'wb') as f:
    writer = csv.writer(f,delimiter=' ')

    url = "https://api.newdex.io/v1/price?symbol=sesacashmain-ynt-tlos"
    data = requests.get(url).json()
    if data['code'] != 200:
        print "Newdex returned non-200 code when querying price"
        print data
        exit(-1)
    ynt_tlos_price=data['data']['price']

    writer.writerows([['Asset','TLOS price'],
                    ['YNT',ynt_tlos_price]])

