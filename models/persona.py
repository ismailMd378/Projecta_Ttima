from odoo import models, fields

class Persona(models.Model):
    _name = 'rutas_bicicleta.persona'
    _description ='Taula de Persona'
    
    CodiPersona = fields.Char('Codi Persona', size=7)
    Nom = fields.Char('Nom', size=50),
    AnyNaixement = fields.Integer('Any de Naixement')