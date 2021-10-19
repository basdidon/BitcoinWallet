from bitcoinlib.keys import Key
from bitcoinlib.wallets import *


def newKey():
    print('--- generate bitcoin key on mainnet ---')
    k = Key()
    k.info()


def newTestnetKey():
    print('---generate bitcoin key on testnet ---')
    tk = Key(network='testnet')
    tk.info()


def keyInfo(wif, network):
    if network == 'bitcoin'.lower():
        k = Key(wif)
        k.info()
        print('goto : https://www.blockchain.com/btc/address/' + k.address())
    if network == 'testnet'.lower():
        k = Key(wif, network='testnet')
        k.info()
    else:
        pass


def wifToKey(wif, network):
    if network == 'bitcoin'.lower():
        k = Key(wif)
        return k
    if network == 'testnet'.lower():
        k = Key(wif, network='testnet')
        return k
    else:
        pass


# mainnet WIF
k1_wif = 'L4n5A5Do6PJM4VBMVcFJ2sYSinowzjW8bzFpwtf6xzxfeNNEaYyP'
# testnet WIF
tk1_wif = 'cQ8xxsNBUtSWxv7wHJi6j53saqTrmiktaZpnzMKoariJ3Lbxz58Q'        # test_wallet_#1
tk2_wif = 'cMgmREQi7JnVSBM4pVyNnNHz34DSwnTQm42q5BjK3JHkEq1XYK2E'        # test_wallet_#2

tk1 = wifToKey(tk1_wif, 'testnet')
tk2 = wifToKey(tk2_wif, 'testnet')

print('download electrum : https://electrum.org/#download')
print('and access bitcoin address from WIF')
print('tk1.wif : ' + tk1.wif())
print('tk2.wif : ' + tk2.wif())
print('add testnet fund : https://bitcoinfaucet.uo1.net/')
print('tk1.address : ' + tk1.address())
print('tk2.address : ' + tk2.address())

# # create Wallet at first time
# w = Wallet.create('test_wallet_03', network='testnet'))

w = Wallet('test_wallet_02')        # get Wallet by wallet name
w.scan()                            # scan this wallet
w.info()                            # Show wallet info on console

# # create transaction
# w.send_to('moMPntuw5aSsznh5ZZ7sARprSk2GNz4nbq', 4000, fee=1000)
