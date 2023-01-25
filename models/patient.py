# -*- coding: utf-8 -*-
from odoo import fields, models


class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Information about the patients'

    # Now we add the fields
    name = fields.Char(string='First Name', required=True)
    last_name = fields.Char(string='Last Name', required=False)
    age = fields.Integer(string='Age', required=True)
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female')
    ], required=True, default='male')
    notes = fields.Text(string='Notes')
