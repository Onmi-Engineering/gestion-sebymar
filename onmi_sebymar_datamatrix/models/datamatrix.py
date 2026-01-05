from odoo import fields, models, api


class Datamatrix(models.Model):
    _name = 'datamatrix'
    _description = 'Datamatrix lines'
    _rec_name = 'name'

    name = fields.Char('Name', compute="_compute_reference", store=True)
    qr_code = fields.Char('Datamatrix')
    product_id = fields.Many2one('product.product')
    picking_id = fields.Many2one('stock.picking')
    move_id = fields.Many2one('stock.move')

    @api.depends('qr_code')
    def _compute_reference(self):
        for rec in self:
            ref = ''
            if rec.qr_code:
                ref += '[' + rec.qr_code + '] '
            ref += rec.product_id.name
            rec.name = ref
