import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='onespacemedia-cms-faqs',
    version='0.1.1',
    url='https://github.com/onespacemedia/cms-faqs',
    packages=['faqs'],
    include_package_data=True,
    license='BSD License',  # example license
    description='A FAQ management app for use with the Onespacemedia CMS.',
    long_description=README,
    author='Onespacemedia',
    author_email='developers@onespacemedia.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',  # example license
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        # Replace these appropriately if you are stuck on Python 2.
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    install_requires=[
        'django',
        'psycopg2',
        'django-suit',
        'django-optimizations',
        'Pillow',
        'django-reversion',
        'django-usertools',
        'django-historylinks',
        'django-watson',
        'django-extensions',
        'Werkzeug',
        'onespacemedia-cms'
    ]
)
