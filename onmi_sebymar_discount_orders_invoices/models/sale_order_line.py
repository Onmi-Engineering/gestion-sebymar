from odoo import fields, models, api


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    discount_dif = fields.Float(
        string='Total discount', compute="_compute_total_discount",
        digits='Product Price', readonly=True)


    def _compute_total_discount(self):
       for rec in self:
                rec.discount_dif = 0
                rec.discount_dif  = (rec.product_uom_qty * rec.price_unit) - rec.price_subtotal 