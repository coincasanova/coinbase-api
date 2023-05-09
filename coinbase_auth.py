
import json,hmac,hashlib,time,requests
from requests.auth import AuthBase


"""
Authentication class to hash our API keys
https://docs.cloud.coinbase.com/sign-in-with-coinbase/docs/api-key-authentication

Args: 
    api_key 
    secret_key

Returns:
    CoinbaseAuth will return a hashed authentication

Raises:
    KeyError: Raises an exception.
"""

class CoinbaseAuth(AuthBase):
    def __init__(self,api_key,secret_key):
        self.api_key = api_key
        self.secret_key = secret_key
        
    def get_auth_headers(self,method,request_path, body=''):
        timestamp = str(int(time.time()))
        message = timestamp + method.upper() + request_path + body
        signature = hmac.new(self.secret_key.encode('utf-8'), message.encode('utf-8'), digestmod=hashlib.sha256).hexdigest()
        
        return {
            'CB-ACCESS-SIGN': signature,
            'CB-ACCESS-TIMESTAMP': timestamp,
            'CB-ACCESS-KEY': self.api_key,
            'Content-Type':'application/json'
        }
        