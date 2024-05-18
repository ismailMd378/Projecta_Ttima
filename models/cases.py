from odoo import models, fields

class Cases(models.Model):
    _name = 'projecta_ttima.cases'
    _description = 'Taula de cases'

    id = fields.Integer('ID', readonly=True)
    NIF = fields.Char('Codi Persona', size=9)
    NomCasa = fields.Char('Nom', size=50)
    NomPersona = fields.Char('Nom de Persona', size=50)
    NomPersona2 = fields.Char('Nom de Persona2', size=50)
    Telefons = fields.Char('Telefons', size=50)
    cc = fields.Integer('cc')
    Ubicacio = fields.Char('Ubicacio', size=50)
    Adressa = fields.Char('Adressa', size=50)
