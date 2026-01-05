from odoo import fields, models, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    commercial_note = fields.Html('Commercial Note')

    order_line_product = fields.Many2one(
        related='order_line.product_template_id',
        string='Producto',
        readonly=True,
        store=True
    )


    product_retail = fields.Boolean(
        related='order_line.product_template_id.retail',
        string='Retail',
        store=True,
        readonly=True
    )

    product_cabin = fields.Boolean(
        related='order_line.product_template_id.cabin',
        string='Cabin',
        store=True,
        readonly=True
    )

    product_collection_id = fields.Many2one(
        related='order_line.product_template_id.collection_id',
        string='Collection',
        store=True,
        readonly=True
    )

    product_type_id = fields.Many2one(
        related='order_line.product_template_id.type_id',
        string='Product Type',
        store=True,
        readonly=True
    )