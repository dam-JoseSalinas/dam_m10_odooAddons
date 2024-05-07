from odoo import models, fields

class Singer(models.Model):
    _name = "infomusic.singer"
    name = fields.Char(string="Name", required=True)
    birthday = fields.Date(string="Date of birth")
    disk_ids = fields.Many2many(comodel_name="infomusic.disk", string="discos del cantante")