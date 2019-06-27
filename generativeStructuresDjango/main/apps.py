
from django.apps import AppConfig

# https://hackernoon.com/creating-a-python-ethereum-interface-part-1-4d2e47ea0f4d

from web3 import Web3, HTTPProvider
import os
from interface import ContractInterface

class TEMP(object):
    def __init__(self):
        max_deploy_gas = 0


# Initialize web3 object
web3 = Web3(HTTPProvider('http://localhost:8545')) #Ganache default host + port

# Path for Solidity source files
contract_dir = os.path.abspath('./contracts')

# Initialize interface
interface = ContractInterface(web3, 'TEST', contract_dir)

# Compile contracts & deploy
interface.compile_source_files()
interface.deploy_contract()

# Estimate gas usage. Can be used to deploy if it's below X value
# TODO What class is this in?
deployment_estimate = deployment.constructor().estimateGas(transaction = deployment_params)
if deployment_estimate < self.max_deploy_gas:
    tx_hash = deployment.constructor().transact(transaction = deployment_params)


tx_receipt = self.web3.eth.waitForTransactionReceipt(tx_hash)
contract_address = tx_receipt['contractAddress']

vars = {
    'contract_address': contract_address,
    'contract_abi': deployment_compiled['abi']
}

with open (self..deployment_vars_path, 'w') as write_file:
    json.dump(vars, write_file, indent = 4)

interface.get_instance()

# # web3.contract.Contract
# # Contract.address




class MainConfig(AppConfig):
    name = 'main'
