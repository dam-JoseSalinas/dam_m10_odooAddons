from odoo import models, fields

class Disk(models.Model):
    _name = "infomusic.disk"
    name = fields.Char(string="TItle", required=True)
    publish_date = fields.Date(string="Publishing date")
    song_ids = fields.One2many(comodel_name="infomusic.song", inverse_name="disk_id", string="canciones del disco")
    singer_ids = fields.Many2many(comodel_name="infomusic.singer", string="cantantes del disco")
