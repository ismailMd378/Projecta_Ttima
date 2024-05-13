from odoo import models, fields

class reserves_habitacions(models.Model):
    _name = 'projecta_ttima.reserves_habitacions'
    _description = 'Taula reserves_habitacions'
    
    CodiReserva = fields.Many2one(
        string='Codi Reserva',
        comodel_name='projecta_ttima.reserves',
        )
        
    CodiHabitacio = fields.Many2one(
        string='Codi Habitacio',
        comodel_name='projecta_ttima.habitacions',
        ) 
    
    DataConfirmacio = fields.Date(
        string='Data De Confirmacio',
        default=fields.Date.today(),
    )

    DataAribada =  fields.Date(
        string='Data Aribada',
        default=fields.Date.today(),
    )

    DataSortida  = fields.Date(
        string='Data de Sortida',
        default=fields.Date.today(),
    )