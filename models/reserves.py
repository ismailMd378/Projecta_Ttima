from odoo import models, fields

class Reserves(models.Model):
    _name = 'projecta_ttima.reserves'
    _description = 'Taula de Reserves'
     
    CodiReserva = fields.Char('Codi Reserva', size=7, required=True)
    DataArrivada = fields.Date('Data Arribada')
    NitExtra = fields.Boolean('Nit Extra')
    Num_Bicis = fields.Integer('Num De Bicis')
    DataReserva = fields.Date('Data Reserva')
    CodiIntermidiari = fields.Many2one('projecta_ttima.intermediaris', string='Codi Intermidiari')
    CodiGrup = fields.Many2one('projecta_ttima.grups', string='Codi Grup')
    GrupRuta = fields.Many2one('projecta_ttima.ruta', string='Codi Ruta')
    CodiTarifa = fields.Many2one('projecta_ttima.tarifa', string='Codi Tarifa')
