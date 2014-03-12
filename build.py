from pelican import Pelican
import pelican.settings


import os



settings = pelican.settings.DEFAULT_CONFIG

for i in ['PATH', 'OUTPUT_PATH', 'THEME', 'SITEURL']:
    del settings[i]

settings.update({
    u'THEME_STATIC_DIR':'theme',
    u'AUTHOR': '',
    u'SITENAME': 'Open Science Collaboration Blog',
    u'TIMEZONE': 'America/New_York',
    u'LINKS': (
    ),
    u'SOCIAL' : (
    ),
})

settings['ARTICLE_URL'] = '{date:%Y}/{date:%m}/{date:%d}/{slug}/'
settings['ARTICLE_SAVE_AS'] = '{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'
settings['DISQUS_SITENAME'] = 'opensciencecollaboration'


def generate(settings,
    input_path=None,
    output_path=None,
    theme_path=None,
    siteurl=None,
    static_paths=None,
    plugin_path=None,
    plugins=None
):
    settings['PATH'] = input_path
    settings['OUTPUT_PATH'] =  output_path
    settings['THEME'] = theme_path
    settings['SITEURL'] = siteurl
    settings['STATIC_PATHS'] = static_paths
    settings["PLUGIN_PATH"] = plugin_path
    settings["PLUGINS"] = plugins


    if settings['SITEURL'].endswith('/'):
        settings['SITEURL'] = settings['SITEURL'][:-1]

    if not os.path.exists(settings['OUTPUT_PATH']):
        os.mkdir(settings['OUTPUT_PATH'])

    settings = pelican.settings.configure_settings(settings)
    Pelican(settings).run()

if __name__ == '__main__':
    generate(
        settings,
        input_path='site/content',
        output_path='output/',
        theme_path='pelican-mockingbird/',
        siteurl='http://osc.centerforopenscience.org',
        static_paths=['images', 'static'],
        plugin_path='plugins',
        plugins=["share-post"]
    )
