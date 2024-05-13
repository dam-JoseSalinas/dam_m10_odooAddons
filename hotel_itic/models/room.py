from odoo import models, fields, api
from odoo.exceptions import ValidationError, UserError

class Room(models.Model):
    _name = 'hotel_itic.room'
    name = fields.Char(string="Numero de habitaciones")
    hasTv = fields.Boolean()
    capacity = fields.Integer()
    clients_ids = fields.One2many(comodel_name="hotel_itic.client", inverse_name="room_id", string="Clients")
    floor = fields.Integer(compute="compute_floor", store=True)
    @api.depends("name")
    def compute_floor(self):
        for registro in self:
            if registro.name:
                registro.floor = int(registro.name[0])

    @api.constrains('clients_ids')
    def _check_cities(self):
        for record in self:
            if len(record.clients_ids) > record.capacity:
                raise ValidationError("Aixo no es possible")
    

    # @api.depends('value')
    # def _value_pc(self):
    #     for record in self:
    #         record.value2 = float(record.value) / 100
