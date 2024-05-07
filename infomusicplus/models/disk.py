from odoo import models, fields, api

class Disk(models.Model):
    _inherit = "infomusic.disk"
    genre = fields.Selection([('g1', 'rock'), ('g2','pop'), ('g3','pop-rock'), ('g4', 'heavy')], string="Generos", default="g1")
    cover = fields.Image("portada del disco", max_width=150, max_height=150)
    nbr_of_songs = fields.Integer(compute = "count_nbr_of_songs", store=True)
    _sql_constraints = [('check_disk_name_unique', 'UNIQUE(name)' ,'El valor de nombre de disco tiene que ser unico')]
    @api.depends("song_ids")
    def count_nbr_of_songs(self):
        for registro in self:
            registro.nbr_of_songs = len(registro.song_ids)