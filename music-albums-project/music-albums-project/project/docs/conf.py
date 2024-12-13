# -*- coding: utf-8 -*-
import os
import sys
sys.path.insert(0, os.path.abspath('..'))

project = 'Music Albums Project'
author = 'Your Name'
release = '1.0'

extensions = [
    'sphinx.ext.autodoc',
]

templates_path = ['_templates']
exclude_patterns = []

html_theme = 'alabaster'