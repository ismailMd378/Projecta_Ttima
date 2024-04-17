from odoo import models, fields

class Grups(models.Model):
    _name = 'rutas_bicicleta.grups'
    _description ='Taula de Grups'
    
    CodiGrup = fields.Char('Codi Grups', size=6,required=True)
    CodiPersonalEnCap = fields.Many2One('Personal.model', string='Personal en Cap')
    Adressa = fields.Char('Adressa', size=50)
    Poblacion = fields.Char('Poblacion', size=30)
    CP = fields.Char('Codi Postal', size=5)
    Pais = fields.Char('Pais', size=30)
    Telefons = fields.Char('Telefons', size=30)
    Num_Persones = fields.Integer('Num_Persones')
    Observacions = fields.Char('Observacions', size=50)