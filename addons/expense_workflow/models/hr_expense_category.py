from odoo import models, fields

class HrExpenseCategory(models.Model):
    _inherit = 'product.product'

    max_amount_allowed = fields.Float(
        string="Max Allowed Amount",
        help="Maximum amount allowed for this expense category (0 = no limit)"
    )
