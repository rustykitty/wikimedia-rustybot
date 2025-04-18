"""
UNTESTED CODE
"""

import re

import pywikibot

PATTERN = re.compile(r"\{\{AfC submission\|(d\||\|\|)?ts=(?:(\d{2}):(\d{2}), (\d{1,2}) (January|February|March|April|May|June|July|August|September|October|November|December) (\d{4}) \(UTC\))(?:\|\w+=[^|}]+)*?\}\}", flags=re.I)
# {{AFC submission|d|ts=00:00, 1 January 1970 (UTC)}}
# {{AfC submission|||ts=20250413180647}}

site = pywikibot.Site()

def parse_date_format(hour: str, minute: str, day: str, month: str, year: str):
    return ''.join((
        year,
        "January February March April May June July August September October November December".split().index(month),
        day,
        hour,
        minute
    )) + "00" # seconds

for page in pywikibot.pagegenerators.SearchPageGenerator(
              r"insource:/\{\{AfC submission.*?\|ts=[0-9]{2}:/i", 
              namespaces=[0], 
              site=site, content=True
):
    match = PATTERN.search(page.content)
    if match:
        has_other_templates = page.content.lower().count('{{afc submission') > 1
        if has_other_templates:
            # just remove this one
            page.content = page.content[:match.start(0)] + page.content[match.end(0):]
        else:
            template = "{{AfC submission|||ts=" + parse_date_format(re.group(1), re.group(2), re.group(3), re.group(4), re.group(5)) + "}}"
            page.content = page.content[:match.start(0)] +  + page.content[match.end(0):]
