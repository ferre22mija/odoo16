from odoo import fields,models

class CustomProperty(models.Model):
    _name="custom.property"
    _description="propiedades del cliente"
    name = fields.Char(required=True)
    description = fields.Text()
    postcode = fields.Char()
    date_availability = fields.Date()
    excepted_price = fields.Float(required=True)
    selling_price = fields.Float()
    bedrooms = fields.Integer()
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection(
        string='Type',
        selection=[('north','north'),('south','south'),('east','east'),('west','west')],
        help='four sections of the planet'
    )
