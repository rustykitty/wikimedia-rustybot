import pywikibot
from pywikibot import page
from time import sleep
import os
os.path.dirname(os.path.realpath(__file__))
os.path.join(os.path.dirname(os.path.realpath(__file__)), 'page_titles.txt')

site = pywikibot.Site()

ad_cat = page.Category(site, 'Years AD')
ad_cat_link = ad_cat.aslink()

for year in open(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'page_titles.txt')):
    year = year.strip()[3:]
    page = pywikibot.Page(site, f'AD {year}')
    if not page.botMayEdit():
        print('skipped', year)
        sleep(1)
        continue
    if ad_cat not in page.categories():
        page.text += ad_cat_link
        print(year, 'Add to cat')
    for redir_page in (f'AD{year}', f'{year} AD', f'{year}AD'):
        if redir_page.exists():
            continue
        redir_page.set_redirect_target(f'AD {year}', create=True, summary='Creating redirect to year page (Task 2)')