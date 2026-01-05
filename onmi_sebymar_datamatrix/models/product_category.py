from odoo import fields, models, api


class ProductCategory(models.Model):
    _inherit = 'product.category'

    datamatrix = fields.Boolean('In datamatrix')
