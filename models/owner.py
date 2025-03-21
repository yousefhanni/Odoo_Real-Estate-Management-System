from odoo import models,fields

class Owner(models.Model):
    _name = 'owner'
    
    name=fields.Char(required=1,default='New Owner')    
    phone=fields.Char()
    address=fields.Char()
    property_ids = fields.One2many('property','owner_id',string='Properties')
    
    
    