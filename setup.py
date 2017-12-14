from pathlib import Path
from setuptools import setup


setup(
    name='shu',
    version='0.3.0',
    description='Library for making Chinese ebooks',
    url='http://github.com/feihong/shu',
    license='MIT',
    packages=['shu'],
    install_requires=[
        'html5lib>=1.0.1',
        'lxml>=4.1.1',
        'pyquery>=1.3.0',
        'requests>=2.18.4',
        'urlpath>=1.1.2',
    ],
)
