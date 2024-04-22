from odoo import models, fields

class Intermediaris(models.Model):
    _name = 'projecta_ttima.intermediaris'
    _description = 'Taula de Intermediaris'
    CodiIntermidiari = fields.Char('Codi Intermidiari', size=4)
    Nom = fields.Char('Nom', size=50)
    Adressa = fields.Char('Adressa', size=50)
    Poblacio = fields.Char('Poblacio', size=30)
    CP = fields.Char('C.P', size=5)
    Pais = fields.Char('Pais', size=30)
    Telefons = fields.Char('Telefons', size=50)
    PersonaContacte = fields.Char('Persona de Contacte', size=50)
