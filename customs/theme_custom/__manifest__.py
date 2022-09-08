{
    # Theme information
    'name': "Custom Theme",
    'description': """
    """,
    'category': 'Theme',
    'version': '1.0',
    'depends': ['website'],

    # templates
    'data': [
        'views/header.xml',
        'views/footer.xml',
        'views/assert.xml',
        'views/about_us.xml',
        'views/product.xml',
        'views/facilities.xml',
        'views/snippets.xml',
        'views/snippets/about_banner.xml',
        'views/snippets/about_background.xml',
        'views/snippets/newsletter.xml',
        'views/snippets/hr_lines.xml',
        'views/snippets/heading_center.xml',
    ],

    # demo pages
    'demo': [
        # 'demo/pages.xml',
    ],

    # Your information
    'author': "My Company",
    'website': "",
    'application': True,
    'auto-install': True,
}
