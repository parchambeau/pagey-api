import os
from flask import Flask
from blockchain.wallet import Wallet


app = Flask(__name__)

@app.route('/')
def hello():
    print 'Hitting main route'

    # Create new wallet Ghetto ass credentials, need to get a "FROM ADDRESS from an identifier"
    wallet = Wallet('c4e7c925-8a48-4a0f-bf0a-88bae5def1cb', 'Loeras2662#s2n')

    # Send from wallet to new address (Receiving address (My Multibit HD for testing), Amount in satoshi, from address)
    payment = wallet.send('1GKjg6fJjFFjRfJSbSzPSzxzaZZ2iwX1aJ', 100000, from_address='1HKGvNjrMuZ71jkHAFA6e77iPxWM1pranx')

    print payment.tx_hash

    return

if __name__ == "__main__":
    app.run(debug=True)
