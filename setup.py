# coding: utf8

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

__version__ = (0, 1, 0)

setup(
    name='python-drip',
    packages=['python-drip'],
    version='.'.join(str(x) for x in __version__),
    description="DRIP API implementation",
    author='Urbvan Transit',
    author_email='dharwin@urbvan.com',
    url='https://github.com/urbvantransit/python-drip',
    download_url='https://github.com/urbvantransit/python-drip/tarball/master',
    keywords=['getdrip', 'drip'],
    classifiers=[],
    license='MIT license',
    install_requires=[
        'requests',
        'marshmallow'
    ],
)
