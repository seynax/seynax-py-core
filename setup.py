import os
from setuptools import setup


# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(file_name):
    return open(os.path.join(os.path.dirname(__file__), file_name)).read()


setup(
    name='seynax_py_core',
    version='1.0.0',
    author='Seynax',
    description='Code used by Seynax into multiples python projects',
#    long_description=read('README'),
    license='GNU General Public License v3.0',
    keywords='seynax_py_core seynax-py-core seynax core',
    url='https://github.com/seynax/seynax-py-core',
    classifiers=[
        "Development Status :: 1 - Alpha",
        "Topic :: Utilities",
        "License :: GNU General Public License v3.0",
    ]
)
