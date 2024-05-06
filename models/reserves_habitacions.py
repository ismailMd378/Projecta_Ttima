from odoo import models, fields

class reserves_habitacions(models.Model):
    _name = 'projecta_ttima.reserves_habitacions'
    _description = 'Taula reserves_habitacions'
    
    CodiReserves = fields.Many2one(
        string='Codi Reserves',
        comodel_name='projecta_ttima.reserves',
        column='CodiReserva')
        
    CodiHabitacio = fields.Many2one(
        string='Codi Habitacio',
        comodel_name='projecta_ttima.habitacions',
        column='CodiHabitacio') 
    

    DataConfirmacio = fields.Date(
        string='Data De Confirmacio',
        default=fields.Date.context_today,
    )

    DataAribada =  fields.Date(
        string='Data Aribada',
        default=fields.Date.context_today,
    )

    DataSortida  = fields.Date(
        string='Data de Sortida',
        default=fields.Date.context_today,
    )
    
    
    