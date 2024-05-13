from odoo import models, fields

class Reserves(models.Model):
    _name = 'projecta_ttima.reserves'
    _description = 'Taula de Reserves'
     
    CodiReserva = fields.Many2many(
        string='CodiReserva',
        comodel_name='projecta_ttima.reserves',
        relation='reserves_habitacions_rel',
        column1='CodiHabitacio',
        column2='CodiReserva',
    )
    DataArrivada = fields.Date('Data Arribada')
    NitExtra = fields.Boolean('Nit Extra')
    Num_Bicis = fields.Integer('Num De Bicis')
    DataReserva = fields.Date('Data Reserva')
    CodiIntermediaris = fields.Many2one( 'projecta_ttima.intermediaris',string='Codi Intermediaris')
    CodiGrup = fields.Many2one('projecta_ttima.grups',string='Codi Grup')
    CodiRutes = fields.Many2one('projecta_ttima.rutes',string='Codi Ruta')
