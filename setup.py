from setuptools import setup, find_packages

version = __import__('cmsplugin_lastfm').__version__

setup(
    name = 'cmsplugin_lastfm',
    version = version,
    description = 'Django CMS Last.fm Plugins',
    author = 'Christopher Glass',
    author_email = 'christopher.glass@divio.ch',
    url = 'http://github.com/chrisglass/cmsplugin_lastfm',
    packages = find_packages(),
    package_data={
        'cmsplugin_lastfm': [
            'templates/cmsplugin_lastfm/*.html',
        ]
    },
    zip_safe=False,
    install_requires=[
        "django-cms",
    ]
)
