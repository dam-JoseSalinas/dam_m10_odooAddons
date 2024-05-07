# -*- coding: utf-8 -*-
# from odoo import http


# class Infomusicplus(http.Controller):
#     @http.route('/infomusicplus/infomusicplus', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/infomusicplus/infomusicplus/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('infomusicplus.listing', {
#             'root': '/infomusicplus/infomusicplus',
#             'objects': http.request.env['infomusicplus.infomusicplus'].search([]),
#         })

#     @http.route('/infomusicplus/infomusicplus/objects/<model("infomusicplus.infomusicplus"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('infomusicplus.object', {
#             'object': obj
#         })
