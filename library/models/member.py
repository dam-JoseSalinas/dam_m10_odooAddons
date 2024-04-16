from odoo import models, fields

class Member(models.Model):
    _name = "library.member"
    name = fields.Char(string="Member", required=True)
    email = fields.Char(string="Email")
    loan_ids = fields.One2many(comodel_name="library.loan", inverse_name="member_id", string="Loans")
