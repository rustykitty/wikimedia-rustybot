# this file is symlinked into site-packages/pywikibot/families

from pywikibot import family

class Family(family.Family):
    name = 'wingsoffire'
    langs = {
        'en': 'wingsoffire.wiki',
    }
    
    def scriptpath(self, code): 
        return ''
    def protocol(self, code):
        return 'HTTPS'
    def version(self, code):
        return "1.42.3"

