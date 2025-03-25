# this file is symlinked into site-packages/pywikibot/families


from pywikibot import family

class Family(family.Family):
    name = 'woftnw'
    langs = {
        'en': 'wiki.woftnw.org',
    }
    
    def scriptpath(self, code): 
        return ''

    def protocol(self, code):
        return 'HTTPS'
    def version(self, code):
        return "1.41.1"
     
