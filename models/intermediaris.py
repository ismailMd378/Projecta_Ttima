from odoo import models, fields

class Intermediaris(models.Model):
    _name = 'projecta_ttima.intermediaris'
    _description = 'Taula d\'Intermediaris'

    CodiIntermediaris = fields.Char(
        string='Codi Intermediaris',
    )
    
    CodiFacturaFinalServeis = fields.One2many(
        'projecta_ttima.factura_serveis',
        'CodiIntermediaris',
        string='Factures de Serveis'
    )
    Nom = fields.Char('Nom', size=50)
    Adressa = fields.Char('Adreça', size=50)
    Poblacio = fields.Char('Població', size=30)
    CP = fields.Char('Codi Postal', size=5)
    Pais = fields.Char('País', size=30)
    Telefons = fields.Char('Telèfons', size=50)
    PersonaContacte = fields.Char('Persona de Contacte', size=50)