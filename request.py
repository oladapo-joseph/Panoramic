from requests import Session
from requests.exceptions import Timeout, TooManyRedirects
import json

class Coin:
    
    """"
        This class makes api call to the coinmarketcap web to retrieve some data about 
        a specified coin
    
    
    """
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'

    parameters = {
    'symbol':'BTC,ETH,BNB,XRP',
    'convert':'USD'
    }
    headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': '8c556046-54e0-4a95-8154-6946d2320bee',
    }

    def __init__(self, ):
        self.session = Session()
        self.session.headers.update(self.headers)

    def retrieve(self, detail='price')-> str :
        """
            Args:
                detail: str,
                    could be "price", 'volume_24h', 'volume_change_24h', 'market_cap'

        """
        try:
            response = self.session.get(self.url, params=self.parameters)
            data = json.loads(response.text)
            list_ = self.parameters['symbol'].split(',')
            print(detail)
            for token in list_:
                print(token , data['data'][token]['quote']['USD'][detail])
            date, time = data['data'][token]['quote']['USD']['last_updated'].split('T')
            print("As at ", date , time.split('.')[0] )
        except (Timeout, TooManyRedirects) as e:
            print(e)
            
        
        
        
coin = Coin()

coin.retrieve('volume_24h')        
        

"""
        Sample output 

        volume_24h
        BTC 19102362923.404392
        ETH 9159183768.742136
        BNB 1654418111.7116253
        XRP 851429210.6031173
        As at  2022-05-22 11:23:00


"""