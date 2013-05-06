#-*- coding: utf-8 -*-

"""
    routes.chapters
    ~~~~~~~~~~~~~~~

    Route handling for the contents of the book

    :copyright: (c) 2012 Mek.
    :license: Creative Commons, see LICENSE for more details.
"""

import waltz
from waltz import track, render, slender

class Chapter:
    def GET(self, title, chapter=0):
        try:
            return getattr(render().chapters, 'chapter_%s' % chapter,
                           'chapter_1')()
        except:
            return "coming soon"
