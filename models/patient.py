# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Hospital patients'

    # Now we add the fields
    reference = fields.Char(string='Patient Reference', required=True, copy=False, readonly=True, default=lambda self: _('New'))
    name = fields.Char(string='First Name', required=True, tracking=True)
    last_name = fields.Char(string='Last Name', required=False)
    age = fields.Integer(string='Age', required=True, tracking=True)
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female')
    ], required=True, default='male')
    notes = fields.Text(string='Notes')
    state = fields.Selection([('draft', 'Draft'), ('confirm', 'Confirmed'), ('done', 'Done'), ('cancel', 'Canceled')],
                             default='draft', string='Status', tracking=True)

    # It's best practise to end the Many2one field name with _id
    # comodel_name = 'res.partner'
    responsible_id = fields.Many2one('res.partner', string='Responsible')

    def action_confirm(self):
        print('Confirm Button Clicked!')
        self.state = 'confirm'

    def action_done(self):
        print('Done Button Clicked!')
        self.state = 'done'

    def action_draft(self):
        print('Draft Button Clicked!')
        self.state = 'draft'

    def action_cancel(self):
        print('Cancel Button Clicked!')
        self.state = 'cancel'

    def action_name(self):
        self.name = 'Master'

    @api.model
    def create(self, vals):
        # print('Successfully overwritten Create method!')
        if not vals.get('notes'):
            vals['notes'] = 'New patient!'

        if vals.get('reference', _('New')) == _('New'):
            vals['reference'] = self.env['ir.sequence'].next_by_code('hospital.patient') or _('New')

        if vals.get('age') <= 0:
            raise ValueError("Invalid Age!")

        res = super(HospitalPatient, self).create(vals)
        return res
