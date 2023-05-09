import json
import logging
import pandas as pd


class CoinbaseCleanup():
    def __init__(self):
        """ Create an instance of the AuthenticatedClient class.
        Args:
            api_key (str): Your API key.
            secret_key (str): The secret key matching your API key.
            api_url (Optional[str]): API URL. Defaults to coinbase advanced API.
        """
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)

    def historical_fill_cleanup(self, result):
        self.logger.info('Cleaning up historical')
        

