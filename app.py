import os
from flask import Flask
from blockchain.wallet import Wallet


app = Flask(__name__)

reader_wallet_id = 'c4e7c925-8a48-4a0f-bf0a-88bae5def1cb'
reader_wallet_password = 'Loeras2662#s2n'
reader_send_from_address = '1HKGvNjrMuZ71jkHAFA6e77iPxWM1pranx'

author_receive_address = '1JGcSP5qu5BZG7gtt8rEaob9nxBxWaJzAz'

@app.route('/send')
def send_btc_to_author():
    print 'Attempting to send 2000 bits from reader to author for turning page'

    # Set Wallet object to readers wallet
    wallet = Wallet(reader_wallet_id, reader_wallet_password)

    # Send from wallet to new address (Receiving address (AUTHOR), Amount in satoshi, from address (READER))
    payment = wallet.send(author_receive_address, 2000, from_address=reader_send_from_address)

    print 'Sent 2000 bits from reader to author for turning page'
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
