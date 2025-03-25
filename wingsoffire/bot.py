import pywikibot
import pywikibot.pagegenerators as pagegenerators
import pywikibot.textlib as textlib

site = pywikibot.Site('wingsoffire:en')


for page in pagegenerators.SearchPageGenerator('Blurb', site=site, namespaces=[0]):
    print(page.title())
    # if not textlib.does_text_contain_section(page.text, 'blurb', site=site):
    #     continue
    content = textlib.extract_sections(page.text, site=site)
    
    section = next((section for section in content if section.heading == 'Blurb'), None)

    if section:
        section.text = section.text.replace('\n', '\n\n')
    print(section.text)
