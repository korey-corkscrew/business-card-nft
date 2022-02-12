from brownie import BusinessCardNFT, accounts
import os

myaccount = accounts.add(os.getenv("PRIVATE_KEY"))
dev = accounts.at(myaccount)

def deploy(name, symbol, businessCardURI, gasPrice):
    return BusinessCardNFT.deploy(name, symbol, businessCardURI, {'from': dev, 'gas_price': gasPrice})

def totalSupply():
    return BusinessCardNFT[-1].totalSupply()

def businessCardURI():
    return BusinessCardNFT[-1].businessCardURI()

def mint(gasPrice):
    return BusinessCardNFT[-1].mint({'from': dev, 'gas_price': gasPrice})

def pause(gasPrice):
    return BusinessCardNFT[-1].pause({'from': dev, 'gas_price': gasPrice})

def unpause(gasPrice):
    return BusinessCardNFT[-1].unpause({'from': dev, 'gas_price': gasPrice})



def main():
    deploy("Bobby Jeffrey Hill", "BJH", "https://static.wikia.nocookie.net/kingofthehill/images/5/59/Bobbeah.jpg/revision/latest?cb=20200724170428", '40 gwei')

    mint('40 gwei')

    print(totalSupply())

    print(businessCardURI())