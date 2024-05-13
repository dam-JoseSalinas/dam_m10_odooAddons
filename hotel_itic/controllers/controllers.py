# -*- coding: utf-8 -*-
# from odoo import http


# class Hotel-itic(http.Controller):
#     @http.route('/hotel-itic/hotel-itic', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hotel-itic/hotel-itic/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('hotel-itic.listing', {
#             'root': '/hotel-itic/hotel-itic',
#             'objects': http.request.env['hotel-itic.hotel-itic'].search([]),
#         })

#     @http.route('/hotel-itic/hotel-itic/objects/<model("hotel-itic.hotel-itic"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hotel-itic.object', {
#             'object': obj
#         })
