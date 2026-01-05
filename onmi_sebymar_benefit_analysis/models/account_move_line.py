from odoo import fields, models, api


class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    purchase_price = fields.Float(
        string='Cost', compute="_compute_purchase_price",
        digits='Product Price', readonly=False, store=True)
    margin = fields.Monetary(
        "Margin", compute='_compute_margin_invoice', store=True, currency_field='currency_id')
    move_type = fields.Selection(related="move_id.move_type")
    product_categ_id = fields.Many2one(related="product_id.categ_id", store=True)
    product_retail = fields.Boolean(related="product_id.retail", store=True)
    product_cabin = fields.Boolean(related="product_id.cabin", store=True)
    product_collection_id = fields.Many2one(related="product_id.collection_id", store=True)
    product_type_id = fields.Many2one(related="product_id.type_id", store=True)

    @api.depends('product_id.standard_price')
    def _compute_purchase_price(self):
        for line in self:
            if not line.product_id:
                line.purchase_price = 0.0
                continue
            line = line.with_company(line.company_id)
            product_cost = line.product_id.standard_price
            line.purchase_price = product_cost

    @api.depends('purchase_price', 'price_unit', 'quantity')
    def _compute_margin_invoice(self):

        for line in self:
            if line.move_type == 'out_invoice':
                line.margin = line.price_subtotal - (line.purchase_price * line.quantity)
            if line.move_type == 'out_refund':
                line.margin = (line.price_subtotal - (line.purchase_price * line.quantity)) * -1

    def update_benefits(self):
        self._compute_purchase_price()
