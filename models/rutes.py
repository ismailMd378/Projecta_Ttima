from odoo import models, fields

class Rutes(models.Model):
    _name = 'projecta_ttima.rutes'
    _description ='Taula de Rutes'

    #id = fields.Integer('ID', readonly=True)
    rutes_ids = fields.Many2many(
        string=' rutes_id',
        comodel_name='projecta_ttima.rutes',
        relation='projecta_ttima_passa_per_rel',
        column1='cases_id',
        column2='rutes_id')
    
    
    Nom = fields.Char('Nom')
    Preu = fields.Integer('Preu')