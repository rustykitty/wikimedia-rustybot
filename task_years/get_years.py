import pywikibot

import time

from pywikibot import pagegenerators

site = pywikibot.Site()

fs = open('page_titles.txt', 'w')
# for page in pagegenerators._filters.RegexFilterPageGenerator(
#                 pagegenerators.AllpagesPageGenerator(start="1 BC", 
#                  includeredirects=False, 
#                  content=True),
#                 r'^\d BC+$'):
for i in range(2000):
    page = pywikibot.Page(site, f'AD {i}')
    if (not page.exists()) or page.isRedirectPage(): 
        print(page.title(), 'skipped')
        time.sleep(0.5)
        continue
    print('writing', page.title())
    fs.write(page.title() + '\n')
    fs.flush()
    time.sleep(1)