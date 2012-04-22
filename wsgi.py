import web
from reloader import PeriodicReloader

urls = ("/", "Index",
        "/(.*)-chapter-([0-9]+)/?", "Chapter",
        "/([Pp]ractical-[Pp]ython)/chapters/([0-9]+)/?", "Chapter")

app = web.application(urls, globals())
render = web.template.render('templates/')

class Index:
    def GET(self, book=None):
        return render.template()

class Chapter:
    def GET(self, title, chapter=0):
        return getattr(render.chapters, 'chapter_%s' % chapter, 'chapter_1')()

if __name__ == "__main__":
    PeriodicReloader()
    app.run()
else:
    web.config.debug = False
    application = app.wsgifunc()
