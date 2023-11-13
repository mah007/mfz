# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from datetime import date, timedelta
from odoo.exceptions import UserError, ValidationError


class Students(models.Model):
    _name = 'student.student'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Students Data'

    name = fields.Char('Student Full Name', compute='_getfullname', translate=True)
    image = fields.Image('Student image', )
    f_name = fields.Char('First Name', required=True, translate=True)
    m_name = fields.Char('Middel Name', translate=True)
    l_name = fields.Char('Last Name', required=True, translate=True)
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], translate=True)
    dob = fields.Date('Date of birth')
    age = fields.Integer('Age', compute='_get_age')
    level = fields.Many2one('student.level', string='Class')
    nationality = fields.Many2one('res.country')
    city = fields.Many2one('res.country.state', )
    state = fields.Selection([('wait', 'Waiting'), ('approved', 'Approved'), ('rejected', 'Rejected')], default='wait',
                             string='Status', translate=True)
    reject_reason = fields.Text('Reject Reason', translate=True)

    def act_approve(self):
        for rec in self:
            rec.state = 'approved'

    def act_reject(self):
        for rec in self:
            rec.state = 'rejected'

    def to_waiting(self):
        for rec in self:
            rec.state = 'wait'

    @api.onchange('nationality')
    def _get_country(self):
        for rec in self:
            if rec.nationality:
                return {'domain': {'city': [('country_id', '=', rec.nationality.id)], }}

    # module functions
    @api.onchange('f_name', 'm_name', 'l_name')
    def _getfullname(self):
        for rec in self:
            name = ''
            if rec.f_name:
                name += rec.f_name
            if rec.m_name:
                name += ' ' + rec.m_name
            if rec.l_name:
                name += ' ' + rec.l_name
            rec.name = name

    @api.onchange('dob')
    def _get_age(self):
        for rec in self:
            age = 0
            if rec.dob:
                age = int(date.today().year - rec.dob.year)
                print('Age', age)
                # if age > 18 or age < 7:
                #     raise ValidationError('Age must be between 7 to 18')
            rec.age = age

    # ORM override

    def unlink(self):

        if self.state != 'wait':
            raise ValidationError('You cant delete this record ')
        else:
            return super(Students, self).unlink()

    @api.model
    def create(self, vals):
        student = super(Students, self).create(vals)
        age = student.age
        print('Age =', age)
        if age:
            if age > 18 or age < 7:
                raise ValidationError('Age must be between 7 to 18')

        print(student)
        return student

    def write(self, vals):
        student = super(Students, self).write(vals)
        for rec in self:
            print(vals)
            if rec.age:
                age = rec.age
                if age >= 18 or age <= 7:
                    print(age)
                    raise ValidationError('Age must be between 7 to 18')
        return student


class RejectReason(models.TransientModel):
    _name = 'student.reason.reject'
    _description = 'Reason of rejection'

    reason = fields.Text('Reason of Rejection')

    def reject_reason_act(self):
        student = self.env['student.student'].browse(self.env.context.get('active_ids'))
        student.reject_reason = self.reason
        student.state = 'rejected'
        student.message_post(body=_(self.reason))
