from odoo import models, fields

class RutaBicicleta(models.Model):
    _name = 'rutas.bicicleta'
    _description = 'Modelo para almacenar rutas de bicicleta'
     
    CodiReserva = fields.Char('Codi Reserva' , size=7, required=True)
    DataArrivada = fields.Date('Date Arivada')
    NitExtra = fields.Boolean('Nit Extra')
    

