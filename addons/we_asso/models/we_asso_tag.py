from odoo import models, fields, api

class AssoTag(models.Model):
    _name = 'asso.tag'
    _description = 'asso.tag'

    name = fields.Char("Tag", required=True)
    description = fields.Text()

