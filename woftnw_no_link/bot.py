import pywikibot
import pywikibot.pagegenerators

site = pywikibot.Site('woftnw:en')

f = open('templates_no_link.txt', 'a')
f2 = open('templates_with_link.txt', 'a')

def better_len(i):
    try:
        return len(i)
    except TypeError:
        n = 0
        for _ in i:
            n += 1
        return n

for page in pywikibot.pagegenerators.AllpagesPageGenerator('!', 10, True, site=site):
    if page.title().endswith('/doc'): continue
    if better_len(page.backlinks(total=1)) == 0:
        f.write(page.title())
        f.write('\n')
    else:
        f2.write(page.title())
        f2.write('\n')

f.flush()
f.close()