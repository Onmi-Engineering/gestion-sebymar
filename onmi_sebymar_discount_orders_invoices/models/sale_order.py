from odoo import fields, models, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    total_discount = fields.Float(
        string='Total discount', compute="_compute_total_discount",
        digits='Product Price', readonly=True)
    
   
    def _compute_total_discount(self):
        for rec in self:
            rec.total_discount = 0
            for line in rec.order_line:      
             rec.total_discount +=  line.discount_dif