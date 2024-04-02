# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Book(models.Model):
    _name = 'library.book'
    name = fields.Char(string="Title", required=True)
    author = fields.Char(string="Author")

    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100
