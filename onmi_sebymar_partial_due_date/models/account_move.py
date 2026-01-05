from odoo import fields, models, api, _
from dateutil.relativedelta import relativedelta


class AccountMove(models.Model):
    _inherit = 'account.move'

    invoice_date_due_partial = fields.Date(
        string='Partial Due Date', compute='_compute_invoice_date_due_partial', store=True,
        help=_('Date due of next payment to do.'))

    def _compute_invoice_date_due_partial(self):
        for rec in self:
            line = False
            rec.invoice_date_due_partial = rec.invoice_date
            if rec.invoice_payment_term_id:
                if rec.payment_state == 'not_paid':
                    if rec.amount_residual == rec.amount_total:
                        line = rec.invoice_payment_term_id.line_ids.sorted(lambda g: g.months)[0]
                if rec.payment_state == 'partial':
                    percent_paid = (rec.amount_total - rec.amount_residual) / rec.amount_total
                    total_payments = len(rec.invoice_payment_term_id.line_ids)
                    payments_reconciled = round(total_payments*percent_paid)
                    lines_sorted = sorted(rec.invoice_payment_term_id.line_ids, key=lambda ln: ln.months)
                    if payments_reconciled < total_payments:
                        line = lines_sorted[payments_reconciled]
                if rec.payment_state in ('in_payment', 'paid'):
                    line = rec.invoice_payment_term_id.line_ids.sorted(lambda g: g.months)[-1]
                if line:
                    date = rec.invoice_date
                    if line.months >= 0:
                        if line.end_month:
                            prev_date = date
                            date = rec.invoice_date + relativedelta(months=line.months + 1)

                        else:
                            date = rec.invoice_date + relativedelta(months=line.months)
                    if line.days_after and line.end_month:
                        date = date.replace(day=line.days_after)
                    elif line.days:
                        date = date + relativedelta(days=line.days)
                    rec.invoice_date_due_partial = date

    def update_partial_due_date(self):
        for rec in self:
            rec._compute_invoice_date_due_partial()
