# -*- coding: utf-8 -*-
{
    'name': "associazione",
    'summary': """Associazione""",
    'description': """Descrizione App Associazione""",
    'author': "Web2e",
    'website': "https://www.web2e.it",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': [
        'base',
        'sale',
        'mail',
        'hr'
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/ruoli_view.xml',
        'views/ruoli_specifici_view.xml',
        'views/anagrafiche_view.xml',
        'views/iscrizioni_view.xml',
        'views/tag_view.xml',
        'views/gruppi_view.xml',
        'views/tipo_documenti_view.xml',
        'views/website_form.xml',        
    ],
    'license': 'LGPL-3'
}
