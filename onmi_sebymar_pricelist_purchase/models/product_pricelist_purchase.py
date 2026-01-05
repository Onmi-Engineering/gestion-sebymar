from odoo import fields, models, api


class ProductPricelistPurchase(models.Model):
    _name = 'product.pricelist.purchase'
    _description = 'Product Pricelist Purchase'

    def _default_currency_id(self):
        return self.env.company.currency_id.id

    name = fields.Char(string="Pricelist Name", required=True, translate=True)

    active = fields.Boolean(
        string="Active",
        default=True,
        help="If unchecked, it will allow you to hide the pricelist without removing it.")

    currency_id = fields.Many2one(
        comodel_name='res.currency',
        default=_default_currency_id,
        required=True)

    company_id = fields.Many2one(
        comodel_name='res.company')

    item_ids = fields.One2many(
        comodel_name='product.pricelist.item.purchase',
        inverse_name='pricelist_id',
        string="Pricelist Rules",
        copy=True)

