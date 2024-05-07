from odoo import models, fields, api

class Tour_city(models.Model):
    _name = "infomusicplus.tour_city"
    name = fields.Char(required=True)
    country_id = fields.Many2one(comodel_name="res.country", string="Country", required=True)
    date = fields.Date(name="Date")
    tour_id = fields.Many2one(comodel_name="infomusicplus.tour", string="tour de la ciutat")
    confirmed = fields.Boolean(compute="if_date_exists")

    @api.depends("date")
    def if_date_exists(self):
        for registro in self:
            if registro.date:
                registro.confirmed = True
            else:
                registro.confirmed = False