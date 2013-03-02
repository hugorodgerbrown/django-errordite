"""
Setup file for django-errordite.
"""
import os
from os.path import join, dirname, normpath, abspath
from setuptools import setup
import django_errordite

# allow setup.py to be run from any path
os.chdir(normpath(join(abspath(__file__), os.pardir)))

setup(
    name=django_errordite.__title__,
    version=django_errordite.__version__,
    packages=['django_errordite'],
    install_requires=['errordite>=0.3'],
    include_package_data=True,
    license=open(join(dirname(__file__), 'LICENCE.md')).read(),
    description=django_errordite.__description__,
    long_description=open(join(dirname(__file__), 'README.rst')).read(),
    url='https://github.com/hugorodgerbrown/python-errordite',
    author=django_errordite.__author__,
    author_email='hugo@rodger-brown.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
