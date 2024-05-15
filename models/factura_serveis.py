from odoo import models, fields

class factura_serveis(models.Model):
    _name = 'projecta_ttima.factura_serveis'
    _description ='Taula Factura de Serveis'
    

    
    intermediaris_id = fields.Many2one(
        'projecta_ttima.intermediaris',
        string='intermediaris_id',
        inverse_name='factura_serveis_id'
        )
    Description =  fields.Char(string='Descripció')
    Data = fields.Date(
        string='Data',
        default=fields.Date.today
    )
    TotalSuplert = fields.Integer(string='Total Suplert')
    TotalPagar = fields.Integer(string='Total Pagar')
    DataPagar = fields.Date(string='Data Pagar', default=fields.Date.today)    
    