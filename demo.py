from datetime import datetime
import logging,pprint,traceback,time,json
from binance.client import Client
from web3 import Web3, HTTPProvider

#logging.basicConfig(level=logging.info)
#exec(open("tab_axies.py").read())

w3 = Web3(Web3.HTTPProvider(endpoint_uri="https://api.roninchain.com/rpc"))
# w3 = Web3(Web3.HTTPProvider(endpoint_uri="https://mainnet.infura.io/v3/85db4eab782841da9ae4183ad6a130db"))

weth = w3.toChecksumAddress('0x32950db2a7164ae833121501c797d79e7b79d74c')
event_filter = w3.eth.filter({
    "address": weth,
    "topics": ["0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef"],})
    
breakpoint()
e = event_filter.get_new_entries()
print('entries', e)