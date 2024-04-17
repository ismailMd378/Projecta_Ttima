from odoo import models, fields

class Reserves(models.Model):
    _name = 'rutas_bicicleta.reserves'
    _description = 'Taula de Reserves'
     
    CodiReserva = fields.Char('Codi Reserva' , size=7, required=True)
    DataArrivada = fields.Date('Date Arivada')
    NitExtra = fields.Boolean('Nit Extra')
    Num_Bicis = fields.Integer('Num De Bicis')
    DataReserva = fields.Date('Data Reserva')
    CodiIntermidiari = fields.Many2one('Intermidiari.model', string = 'Codi_Intermidiari')
    CodiGrup = fields.Many2one('Codi.grup', string='Code Groupe')
    GrupRuta = fields.Many2one('Codi.Ruta', string = 'Codi Ruta')
    CodiTarifa = fields.Many2one('Codi.Tarifa, string = 'Codi Tarifa)
    

    

=======
    CodiIntermidiari = fields.Many2one('Intermidiari.model', string = 'Codi_Intermidiari')
    CodiGrup = fields.Many2one('Codi.grup', string='Code Groupe')
    GrupRuta = fields.Many2one('Codi.Ruta', string = 'Codi Ruta')
    CodiTarifa = fields.Many2one('Codi.Tarifa', string = 'Codi Tarifa')
    DataArribada = fields.Date('Date d\ Arribada')
    DataSortida = fields.Date('Data de Sortida')
    NitExtra = fields.Boolean('Nit Extra')
    Num_Bicis = fields.Integer('Num De Bicis', size=3)
    DataReserva = fields.Date('Data de Reserva')
>>>>>>> Hicham
