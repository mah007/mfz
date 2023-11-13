# -*- coding: utf-8 -*-
# from odoo import http


# class Mfz1(http.Controller):
#     @http.route('/mfz1/mfz1', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/mfz1/mfz1/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('mfz1.listing', {
#             'root': '/mfz1/mfz1',
#             'objects': http.request.env['mfz1.mfz1'].search([]),
#         })

#     @http.route('/mfz1/mfz1/objects/<model("mfz1.mfz1"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('mfz1.object', {
#             'object': obj
#         })
