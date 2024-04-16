from odoo import models, fields

class Loan(models.Model):
    _name = "library.loan" 		
    name = fields.Char(string="Loan id", required=True)
    loan_date = fields.Datetime(string="Loan Date", required=True)
    return_date = fields.Datetime(string="Return Date")
    book_id = fields.Many2one(comodel_name="library.book", string="Libro prestado", required=True)
    member_id = fields.Many2one(comodel_name="library.member", string="Usuario prestante", required=True)


    