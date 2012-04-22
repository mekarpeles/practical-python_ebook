import web
from reloader import PeriodicReloader

urls = ("/", "Index",
        "/([Pp]ractical-[Pp]ython)/?", "Ebook")

app = web.application(urls, globals())
render = web.template.render('templates/')

class Index:
    def GET(self, book=None):
        return render.template()

class Ebook:
    def GET(self, title):
        book = getattr(self, 'title', 'default').lower()
                   

if __name__ == "__main__":
    PeriodicReloader()
    app.run()
else:
    web.config.debug = False
    application = app.wsgifunc()
