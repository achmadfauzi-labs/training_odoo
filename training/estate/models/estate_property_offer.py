from odoo import fields, models, api
from odoo.tools.populate import compute
from dateutil.relativedelta import relativedelta
from odoo.exceptions import ValidationError


class EstateOffer(models.Model):
    _name = "estate.property.offer"
    _description = "Offer Made"
    _rec_name = "property_id"

    price = fields.Float()
    status = fields.Selection(
        [
            ("accepted","Accepted"),
            ("refused","Refused")
        ], copy = False,
    )

    partner_id = fields.Many2one("res.partner",required=True, string="Partner")
    property_id = fields.Many2one("estate.property",required=True, string="Property")
    property_type_id = fields.Many2one(related="property_id.property_type_id",store= True, string="Property Type")

    validity = fields.Integer('Validity', default=7)
    date_deadline = fields.Date('Deadline', compute="_compute_date_deadline", inverse="_inverse_date_deadline")

    @api.depends("create_date","validity")
    def _compute_date_deadline(self):
        for offer in self:
            date = offer.create_date.date() if offer.create_date else fields.Date.today()
            offer.date_deadline = date + relativedelta(days=offer.validity)

    def _inverse_date_deadline(self):
        for offer in self:
            date = offer.create_date.date() if offer.create_date else fields.Date.today()
            offer.validity = (offer.date_deadline - date).days

    def action_accept(self):
        for rec in self:
            accept_offer = rec.property_id.offer_ids.filtered(lambda r: r.status == 'accepted')
            if not accept_offer:
                rec.property_id.write({
                    'buyer_id': rec.partner_id.id,
                    'selling_price':rec.price,
                })
                rec.status = 'accepted'
            else:
                raise ValidationError("Data sudah ada yang di accept")

    def action_refuse(self):
        for rec in self:
            rec.status = 'refused'