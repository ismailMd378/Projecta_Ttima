from odoo import models, fields

class Persones(models.Model):
    _name = 'projecta_ttima.persones'
    _description = 'Taula de Persones'
    
    CodiPersona = fields.Char('Codi Persona', size=7)
    Nom = fields.Char('Nom', size=50)
    AnyNaixement = fields.Integer('Any de Naixement')
