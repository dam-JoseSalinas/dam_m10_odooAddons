from odoo import models, fields, api


class Client(models.Model):
    _name = 'hotel_itic.client'
    name = fields.Char(string="Nom")
    dni = fields.Char(string="DNI")
    birthday = fields.Integer(string="Data de nai")
    room_id = fields.Many2one(comodel_name="hotel_itic.room", string="habitacio de clientes")

    # @api.depends('value')
    # def _value_pc(self):
    #     for record in self:
    #         record.value2 = float(record.value) / 100
