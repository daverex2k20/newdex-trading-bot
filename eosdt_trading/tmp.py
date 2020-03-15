
import requests
import os
import json

url='cleos -u https://eos.greymass.com get transaction afdf978b7c8de58a1f261b94b80d1939d1e1b4fe0aeb6fe2fbce2b1dc739f450'
#trx_info = os.popen(url).read().json()
try:
    response = os.popen(url).read()
    trx_info = json.loads(response)
except:
    print "Exception"
#data = requests.get(url).json()

print trx_info

#if "web" in trx_info["trx"]["trx"]["actions"][0]["data"]["memo"]:
#    print "yeah!"

exit()

def test_fn( input ):
    if input=="a":
        return "blah"
    else:
        print "Im not returning anything."

poo='a'
ret=test_fn( url )

print "printing return:..."
print ret

if ret==None:
    print "exiting"

