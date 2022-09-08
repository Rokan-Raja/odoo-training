from odoo import models

class ThemeCustom(models.AbstractModel):
    _inherit = 'theme.utils'
    def _theme_custom_post_copy(self, mod):
        print('hello')
        self.disable_view('website.template_header_default')
        self.enable_view('website.template_header_centered_logo')
