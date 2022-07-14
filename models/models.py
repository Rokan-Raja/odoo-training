# -*- coding: utf-8 -*-
import datetime

from odoo import models, fields, api ,_
from odoo.exceptions import AccessError, UserError, ValidationError
class SaleOrder(models.Model):
    _inherit = 'sale.order'
    @api.model
    def action_confirm(self):
        res= super(SaleOrder, self).action_confirm()
        print(res)
        if res:
            return res






