import os
from flask import Flask
from blockchain.wallet import Wallet


app = Flask(__name__)

@app.route('/')
def hello():
    print 'Hitting main route'

    wallet_id = 'c4e7c925-8a48-4a0f-bf0a-88bae5def1cb'
    wallet_password = 'Loeras2662#s2n'

    author_receive_address = '1JGcSP5qu5BZG7gtt8rEaob9nxBxWaJzAz'
    reader_send_from_address = '1HKGvNjrMuZ71jkHAFA6e77iPxWM1pranx'

    # Create new wallet Ghetto ass credentials, need to get a "FROM ADDRESS from an identifier"
    wallet = Wallet(wallet_id, wallet_password)

    # Send from wallet to new address (Receiving address (My Multibit HD for testing), Amount in satoshi, from address)
    payment = wallet.send(author_receive_address, 2000, from_address=reader_send_from_address)

    print payment.tx_hash

    return

if __name__ == "__main__":
    app.run(debug=True)
