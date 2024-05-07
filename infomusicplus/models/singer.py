from odoo import models, fields, api
import datetime
class Singer(models.Model):
    #_name = "infomusic.singer"
    _inherit = "infomusic.singer"
    country_of_birth = fields.Many2one(comodel_name="res.country", string="pais de nacimiento")
    photo = fields.Image("foto del cantante", max_width=150, max_height=150)
    tour_ids = fields.One2many(comodel_name="infomusicplus.tour", inverse_name="singer_id", string="tours del cantant")
    age = fields.Integer(compute="_compute_date_diff")
    _sql_constraints = [('check_singer_name_unique', 'UNIQUE(name)' ,'El valor de nombre de cantante tiene que ser unico')]

    @api.depends("birthday")
    def _compute_date_diff(self):
        end_date = datetime.datetime.now()
        end_year = end_date.strftime("%Y")
        end_month = end_date.strftime("%m")
        for registro in self:
            if registro.birthday:
                start_date = fields.Datetime.from_string(registro.birthday)
                start_year = start_date.strftime("%Y")
                start_month = start_date.strftime("%m")
                age = int(end_year) - int(start_year)
                if end_month < start_month:
                    age -= 1
                registro.age = age
            else:
                registro.age = 0