import hmac
import hashlib
import time
import requests
import base64
import json
import logging
import pandas as pd
from coinbase_auth import CoinbaseAuth


class CoinbaseTrade():
 
    def __init__(self, api_key, secret_key,api_url="https://api.coinbase.com"):
        """ Create an instance of the CoinbaseTrade class.
        Args:
            api_key (str): Your API key.
            secret_key (str): The secret key matching your API key.
            api_url (Optional[str]): API URL. Defaults to coinbase advanced API.
        """
        self.api_url = api_url
        self.auth = CoinbaseAuth(api_key, secret_key)
        self.session = requests.Session()
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)
        
    
    def get_request(self, request_path,params=None):
        """ Make a GET request to the Coinbase API.

        Args: 
            request_path (str): The path to the request after the base URL.
            params (Optional[dict]): A dictionary of query parameters. Defaults to None.

        Returns:
            response (requests.Response): The response from the request.
        
        """

        if params is None:
            params=dict()
        method = 'GET'
        url = self.api_url + request_path
        headers = self.auth.get_auth_headers(method,request_path)
        try:
            response = self.session.get(url, headers=headers,params=params)
            if response.status_code == 200:
                self.logger.info('Successfully')
                return response.json()
            else:
                self.logger.error('Request failed with status code: ', response.status_code)
        except resquests.exceptions.RequestException as e:
            self.logger.error('Something went wrong: %s', e)

    #def post_request(self, url, params=None):

    def get_fills(self,order_id=None,product_id = None):
        """
        Get a list of fills filtered by optional query parameters (product_id, order_id, etc).
        Requires at least product_id or order_id.

        Args: 
            - order_id (Optional[str]): The order id to filter by.
            - product_id (Optional[str]): The product id to filter by.

        Returns:
            list: A list of fills.
                [
                        {
                            "trade_id": 74,
                            "product_id": "BTC-USD",
                            "price": "10.00",
                            "size": "0.01",
                            "order_id": "d50ec984-77a8-460a-b958-66f114b0de9b",
                            "created_at": "2014-11-07T22:19:28.578544Z",
                            "liquidity": "T",
                            "fee": "0.00025",
                            "settled": true,
                            "side": "buy"
                        },
                        {
                            ...
                        }
                    ]
        Raises:
            - KeyError: Raises an exception.
        '"""
        
        request_path = '/api/v3/brokerage/orders/historical/fills'

        params = {}
        if order_id is not None:
            params['order_id'] = order_id
        if product_id is not None:
            params['product_id'] = product_id

        result = self.get_request(request_path,params)
        return result
        # cleanup_result = self.cleanup.historical_fill_cleanup(result)
        # self.logger.info(cleanup_result)

