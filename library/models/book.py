from odoo import models, fields

class Book(models.Model):
    _name = "library.book" 		
    name = fields.Char(string="Title", required=True)
    author = fields.Char(string="Author", required=True)
    editorial = fields.Char(string="Editorial")
    isbn = fields.Char(string="ISBN", size=13)
    year = fields.Integer(string="Year")
    category = fields.Selection([('categoria1', 'Classics'), ('categoria2','Crime'), ('categoria3','Fantasy')], string="Categorias")
    pages = fields.Integer(string="Pages")
    loan_ids = fields.One2many(comodel_name="library.loan", inverse_name="book_id", string="Book's loan", required=True)