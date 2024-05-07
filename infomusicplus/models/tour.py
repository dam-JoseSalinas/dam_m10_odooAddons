from odoo import models, fields, api
from odoo.exceptions import ValidationError, UserError

class Tour(models.Model):
    _name = "infomusicplus.tour"
    name = fields.Char(string="Title", required=True)
    singer_id = fields.Many2one(comodel_name="infomusic.singer", string="Cantant del tour")
    tour_city_ids = fields.One2many(comodel_name="infomusicplus.tour_city", inverse_name="tour_id", string="ciutats del tour")
    _sql_constraints = [('check_tour_name_unique', 'UNIQUE(name)' ,'El valor de nombre del tour tiene que ser unico')]
    state = fields.Selection([('s1', 'New'), ('s2','Confirmed'), ('s3','Done'), ('s4', 'Cancelled')], string="Estado de gira", default="s1")
    
    @api.constrains('tour_city_ids')
    def _check_cities(self):
        for record in self:
            if len(record.tour_city_ids) > 4:
                raise ValidationError("No se puede añadir mas de 4 ciudades")
    
    @api.onchange("tour_city_ids")
    def on_change_tour_city_ids(self):
        state = self.state
        for tour_city in self.tour_city_ids:
            if tour_city.confirmed == False:
                state = 's1'
                break
            elif tour_city.confirmed == True:
                state = 's2'
        self.state = state
    
    def onclick_done(self):
        for record in self:
            if record.state == 's3':
                raise UserError("ya esta done")
            else:
                record.state = 's3'
        return True

    def onclick_cancel(self):
        for record in self:
            if record.state == 's4':
                raise UserError("ya esta cancelled")
            else:
                record.state = 's4'

    #@api.model()
    def unlink(self):
        if self.state == 's1' or self.state ==  's2':
            raise ValidationError("No se puede borrar un tour con ciudades pendientes")
        return super(Tour, self).unlink()
