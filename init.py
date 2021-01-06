import os
import hashlib
import marshal
from uuoskit import uuosapi, wallet, config

if os.path.exists('test.wallet'):
    os.remove('test.wallet')
psw = wallet.create('test')

# active key of wkpmdjdsztyu
wallet.import_key('test', '5Jaz37nnxbpAiAGQEsyxtnGfCPTJFjX9Wn6zv7V41Ko6DXSqhd9')
# active key of ceyelqpjeeia
wallet.import_key('test', '5JfZz1kXF8TXsxQgwfsvZCUBeTQefYSsCLDSbSPmnbKQfFmtBny')

uuosapi.set_node('http://127.0.0.1:8888')
uuosapi.set_node('https://api.testnet.eos.io')

config.setup_eos_test_network()

python_contract = config.python_contract
test_account1 = 'wkpmdjdsztyu'