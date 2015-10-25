import os
from flask import Flask
from blockchain.wallet import Wallet
from flask.ext.cors import CORS


app = Flask(__name__)
app.config['DEBUG'] = True
CORS(app)

reader_wallet_id = 'f0ec6849-86c4-4c76-9470-d77acead7aef'
reader_wallet_password = 'unknown'
reader_send_from_address = '1AsvJjuTANsCRZUu5r86DkTa8dUpwG47MA'

author_receive_address = '1JGcSP5qu5BZG7gtt8rEaob9nxBxWaJzAz'

@app.route('/send')
def send_btc_to_author():
    print 'Attempting to send 10000 bits from reader to author for turning page'

    # Set Wallet object to readers wallet
    wallet = Wallet(reader_wallet_id, reader_wallet_password)

    # Send from wallet to new address (Receiving address (AUTHOR), Amount in satoshi, from address (READER))
    payment = wallet.send(author_receive_address, 10000, from_address=reader_send_from_address)

    # Adds 10,000 for some unknown reason in the error message when you try to send again with an unconfirmed transactions

    print 'Sent 10000 bits from reader to author for turning page'
    print 'Transaction Hash to search blockchain.info to verify transactions: ' + str(payment.tx_hash)

    # Return the balance of reader's wallet
    balance = wallet.get_balance()

    print 'Current total balance of readers wallet in Satoshi is  ' + str(balance)

    # Convert from Satoshi's to bits
    converted_balance = convert_satoshi_to_bits(balance)

    print 'Current total balance of readers wallet in Bits is  ' + str(converted_balance)

    # return current wallet balance (includes unconfirmed) for front end
    return str(converted_balance)


@app.route('/balance')
def check_balance():
    print 'Checking balance of wallet...'

    # Make sure to grab wallet of reader
    wallet = Wallet(reader_wallet_id, reader_wallet_password)

    # Pull back the balance for readers wallet
    balance = wallet.get_balance()

    print 'Current total balance of readers wallet in Satoshi is  ' + str(balance)

    converted_balance = convert_satoshi_to_bits(balance)

    print 'Current total balance of readers wallet in Bits is  ' + str(converted_balance)

    # Return current reader wallet balance for front end
    return str(converted_balance)

def convert_satoshi_to_bits(value):
    # Divide Satoshi by 100 to get value in bits
    balance = value/100

    return balance

if __name__ == "__main__":
    app.run(debug=True)
