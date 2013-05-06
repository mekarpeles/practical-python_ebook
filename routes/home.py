#-*- coding: utf-8 -*-

"""
    routes.home
    ~~~~~~~~~~~

    Routes related to the homepage.

    :copyright: (c) 2012 Mek.
    :license: Creative Commons , see LICENSE for more details.
"""

import waltz
from waltz import track, slender

class Index:
    def GET(self, book=None):
        """
        kwargs should be moved to books.cfg or there should be a
        book_<title>.cfg per book or [title] within books.cfg
        """
        kwargs = {"title": "Practical Python",
                  "subtitle": "A Guide to Better Python",
                  "version": "v.0.0.1",
                  "description": "By Mek; Hyperink 2012, ISBN 9781614642411. Practical Python is the fastest way to learn python tricks.",
                  "keywords": "Python,Practical Python,programming,hacks,learning",
                  }                  
        return slender().index(**kwargs)
