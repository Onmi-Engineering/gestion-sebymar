from odoo import fields, models, api


class AccountMove(models.Model):
    _inherit = 'account.move'

    total_margin = fields.Monetary("Total Margin", compute='_compute_total_margin')
    show_margin = fields.Boolean(
        "Show margin", default=False
    )

    @api.depends('invoice_line_ids', 'invoice_line_ids.margin')
    def _compute_total_margin(self):
        for rec in self:
            rec.total_margin = sum(rec.invoice_line_ids.mapped('margin'))
