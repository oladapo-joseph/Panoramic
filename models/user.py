from odoo import models, fields ,api


class User(models.Model):
    _name = 'user_profiles'
    
    username = fields.Char(String= 'Username', required=True)
    price =  fields.Char(String= 'price')
    coin = fields.Char(string= 'Coin')
    detail = fields.Char(string= 'Detail (volume, price)')
    
