#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Litchfield United Church of Christ'
SITENAME = 'LitchfieldUCC'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM         = None
CATEGORY_FEED_ATOM    = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM      = None
AUTHOR_FEED_RSS       = None

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

THEME = '../LitchfieldUCC-BrutalistUCC-PelicanTheme/'
DISPLAY_PAGES_ON_MENU = False
MENUITEMS = (
    ('About Our Church', '/about'),
    ('Calendar', '/calendar'),
)
ARTICLE_URL     = '{category}/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = '{category}/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'
STATIC_PATHS = [
    'pastors-corner/images',
]
PLUGIN_PATHS = [
    f'{THEME}plugins/',
    '../Pelican-Plugins/',
]
PLUGINS = [
    'ical',
    'calendar_event_support'
]