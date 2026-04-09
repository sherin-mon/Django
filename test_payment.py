import requests

url = "http://127.0.0.1:8000/payment/1/"
payload = {
    'transaction_id': '123456789012'
}
files = {
    'payment_screenshot': ('receipt.png', b'fake image data', 'image/png')
}

response = requests.post(url, data=payload, files=files)
print(f"Status Code: {response.status_code}")
