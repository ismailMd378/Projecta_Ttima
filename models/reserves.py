from odoo import models, fields

class Reserves(models.Model):
    _name = 'projecta_ttima.reserves'
    _description = 'Taula de Reserves'
     
    CodiReserva = fields.Char('Codi Reserva', size=7, required=True)
    DataArrivada = fields.Date('Data Arribada')
    NitExtra = fields.Boolean('Nit Extra')
    Num_Bicis = fields.Integer('Num De Bicis')
    DataReserva = fields.Date('Data Reserva')
    CodiIntermediari = fields.Char( string='Codi Intermidiari')
    CodiGrup = fields.Integer('Codi Grup')
    GrupRuta = fields.Integer('Codi Ruta')
