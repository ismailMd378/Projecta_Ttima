from odoo import models, fields

class Reserves(models.Model):
    _name = 'projecta_ttima.reserves'
    _description = 'Taula de Reserves'
     
    id = fields.Integer(string='ID', readonly=True)
    reserves_ids = fields.Many2many(
        string='reserves_id',
        comodel_name='projecta_ttima.reserves',
        relation='reserves_habitacions_rel',
        column1='habitacions_id',
        column2='reserves_id',
    )
    DataArrivada = fields.Date('Data Arribada')
    NitExtra = fields.Boolean('Nit Extra')
    Num_Bicis = fields.Integer('Num De Bicis')
    DataReserva = fields.Date('Data Reserva')
    intermediaris_id = fields.Many2one( 'projecta_ttima.intermediaris',string='Codi Intermediaris')
    grups_id = fields.Many2one('projecta_ttima.grups',string='Codi Grup')
    rutes_id = fields.Many2one('projecta_ttima.rutes',string='Codi Ruta')
