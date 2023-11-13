# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    vendor_vat = fields.Char('Vendor VAT')




