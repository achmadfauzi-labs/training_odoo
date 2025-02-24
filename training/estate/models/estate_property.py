from dataclasses import fields
from tokenize import String

from odoo import models, fields, api, _
from datetime import date

from odoo.exceptions import ValidationError
from odoo.tools.populate import compute


class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "model estate property"
    _sql_constraints = [
        ("check_price", "CHECK(selling_price < 0)", "Price should be positive.")
    ]

    active = fields.Boolean(default=True, invisible=True)
    name = fields.Char(string="Title", required=True)
    state = fields.Selection(
        [
            ("new", "New"),
            ("received", "Offer Received"),
            ("accepted", "Offer Accepted"),
            ("sold", "Sold"),
            ("canceled", "Canceled")
        ],
        required=True,
        copy=False,
        default="new"
    )

    description = fields.Text()

    def _default_date(self):
        return fields.Date.today()

    postcode = fields.Char(string="Postcode")
    date_availability = fields.Date(default=_default_date, string="Date Availability")
    expected_price = fields.Float(required=True, string="Expected Price")
    selling_price = fields.Float(string="Selling Price")
    bedrooms = fields.Integer()
    living_area = fields.Integer(string="Living Area")
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer(string="Garden Area")
    total_area = fields.Integer(compute= "_compute_total")
    garden_orientation = (
        fields.Selection([('north', 'North'), ('south', 'South'), ('east', 'East'), ('west', 'West')]))

    property_type_id = fields.Many2one("estate.property.type", string="Property Type")
    buyer_id = fields.Many2one("res.partner", string="Buyer")
    sales_person_id = fields.Many2one("res.users", string="Sales Person")
    offer_ids = fields.One2many("estate.property.offer", "property_id")
    tag_ids = fields.Many2many("estate.property.tag")

    @api.depends("living_area", "garden_area")
    def _compute_total(self):
        for rec in self:
            rec.total_area= rec.living_area+rec.garden_area

    def action_sold(self):
        for rec in self:
            if rec.state != 'canceled':
                rec.state = 'sold'
            else:
                raise ValidationError("Salah Sold")

    def action_cancel(self):
        for rec in self:
            if rec.state != 'sold':
                rec.state = 'canceled'
            else:
                raise ValidationError("Salah canceled")

    @api.onchange("garden")
    def _onchange_gardern(self):
        if self.garden == False:
            self.garden_area = 0
            self.garden_orientation = False

    @api.onchange("date_availability")
    def _onchange_date_availability(self):
        if self.date_availability < self._default_date():
            return {"warning": {"title": _("Warning"), "message": _("Tanggal lu udah kelewatan")}}

    @api.constrains("expected_price")
    def _check_expected_price(self):
        for cek in self:
            if cek.expected_price < 1:
                raise ValidationError("Expected Price tidak boleh kurang dari 0")

    @api.constrains("selling_price")
    def _check_selling_price(self):
         if self.selling_price < 1:
           raise ValidationError("Selling Price tidak boleh kurang dari 0")