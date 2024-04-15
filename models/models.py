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
    CodiGrup = fields.Many2one('Codi ', string = 'Codi Grup')
   

class TaulaRutes(models.Model):
    _name = 'taula.rutes'
    _description = 'Taula de rutes'

    codi_ruta = fields.Char('CodiRuta', size=4, required=True)
    nom = fields.Char('Nom', size=50)
    preu = fields.Float('Preu', digits=(7, 2))




    

