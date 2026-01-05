from odoo import fields, models, api


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    commercial_note = fields.Html(related='sale_id.commercial_note')
