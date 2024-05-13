from odoo import models, fields

class Habitacions(models.Model):
    _name = 'projecta_ttima.habitacions'
    _description = 'Taula de Habitacions'
    
    
    CodiHabitacio = fields.Many2many(
        string='CodiHabitacio',
        comodel_name='projecta_ttima.habitacions',
        relation='reserves_habitacions_rel',
        column1='CodiReserva',
        column2='CodiHabitacio',
    )
    CodiCasa = fields.Many2one('projecta_ttima.cases', string = 'CodiCasa')
    Num_llits = fields.Integer('Num_llits')
    Bany = fields.Boolean('Bany')
    Observacions = fields.Char('Observacions', size=50)
