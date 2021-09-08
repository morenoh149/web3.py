from datetime import datetime
import logging,pprint,traceback,time,json
from binance.client import Client
from web3 import Web3, HTTPProvider

#logging.basicConfig(level=logging.info)
#exec(open("tab_axies.py").read())

# w3 = Web3(Web3.HTTPProvider(endpoint_uri="https://api.roninchain.com/rpc"))
# w3 = Web3(Web3.HTTPProvider(endpoint_uri="https://mainnet.infura.io/v3/85db4eab782841da9ae4183ad6a130db"))
# ganche
w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:7545'))

# weth = w3.toChecksumAddress('0x32950db2a7164ae833121501c797d79e7b79d74c')
# event_filter = w3.eth.filter({
#     "address": weth,
#     "topics": ["0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef"],})
address_a = '0x6c980FdafA69D59E1D31a1681101f3E4197617bc'
address_b = '0x76afda2f462Bb30918d708B96314bC15Eb178bD7'
transaction = {
     'to': address_b,
     'value': 1,
     'gas': 2000000,
     'gasPrice': 234567,
     'nonce': 0,
     'chainId': 1
 }
key_a = '36b243246f5d32591343384fe169fe54fbcca0d29ab4b12a9c9edfdd56aa7257'
# signed = w3.eth.account.sign_transaction(transaction, key_a)
# print(signed.rawTransaction)
# print(signed.hash)
# print(signed.r)
# print(signed.s)
# print(signed.v)

# When you run send_raw_transaction, you get back the hash of the transaction:
# txn_hash= w3.eth.send_raw_transaction(signed.rawTransaction)  
# print('transaction', txn_hash)

event_filter = w3.eth.filter('latest')
    
# breakpoint()
e = event_filter.get_new_entries()
print('entries', e)
print('time', w3.eth.block_number)

# block = w3.eth.get_block('latest')
#print("\n".join("{}\t{}".format(k, v) for k, v in block.items()))
