# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import date, timedelta


class StudentsLevels(models.Model):
    _name = 'student.level'
    _description = 'Student Levels'

    name = fields.Char('Class')
    students = fields.One2many('student.student','level',string='Students')
