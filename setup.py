#!/usr/bin/env python
from setuptools import find_packages, setup

from oscar_promotions import VERSION

setup(
    name='django-oscar-promotions',
    version=VERSION,
    url='https://github.com/django-oscar/django-oscar-promotions',
    author='Oscar Team',
    author_email='ryan@supported.systems',
    description='Promotions for Django Oscar',
    long_description=open('README.rst').read(),
    license='BSD',
    packages=find_packages(exclude=['sandbox*', 'tests*']),
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 2.0',
        'Framework :: Django :: 3.0',
        'Framework :: Django :: 4.0',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: Unix',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
    install_requires=['django>=2.2', 'django-oscar>=2.0'],
)
