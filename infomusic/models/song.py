from odoo import models, fields

class Song(models.Model):
    _name = "infomusic.song"
    name = fields.Char(string="Title", required=True)
    order = fields.Integer(string="Order")
    duration = fields.Integer(string="Duration")
    disk_id = fields.Many2one(comodel_name="infomusic.disk", string="Disco de la cancion")