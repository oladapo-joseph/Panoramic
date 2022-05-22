from odoo import models, fields ,api


# class User(models.Model):
#     _name = 'user_profiles'
    
#     username = fields.Char(String= 'Username', required=True)
#     price =  fields.Char(String= 'price')
#     coin = fields.Selection([
#         ('btc', 'BTC'),
#         ('eth', 'ETH'),
#         ('bnb', 'BNB'),
#           ], required=True, default='btc')
        
        
#     detail = fields.Char(string= 'Detail (volume, price)')
    
class CoinProfile(models.Model):
    _name = "coin.profile"
    _description = "Coin Profile"
    
    username = fields.Char(String='Name', required=True)
    coin = fields.Selection([
        ('btc', 'BTC'),
        ('eth', 'ETH'),
        ('bnb', 'BNB'),
          ], required=True, default='btc')
         
    detail = fields.Selection([
        ('price', 'Price'),
        ('24h_volume', 'volume_24h'),
        ('24h_Change', 'volume_change_24h'),
        ('Market_cap', 'market_cap')
          ], required=True, default='Price')