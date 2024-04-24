from odoo import models, fields

class PassaPer(models.Model):
    _name = 'projecta_ttima.passa_per'
    _description = 'Taula de Passa Per'
    
    CodiRutes = fields.Many2one(
        string='Codi Rutes',
        comodel_name='projecta_ttima.rutes',
        column='CodiRutes')
        
    CodiCases = fields.Many2one(
        string='Codi Cases',
        comodel_name='projecta_ttima.cases',
        column='CodiCases') 