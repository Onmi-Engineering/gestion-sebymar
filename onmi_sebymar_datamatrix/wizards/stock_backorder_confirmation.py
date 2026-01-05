from odoo import fields, models, api


class StockBackorderConfirmation(models.TransientModel):
    _inherit = 'stock.backorder.confirmation'

    def process(self):
        res = super(StockBackorderConfirmation, self).process()
        if self.pick_ids and self.pick_ids.sale_id:
            self.sudo().pick_ids.sale_id.picking_ids[:2].sudo().generate_datamatrix_lines()

        return res