# cosna_wallet
A controller to access endpoints in the cosna wallet integration API.

## Installation
Install the cosna_wallet package by running the the following command:
```
pip install cosna_wallet
```
or 
```
pip3 install cosna_wallet
```

## Usage
To use the cosna_wallet package:
```python
from cosna_wallet import cosna_wallet

wallet = cosna_wallet.CosnaWallet('XXXXXXXXXXXXXXXX','XXXXXXXXXXXXXXXX')

response = wallet.init_payment({
        "amount": 300,
        "currency": "XAF",
        "hash": "XXXXXXXXXXXXXXXX",
        "return_url": "https://www.fb.com",
        "cancel_url": "https://www.yt.com",
        "callback_url": "https://beta.cosna-afrique.com"
    }
)

print(response)
print(response.text)
```
