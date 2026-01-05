from odoo import fields, models, api


class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'

    def _apply_value_from_seller(self, seller):
        # TODO: Este método no existe en la clase padre. Revisar como está hecho lo de las product.pricelist.purchase...
        # if self.order_id.pricelist_id:
        #     seller = False
        # super(PurchaseOrderLine, self)._apply_value_from_seller(seller)
        pass
