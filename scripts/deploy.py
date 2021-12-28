from scripts.helpful_scripts import get_account
from brownie import Jemini
from web3 import Web3

initial_supply = Web3.toWei(1000, "ether")


def main():
    account = get_account()
    token = Jemini.deploy(initial_supply, {"from": account})
    print(token.name())