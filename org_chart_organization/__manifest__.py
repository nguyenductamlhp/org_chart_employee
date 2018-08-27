# -*- coding: utf-8 -*-
{
	'name': "Org Chart Organization",
	'summary': """Dynamic display of your Department Organization""",
	'description': """Dynamic display of your Department Organization""",
	'author': "SLife Organization, Odoo Community Association (OCA)",
	'category': 'Human Resources',
	'version': '2.0',
	'license': 'AGPL-3',
	'depends': ['hr'],
	'data': ['views/org_chart_views.xml'],
	'images': [
		'static/src/img/main_screenshot.png'
	],
	'qweb': [
        "static/src/xml/org_chart_department.xml",
    ],
	'installable': True,
	'application': True,
	'auto_install': False,
}
