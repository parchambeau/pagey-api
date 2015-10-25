import os
from flask import Flask
from blockchain.wallet import Wallet


app = Flask(__name__)

@app.route('/')
def send_btc_to_author():
    print 'Sending 2000 bits from reader to author for turning page'

    wallet_id = 'c4e7c925-8a48-4a0f-bf0a-88bae5def1cb'
    wallet_password = 'Loeras2662#s2n'

    author_receive_address = '1JGcSP5qu5BZG7gtt8rEaob9nxBxWaJzAz'
    reader_send_from_address = '1HKGvNjrMuZ71jkHAFA6e77iPxWM1pranx'

    # Set Wallet ojbect to send from
    wallet = Wallet(wallet_id, wallet_password)

    # Send from wallet to new address (Receiving address (AUTHOR), Amount in satoshi, from address (READER))
    payment = wallet.send(author_receive_address, 2000, from_address=reader_send_from_address)

    print 'Transaction Hash to search blockchain.info to verify transactions: ' + str(payment.tx_hash)

    return

@app.route('/balance')
def check_balance():
    print 'Checking balance of wallet...'

    return


if __name__ == "__main__":
    app.run(debug=True)
