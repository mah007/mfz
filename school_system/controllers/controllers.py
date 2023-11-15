# -*- coding: utf-8 -*-
import json

from odoo import http
from odoo.http import request


class SchoolSystem(http.Controller):
    @http.route('/school/start', auth='public', website=True)
    def index(self, **kw):
        students = request.env['student.student'].sudo().search([('name', '!=', False)])
        vals = {
            'students': students
        }

        return request.render('school_system.school_system_home', vals)

    @http.route('/school/profile/<int:student_id>', auth='public', website=True)
    def profile(self, student_id=False, **kw):
        students = request.env['student.student'].sudo().search([('id', '=', student_id)])
        vals = {
            'students': students
        }

        return request.render('school_system.school_system_profile', vals)

    @http.route('/school/create/', auth='public',csrf=False,method=['post'])
    def insert(self, **kw):
        data = request.httprequest.data

        student = request.env['student.student'].sudo()
        print(data)
        datajson = json.loads(data)

        student.sudo().create(datajson)
        return

