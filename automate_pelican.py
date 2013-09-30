from pelican import Pelican
import pelican.settings

import os
import pprint
import shutil

settings = pelican.settings.DEFAULT_CONFIG

for i in ['PATH', 'OUTPUT_PATH', 'THEME', 'SITEURL']:
    del settings[i]

settings.update({
    u'THEME_STATIC_DIR':'theme',
    u'AUTHOR': '',
    u'SITENAME': 'Open Science Collaboration Blog',
    u'TIMEZONE': 'America/New_York',
    u'LINKS': (
        ('Center for Open Science', 'http://centerforopenscience.org/'),
    ),
    u'SOCIAL' : (
        ('You can add links in your config file', '#'),
        ('Another social link', '#'),
    ),
})

settings['ARTICLE_URL'] = '{date:%Y}/{date:%m}/{date:%d}/{slug}/'
settings['ARTICLE_SAVE_AS'] = '{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'
settings['DISQUS_SITENAME'] = 'opensciencecollaboration'

def generate(settings, input_path=None, output_path=None, theme_path=None, siteurl=None ):
    settings['PATH'] = input_path
    settings['OUTPUT_PATH'] =  output_path
    settings['THEME'] = theme_path
    settings['SITEURL'] = siteurl

    if settings['SITEURL'].endswith('/'):
        settings['SITEURL'] = settings['SITEURL'][:-1]

    if not os.path.exists(settings['OUTPUT_PATH']):
        os.mkdir(settings['OUTPUT_PATH'])

    settings = pelican.settings.configure_settings(settings)
    Pelican(settings).run()

shutil.rmtree('output')
os.mkdir('output')

generate(
    settings,
    input_path='site/content',
    output_path='output/',
    theme_path='pelican-mockingbird/',
    siteurl='http://localhost:63342/osc.centerforopenscience.org/output/'
)
