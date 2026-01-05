from odoo import fields, models, api


class AccountPayment(models.Model):
    _inherit = 'account.payment'

    def action_draft(self):
        """
            Actualizar Fecha de vencimiento parcial de facturas asociadas cuando se pasa a borrador el pago.
        :return:
        """
        invoices = self.reconciled_invoice_ids
        super(AccountPayment, self).action_draft()
        invoices._compute_invoice_date_due_partial()
