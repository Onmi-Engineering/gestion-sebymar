# -*- coding: utf-8 -*-
from collections import defaultdict

from odoo import models, fields, api, _
from odoo.exceptions import UserError
from odoo.tools import frozendict


class AccountPaymentRegister(models.TransientModel):
    _inherit = 'account.payment.register'

    generate_one_payment = fields.Boolean('Generate only one payment', default=False)

    # Funcion original de Rodrigo no borrar
    # TODO: _get_batches no existe. No se está llamando al método padre. Revisar.
    # def _create_payments(self):
    #     self.ensure_one()
    #     batches = self._get_batches()
    #     '''
    #         MOD only 1 line of batch for account.move
    #     '''
    #     if self.generate_one_payment:
    #         for batch in batches:
    #             lines_selected = self.env['account.move.line']
    #             moves = batch['lines'].move_id
    #             for move in moves:
    #                 percent_paid = (move.amount_total - move.amount_residual) / move.amount_total
    #                 total_payments = len(move.invoice_payment_term_id.line_ids)
    #                 payments_reconciled = round(total_payments * percent_paid)
    #                 lines_sorted = sorted(move.invoice_payment_term_id.line_ids, key=lambda ln: ln.months)
    #                 line = lines_sorted[payments_reconciled]
    #                 amount_payment = 0
    #                 if line:
    #                     if line.value == 'balance':
    #                         amount_payment += move.amount_residual
    #                     if line.value == 'percent':
    #                         amount_payment += round(move.amount_total * (line.value_amount / 100), 2)
    #                 if amount_payment == 0:
    #                     lines_move = batch['lines'].filtered(
    #                         lambda ln: ln.move_id.id == move.id)
    #                 else:
    #                     lines_move = batch['lines'].filtered(
    #                         lambda ln: ln.move_id.id == move.id and ln.balance == amount_payment)
    #                     if not lines_move:
    #                         amount_payment += 0.01
    #                         lines_move = batch['lines'].filtered(
    #                             lambda ln: ln.move_id.id == move.id and ln.balance == amount_payment)
    #                         if not lines_move:
    #                             lines_move = batch['lines'].filtered(
    #                                 lambda ln: ln.move_id.id == move.id)
    #                 lines_selected += lines_move[-1]
    #             batch['lines'] = lines_selected
    #     ''' end MOD'''
    #     first_batch_result = batches[0]
    #     edit_mode = self.can_edit_wizard and (len(first_batch_result['lines']) == 1 or self.group_payment)
    #     to_process = []
    #     if edit_mode:
    #         payment_vals = self._create_payment_vals_from_wizard(first_batch_result)
    #         to_process.append({
    #             'create_vals': payment_vals,
    #             'to_reconcile': first_batch_result['lines'],
    #             'batch': first_batch_result,
    #         })
    #     else:
    #         # Don't group payments: Create one batch per move.
    #         if not self.group_payment:
    #             new_batches = []
    #             for batch_result in batches:
    #                 for line in batch_result['lines']:
    #                     new_batches.append({
    #                         **batch_result,
    #                         'payment_values': {
    #                             **batch_result['payment_values'],
    #                             'payment_type': 'inbound' if line.balance > 0 else 'outbound'
    #                         },
    #                         'lines': line,
    #                     })
    #             batches = new_batches
    #
    #         for batch_result in batches:
    #             to_process.append({
    #                 'create_vals': self._create_payment_vals_from_batch(batch_result),
    #                 'to_reconcile': batch_result['lines'],
    #                 'batch': batch_result,
    #             })
    #
    #     payments = self._init_payments(to_process, edit_mode=edit_mode)
    #     ''' MOD '''
    #     if self.generate_one_payment:
    #         for payment in payments:
    #             moves = self.env['account.move'].search([('payment_reference', 'in', payment.ref.split())])
    #             if moves:
    #                 '''
    #                     Cálculo de importe de pago:
    #
    #                     - Si importe adeudado es 0:
    #                         - El pago que hay que realizar será: Total Factura * línea_con_mes_0.value_amount/100
    #
    #                     - Si importe adeudado > 0:
    #                         (Total Factura - Importe adeudado) / Total Factura -> porcentaje de importe por pagar.
    #                         nº pagos pendientes <- Por pagar / Pagado.
    #                         Coger la línea que tenga de mes -> Total líneas - nº pagos pendientes
    #                         Si Tipo deuda de la línea es "Porciento":
    #                             (Valor/100)*Total Factura -> Importe de Pago.
    #                         Si tipo deuda de la línea es "Saldo":
    #                             Importe Adeudado -> Importe de Pago.
    #                 '''
    #                 # TODO: Todo esto está mal. Revisar.
    #                 if len(moves.invoice_payment_term_id.line_ids) > 1:
    #                     amount_payment = 0.0
    #                     for move in moves:
    #                         if move.amount_residual == 0:
    #                             lines = move.invoice_payment_term_id.line_ids.filtered(lambda ln: ln.months == 0)
    #                             for ln in lines:
    #                                 amount_payment += move.amount_total * (ln.value_amount / 100)
    #                         else:
    #                             percent_paid = (move.amount_total - move.amount_residual) / move.amount_total
    #                             total_payments = len(move.invoice_payment_term_id.line_ids)
    #                             payments_reconciled = round(total_payments * percent_paid)
    #                             lines_sorted = sorted(move.invoice_payment_term_id.line_ids, key=lambda ln: ln.months)
    #                             if len(lines_sorted) < payments_reconciled:
    #                                 lines = lines_sorted[payments_reconciled]
    #                             else:
    #                                 lines = lines_sorted[payments_reconciled - 1]
    #                         if lines:
    #                             if lines.value == 'balance':
    #                                 amount_payment += move.amount_residual
    #                             if lines.value == 'percent':
    #                                 amount_payment += move.amount_total * (lines.value_amount / 100)
    #         if amount_payment > 0:
    #             payment.amount = amount_payment
    #     ''' end MOD '''
    #     self._post_payments(to_process, edit_mode=edit_mode)
    #     self._reconcile_payments(to_process, edit_mode=edit_mode)
    #     return payments


    def action_create_payments(self):
        res = super(AccountPaymentRegister, self).action_create_payments()
        accounts_move = self.env['account.move'].search([('id', 'in', self.line_ids.move_id.ids)])
        for am in accounts_move:
            am._compute_invoice_date_due_partial()
        return res

