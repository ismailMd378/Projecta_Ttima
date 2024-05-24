from odoo import models, fields, api

class Reserves(models.Model):
    _name = 'projecta_ttima.reserves'
    _description = 'Taula de Reserves'
     
    #id = fields.Integer(string='ID', readonly=True)
    reserves_ids = fields.Many2many(
        string='reserves_id',
        comodel_name='projecta_ttima.reserves',
        relation='reserves_habitacions_rel',
        column1='habitacions_id',
        column2='reserves_id',
    )
    DataArribada = fields.Date('Data Arribada')
    NitExtra = fields.Boolean('Nit Extra')
    Num_Bicis = fields.Integer('Num De Bicis')
    DataReserva = fields.Date('Data Reserva')
    intermediaris_id = fields.Many2one( 'projecta_ttima.intermediaris',string='Codi Intermediaris', index=True)
    grups_id = fields.Many2one('projecta_ttima.grups',string='Codi Grup', index=True)
    rutes_id = fields.Many2one('projecta_ttima.rutes',string='Codi Ruta', index=True)
    
    name = fields.Char(string='Nom', compute='_compute_name', store=True)
    
    @api.depends('DataArribada', 'intermediaris_id', 'grups_id')
    def _compute_name(self):
        for record in self:
            intermediari_name = record.intermediaris_id.Nom if record.intermediaris_id else 'Sense Intermediari'
            grup_name = record.grups_id.persones_id.Nom if record.grups_id else 'Sense Grup'
            record.name = f"Reserva: {record.DataArribada} - {intermediari_name} - {grup_name}"
            
   