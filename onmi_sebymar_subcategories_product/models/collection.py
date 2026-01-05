from odoo import fields, models, api


class Collection(models.Model):
    _name = 'collection'
    _description = 'Collections'

    name = fields.Char('Name')
    description = fields.Text('Description')

    product_template_ids = fields.One2many('product.template', 'collection_id')

    product_count = fields.Integer('Products', compute='_compute_product_count')

    def _compute_product_count(self):
        for rec in self:
            rec.product_count = self.env['product.template'].search_count([('collection_id', '=', rec.id)])

    def action_products_collection(self):

        action = self.env["ir.actions.actions"]._for_xml_id("stock.product_template_action_product")
        action['domain'] = [('collection_id', 'in', self.ids)]
        action['context'] = {'default_collection_id': self.id}
        action['context'] = {
            'create': 0,
        }
        return action
