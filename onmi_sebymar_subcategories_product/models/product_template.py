from odoo import fields, models, api


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    retail = fields.Boolean('Retail')
    cabin = fields.Boolean('Cabin')
    collection_id = fields.Many2one('collection')
    type_id = fields.Many2one('product.template.type')
