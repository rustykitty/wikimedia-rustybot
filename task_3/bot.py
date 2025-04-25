import re

import pywikibot

site = pywikibot.Site('en', 'wikipedia')

list_page = pywikibot.Page(site, 'User:Alex 21/sandbox/No episode table')

PAGE_LIMIT = 50

page_count = 0

# regexes
multipleIssues, hatnote, displayTitle, engVar, shortDesc = (
    re.compile(p, re.I) for p in (
        r'\{\{multiple issues\|\n?',
        r'\{\{(?:For(?:-text|-multi)?|Other uses(?: of)?|About(?:-distinguish(?:-text))?|Redirect(?:2|-multi|-several)|Distinguish)\|.*?\}\}\n?',
        r'\{\{(?:DISPLAYTITLE:.*?|Lowercase title|Italic title)\}\}',
        r'\{\{use (?:[dmy]{3} dates|[A-Z][a-z]+ English).*?\}\}',
        r'\{\{short description\|.*?\}\}\n?'
    )
)

for page in list_page.linkedPages(
    namespaces=[0], follow_redirects=True, content=True, total=None
    ):

    if PAGE_LIMIT > 0 and page_count >= PAGE_LIMIT:
        print('Page limit reached')
        break

    templates = page.templates()

    if "Convert to Episode table" in (page.title(with_ns=False) for page in templates):
        print('Already tagged')
        page_count += 1

    original_text = page.text

    page: pywikibot.Page

    m: re.Match

    # Per MOS:SECTIONORDER
    
    # Group in multiple issues template, if present
    if (m := multipleIssues.search(page.text)):
        pos = m.end()
    # After hatnote, if present
    elif (m := hatnote.search(page.text)):
        pos = m.end()
    # After DISPLAYTITLE, if present
    elif (m := displayTitle.search(page.text)):
        pos = m.end()
    # Before English variety / date format, if present
    elif (m := engVar.search(page.text)):
        pos = m.start()
    # After short description, if present
    elif (m := shortDesc.search(page.text)):
        pos = m.end()
    # Else, set pos to beginning of page
    else:
        pos = 0

    pos = min(max(pos, 0), len(page.text)) # clamp position

    page.text = page.text[:pos] + '{{Convert to Episode table}}\n' + page.text[pos:]

    page.save(summary='Tagging page with {{[[Template:Convert to Episode table|Convert to Episode table]]}} (Task 3, TRIAL)', minor=True, bot=True)

    page_count += 1
