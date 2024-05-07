# -*- coding: utf-8 -*-
# from odoo import http


# class Infomusic(http.Controller):
#     @http.route('/infomusic/infomusic', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/infomusic/infomusic/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('infomusic.listing', {
#             'root': '/infomusic/infomusic',
#             'objects': http.request.env['infomusic.infomusic'].search([]),
#         })

#     @http.route('/infomusic/infomusic/objects/<model("infomusic.infomusic"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('infomusic.object', {
#             'object': obj
#         })
