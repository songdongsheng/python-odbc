import sys, os

from setuptools import setup

import odbc

long_description = open('README').read()


setup_args = dict(
    name="odbc",
    version=odbc.__version__,
    author="Dongsheng Song",
    author_email="dongsheng.song@gmail.com",
    description='Python ODBC 3.x library (ctypes-based binding)',
    long_description=long_description,
    download_url="http://python-odbc.googlecode.com/files/python-odbc-%s.tar.gz" % (odbc.__version__),
    url="http://code.google.com/p/python-odbc/",
    license="Apache License 2.0",
    platforms="any",
    classifiers="""\
Development Status :: 5 - Production/Stable
Environment :: Console
Intended Audience :: Developers
License :: OSI Approved :: Apache License 2.0
Operating System :: OS Independent
Programming Language :: Python
Topic :: Software Development""".splitlines(),
    packages=['odbc'],
)

if __name__ == '__main__':
    setup(**setup_args)
