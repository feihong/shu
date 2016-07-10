from pathlib import Path
from setuptools import setup


requirements_file = Path(__file__).parent / 'requirements.txt'
requires = requirements_file.read_text().split()


setup(
    name='shu',
    version='0.2.1',
    description='Tool for making Chinese ebooks',
    url='http://github.com/feihong/shu',
    license='MIT',
    packages=['shu'],
    install_requires=requires,
)
