from odoo import models, fields

class PassaPer(models.Model):
    _name = 'projecta_ttima.passa_per'
    _description = 'Taula de Passa Per'
    
    CodiRutes = fields.Many2one(
        string='Codi Rutes',
        comodel_name='projecta_ttima.rutes',
        column='CodiRutes')
        
    CodiCasa = fields.Many2one(
        string='Codi Casa',
        comodel_name='projecta_ttima.cases',
        column='CodiCasa') 