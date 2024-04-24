from odoo import models, fields

class rutes(models.Model):
    _name = 'projecta_ttima.rutes'
    _description ='Taula de Rutes'
    
    CodiRutes = fields.Integer('Codi Rutes')
    Nom = fields.Char('Nom')
    Preu = fields.Integer('Preu')
