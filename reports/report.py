# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime


class SaleOrder(models.Model):

    _inherit = 'sale.order'

    def get_data(self, name):
        count = 0
        res = self.env['mrp.production'].search([('origin', '=', name)])
        for data in res:
            if data.state == 'done':
                count = count + 1
        print('total -', count)
        val = [{
            'count': len(res),
            'total': count
        }]
        print(val)
        return val

    def date_time(self):
        now = datetime.now()
        date = now.strftime("%d/%m/%Y %H:%M:%S")
        print(date)
        return date



