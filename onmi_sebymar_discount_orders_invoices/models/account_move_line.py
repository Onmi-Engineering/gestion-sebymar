from odoo import fields, models, api


class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    discount_dif = fields.Float(
        string='Total discount', compute="_compute_total_discount",
        digits='Product Price', readonly=True)


    def _compute_total_discount(self):
       for rec in self:
                rec.discount_dif = 0
                rec.discount_dif  = (rec.quantity * rec.price_unit) - rec.price_subtotal 