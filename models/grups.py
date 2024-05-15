from odoo import models, fields

class Grups(models.Model):
    _name = 'projecta_ttima.grups'
    _description = 'Taula de Grups'
    
    persona_id =  fields.Many2one( 'projecta_ttima.persones', string='persona_id')
    Adressa = fields.Char('Adressa', size=50)
    Poblacion = fields.Char('Poblacion', size=30)
    CP = fields.Char('Codi Postal', size=5)
    Pais = fields.Char('Pais', size=30)
    Telefons = fields.Char('Telefons', size=30)
    Num_Persones = fields.Integer('Num_Persones')
    Observacions = fields.Char('Observacions', size=50)
