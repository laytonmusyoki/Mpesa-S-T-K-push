from flask import Flask,request
import requests
from datetime import datetime
import json
import base64
from requests.auth import HTTPBasicAuth

app = Flask(__name__)
my_endpoint="https//d782-102-135-169-122.eu.ngrok.io"

@app.route('/paynow')
def init_stk():
    amount=request.args.get('amount')
    phone=request.args.get('phone')

    endpoint = 'https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest'
    access_token = Access_token2()
    headers = { "Authorization": "Bearer %s" % access_token }
    Timestamp = datetime.now()
    times = Timestamp.strftime("%Y%m%d%H%M%S")
    password = "174379" + "bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919" + times

    data = {
        "BusinessShortCode": "174379",
        "Password": password,
        "Timestamp": times,
        "TransactionType": "CustomerPayBillOnline",
        "PartyA": phone,
        "PartyB": "174379",
        "PhoneNumber": phone,
        "CallBackURL": "https://modcom.co.ke/job/confirmation.php",
        "AccountReference": "TestPay",
        "TransactionDesc": "HelloTest",
        "Amount": amount
    }

    res = requests.post(endpoint, json = data, headers = headers)
    return res.json()

@app.route('/authenticate2')
def Access_token2():
    key = 'euwcvNjSSEJA7s59GjCwair04AJApGqG'
    secret = 'Db7CozA3TJqNe6f0'
    api_sandbox_url = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"

    
    response = requests.get(api_sandbox_url, auth=HTTPBasicAuth(key, secret))
    data = response.json()
    return data['access_token']
    

   
if __name__ == '__main__':
    app.run(debug=True)
