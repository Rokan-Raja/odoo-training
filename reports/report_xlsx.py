from odoo import models
from datetime import datetime

class PartnerXlsx(models.AbstractModel):

    _name = 'report.report.sale_order_excel'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, partners):
        sheet = workbook.add_worksheet('Manufacture Order')
        merge_format = workbook.add_format({'bold': True, 'align': 'center', 'border': 1})
        merge_format2 = workbook.add_format({'bold': True, 'align': 'left', 'border': 1})
        sheet.write('D2', partners.partner_id.name, merge_format2)
        sheet.write('D3', partners.partner_id.street2, merge_format2)
        sheet.write('D4', partners.partner_id.city, merge_format2)
        sheet.write('D5', partners.partner_id.zip, merge_format2)
        sheet.merge_range('D7:F7','Order Priority Report', merge_format)
        sheet.set_column('D:E', 25)
        sheet.set_column('E:F', 32)
        now = datetime.now()
        d = now.strftime("%d/%m/%Y %H:%M:%S")
        date = 'Date :'+d
        sheet.merge_range('D9:E9', date , merge_format2)
        sheet.write(13, 3, 'Order', merge_format)
        sheet.write(13, 4, 'Order Reference', merge_format)
        sheet.write(13, 5, 'Manufacture Order', merge_format)
        row = 14
        for obj in partners:
            count = 0
            res = self.env['mrp.production'].search([('origin', '=', obj.name)])
            for data in res:
                if data.state == 'done':
                    count = count + 1
            total = len(res)
            if total != 0:
                col = 3
                sheet.write(row, col, obj.name, merge_format)
                col = 4
                sheet.write(row, col, obj.client_order_ref, merge_format)
                col = 5
                ans = "completed({}/{})".format(count, total)
                sheet.write(row, col, ans, merge_format)
                row += 1


