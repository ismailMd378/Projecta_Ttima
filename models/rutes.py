from odoo import models, fields

class Rutes(models.Model):
    _name = 'projecta_ttima.rutes'
    _description ='Taula de Rutes'
    
    CodiRutes = fields.Many2many(
        string='Codi Rutes',
        comodel_name='projecta_ttima.rutes',
        relation='projecta_ttima_cases_rutes_rel',
        column1='CodiCases',
        column2='CodiRutes')
    Nom = fields.Char('Nom')
    Preu = fields.Integer('Preu')