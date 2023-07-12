from threading import Thread
from flask import Flask, jsonify
from uniapi.modules.APRCalc.main import APR
# from uniapi.args import Args #Argparse crashed gunicorn
from uniapi.modules.WalletRanks.main import Wallets

app = Flask(__name__)
# Args.parse()

url = "http://127.0.0.1:1317"
debug=False

apr = APR(debug=debug,url=url)
wallets = Wallets(debug=debug,url=url)

Thread(target=apr.start).start()
Thread(target=wallets.start).start()

@app.route('/apr', methods=['GET'])
def get_apr():
    response = jsonify(apr.data)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/wallets', methods=['GET'])
def get_wallets():
    response = jsonify(wallets.data)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == '__main__':
    app.run()
