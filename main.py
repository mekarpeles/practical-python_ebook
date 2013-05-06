#-*- coding: utf-8 -*-

"""
    main.py
    ~~~~~~~

    Application for Practical Python Book

    :copyright: (c) 2012 Mek.
    :license: GPLv3 , see LICENSE for more details.
"""

import waltz

urls = ("/", "routes.home.Index",
        "/([Pp]ractical-[Pp]ython)/chapters/([0-9]+)/?", "routes.chapters.Chapter")

env = {}
app = waltz.setup.dancefloor(urls, globals(), env=env)

if __name__ == "__main__":
    app.run()
