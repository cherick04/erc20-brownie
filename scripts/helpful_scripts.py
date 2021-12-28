from brownie import network, config, accounts

LOCAL_BLOCKCHAIN_ENVIRONMENTS = [
    "development",
    "ganache",
    "ganache-local",
    "hardhat",
    "mainnet-fork",
]


def get_account(index=None, id=None):
    # accounts[0]
    # accounts.add("env")
    # accounts.load("id")
    if index:
        return accounts[index]
    if id:
        return accounts.load(id)
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        # Only works for local ganache
        return accounts[0]

    return accounts.add(config["wallets"]["from_key"])
