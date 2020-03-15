
# Generates a cmc text file and then parses it to display the prices

import requests
import csv

from pprint import pprint

import time
import datetime

ts = time.time()
print "Coingecko price query ... " + datetime.datetime.fromtimestamp(ts).strftime('%m-%d %H:%M:%S')

with open('./gecko_prices.txt', 'wb') as f:
    writer = csv.writer(f,delimiter=' ')

    # Bitcoin
    #url = "https://api.coinmarketcap.com/v1/ticker/bitcoin/"
    url = "https://api.coingecko.com/api/v3/simple/price?ids=equilibrium-eosdt&vs_currencies=eos"
    data = requests.get(url).json()
    eosdt_price=data['equilibrium-eosdt']['eos']

    ## EOS
    #url = "https://api.coinmarketcap.com/v1/ticker/eos/"
    #data = requests.get(url).json()
    #eos_price=data[0]['price_usd']

    writer.writerows([['Asset','EOS_price'],['EOSDT',eosdt_price]])


