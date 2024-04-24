from odoo import models, fields

class Habitacions(models.Model):
    _name = 'projecta_ttima.habitacions'
    _description = 'Taula de Habitacions'
    
    CodiHabitacio = fields.Char('Codi Habitacio', size=6)
    CodiCasa = fields.Char('Codi Casa', size=3)
    Num_llits = fields.Integer('Num_llits')
    Bany = fields.Boolean('Bany')
    Observacions = fields.Char('Observacions', size=50)
