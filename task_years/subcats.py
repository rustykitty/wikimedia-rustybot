import pywikibot
from pywikibot import page
from time import sleep
import os

site = pywikibot.Site()

cat = page.Category(site, 'Years')

subcats = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'subcats.txt'), 'w') 

for sub in cat.subcategories():
    print(sub.title())