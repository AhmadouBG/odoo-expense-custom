from odoo import models, fields, api
from odoo.exceptions import ValidationError

class HrExpense(models.Model):
    _inherit = 'hr.expense'

    @api.constrains('total_amount', 'product_id')
    def _check_expense_limit(self):
        for expense in self:
            if expense.product_id and expense.product_id.max_amount_allowed > 0:
                if expense.total_amount > expense.product_id.max_amount_allowed:
                    raise ValidationError(
                        f"The amount ({expense.total_amount:.2f}) exceeds the authorized limit "
                        f"for the category {expense.product_id.name} "
                        f"({expense.product_id.max_amount_allowed:.2f})."
                    )
