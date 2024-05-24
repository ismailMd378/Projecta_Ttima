from odoo import models,api

class ReservesReport(models.AbstractModel):
    _name = 'report.projecta_ttima.report_reserves'

    @api.model
    def _get_report_values(self, docids, data=None):
        docs = self.env['projecta_ttima.reserves'].browse(docids)
        return {
            'doc_ids': docids,
            'doc_model': 'projecta_ttima.reserves',
            'docs': docs,
        }
