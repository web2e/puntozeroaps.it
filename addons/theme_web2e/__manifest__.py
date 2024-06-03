# -*- encoding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Web2e Theme',
    'description': 'Web2e website theme',
    'category': 'Theme',
    'version': '1.0',
    'depends': ['website'],
    'data': [
        'views/header.xml',
        'views/footer.xml',
        'views/menus.xml',
        'views/snippets/we_carousel.xml',
        'views/snippets/we_about.xml',
        'views/snippets/we_about_intro.xml',
        'views/snippets/we_timeline.xml',
        'views/snippets/we_3col_round.xml',
        'views/snippets/we_3col_round_wh.xml',
        'views/snippets/we_card_header.xml',
        'views/snippets/we_heading.xml',
        'views/snippets/we_3col_round_header.xml',
        'views/snippets/we_cta_1.xml',
        'views/snippets/we_cta_2.xml',
        'views/snippets/we_event.xml',
        'views/snippets/we_text_image.xml',
        'views/snippets/we_image_text.xml',
        'views/snippets/we_features.xml',
        'views/snippets/we_blockquote.xml',
         'views/snippets/we_text_block.xml',
        'views/snippets/we_cover.xml',
        'views/snippets/we_presentation.xml',
        'views/snippets/we_mega_menu_card_little_icon.xml',
        'views/snippets/we_partner_scroll.xml',
        'views/snippets/snippets.xml',
    ],
    'images': [],
    'snippet_lists': {},
    'assets': {
        'web.assets_frontend': [
            'theme_web2e/static/src/scss/style.scss',
        ],
        'web._assets_primary_variables': [
            "theme_web2e/static/src/scss/primary_variables.scss",
        ]
    },
    'application':False,
    'auto_install':False,
    'license': 'LGPL-3',
}
