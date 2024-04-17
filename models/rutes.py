from odoo import models, fields

class rutes(models.Model):
    _name = 'rutas_bicicleta.rutes'
    _description ='Taula de Rutes'
    
    CodiRutes = fields.Integer('Codi Rutes',size=4)
<<<<<<< HEAD
    Nom = fields.Char('Nom', size=40)
=======
    Nom = fields.Char('Nom', size=50)
>>>>>>> Hicham
    Preu = fields.Integer('Preu', size=7)