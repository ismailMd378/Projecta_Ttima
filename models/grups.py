from odoo import models, fields

class Grups(models.Model):
    _name = 'projecta_ttima.grups'
    _description = 'Taula de Grups'
    
  
    CodiPersonalEnCap = fields.Many2one('projecta_ttima.persones', string='Codi Personal en Cap')
    Adressa = fields.Char('Adreça', size=50)
    Poblacio = fields.Char('Població', size=30)
    CP = fields.Char('Codi Postal', size=5)
    Pais = fields.Char('País', size=30)
    Telefons = fields.Char('Telèfons', size=30)
    Num_Persones = fields.Integer('Nombre de Persones')
    Observacions = fields.Char('Observacions', size=50)
