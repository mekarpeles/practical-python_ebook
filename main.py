import web
from reloader import PeriodicReloader

urls = ("/", "Index",
        "/(.*)-chapter-([0-9]+)/?", "Chapter",
        "/([Pp]ractical-[Pp]ython)/chapters/([0-9]+)/?", "Chapter")

app = web.application(urls, globals())
slender = web.template.render('templates/', globals={})
render = web.template.render('templates/', base="book")

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
        return slender.template(**kwargs)

class Chapter:
    def GET(self, title, chapter=0):
        try:
            return getattr(render.chapters, 'chapter_%s' % chapter, 'chapter_1')()
        except:
            return "coming soon"

if __name__ == "__main__":
    PeriodicReloader()
    app.run()
else:
    web.config.debug = False
    application = app.wsgifunc()
