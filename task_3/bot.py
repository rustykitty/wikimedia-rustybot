import re

import pywikibot

from os.path import exists

site = pywikibot.Site('en', 'wikipedia')

list_page = pywikibot.Page(site, 'User:Alex 21/sandbox/No episode table')

for page in list_page.linkedPages(namespaces=[0], follow_redirects=True, content=True, total=None):

    m: re.Match = None # for type hinting purposes only

    # MOS:SECTIONORDER

    # Group in multiple issues template
    if (m := re.search(r'\{\{multiple issues\|\n', page.text, re.I)):
        pos = m.end()
    # After hatnote
    elif (m := re.search(r'\{\{(?:For(?:-text|-multi)?|Other uses(?: of)?|About(?:-distinguish(?:-text))?|Redirect(?:2|-multi|-several)|Distinguish)\|.*?\}\}', 
                       page.text, re.I)):
        pos = m.end() + 1
    # After DISPLAYTITLE, if present
    elif (m := re.search(r'\{\{(?:DISPLAYTITLE:.*?|Lowercase title|Italic title)\}\}', page.text, re.I)):
        pos = m.end()
    # Before English variety / date format, if present
    elif (m := re.search(r'\{\{use (?:[dmy]{3} dates|[A-Z][a-z]+ English).*?\}\}', page.text, re.I)):
        pos = m.start()
    # After short description, if present
    elif (m := re.search(r'\{\{short description\|.*?\}\}', page.text, re.I)):
        pos = m.end() + 1
    else:
        pos = 0

    pos = min(max(pos, 0), len(page.text)) # clamp position

    page.text = page.text[:pos] + '{{Convert to Episode table}}\n' + page.text[pos:]

    page.save(summary='Tagging page with {{[[Template:Convert to Episode table|Convert to Episode table]]}} (Task 3)')
