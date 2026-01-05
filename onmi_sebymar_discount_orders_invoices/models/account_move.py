from odoo import fields, models, api


class AccountMove(models.Model):
    _inherit = 'account.move'

    total_discount = fields.Float(
        string='Total discount', compute="_compute_total_discount",
        digits='Product Price', readonly=True)


    def _compute_total_discount(self):
        for rec in self:
            rec.total_discount = 0
            for line in rec.invoice_line_ids:
             rec.total_discount +=  line.discount_dif