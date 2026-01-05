from odoo import fields, models, api


class StockReturnPicking(models.TransientModel):
    _inherit = 'stock.return.picking'

    def _create_return(self):
        stock_return = super(StockReturnPicking, self)._create_return()
        stock_return.generate_datamatrix_lines()

        return stock_return
