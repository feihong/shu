# Shu - A Tool for Making Chinese Ebooks

Shu is a tool that scrapes content from Chinese literature websites to assemble an ebook that you can easily consume on your mobile device.

## Installation

```
pip install virtualenvwrapper
mkvirtualenv --python=`which python3` shu
pip install -r requirements.txt
python setup.py develop
```

## Instructions

To make an ebook, look at the programs in the example directory and copy the one most similar to what you want to do. Use the [Firefinder add-on for Firefox](https://addons.mozilla.org/en-US/firefox/addon/firefinder-for-firebug/) to preview what elements will get picked up your CSS selectors.
