from odoo import models, fields

class Habitacions(models.Model):
    _name = 'projecta_ttima.habitacions'
    _description = 'Taula de Habitacions'
    
    habitacions_ids = fields.Many2many(
    string='habitacions_id',
    comodel_name='projecta_ttima.habitacions',
    relation='reserves_habitacions_rel',
    column1='reserves_id',
    column2='habitacions_id',
)
    cases_id = fields.Many2one('projecta_ttima.cases', string = 'cases_id')
    Num_llits = fields.Integer('Num_llits')
    Bany = fields.Boolean('Bany')
    Observacions = fields.Char('Observacions', size=50)
