from odoo import models, fields

class Persones(models.Model):
    _name = 'projecta_ttima.persones'
    _description = 'Taula de Persones'
    
    #id = fields.Integer(string='ID', readonly=True)
    Nom = fields.Char('Nom', size=50)
    AnyNaixement = fields.Integer('Any de Naixement')
