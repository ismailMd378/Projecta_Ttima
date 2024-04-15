from odoo import models, fields

class RutaBicicleta(models.Model):
    _name = 'rutas.bicicleta'
    _description = 'Modelo para almacenar rutas de bicicleta'
     
    CodiReserva = fields.Char('Codi Reserva' , size=7, required=True)
    DataArrivada = fields.Date('Date Arivada')
    NitExtra = fields.Boolean('Nit Extra')
    Num_Bicis = fields.Integer('Num De Bicis')
    DataReserva = fields.Date('Data Reserva')
    CodiIntermidiari = fields.Many2one('Intermidiari.model', string = 'Codi_Intermidiari')
    CodiGrup = fields.Many2one('Codi ')
    GrupRuta = fields.Many2one('Grup.model', string = 'Codikrup')

    

