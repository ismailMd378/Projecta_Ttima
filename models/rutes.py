from odoo import models, fields

class rutes(models.Model):
    _name = 'projecta_ttima.rutes'
    _description ='Taula de Rutes'
    
    CodiRutes = fields.Integer('Codi Rutes',size=4)
    Nom = fields.Char('Nom', size=40)
    Preu = fields.Integer('Preu', size=7)
