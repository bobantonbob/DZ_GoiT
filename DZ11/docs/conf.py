import sys
import os
# Отримати поточний робочий каталог (абсолютний шлях до поточної директорії)
# current_directory = os.getcwd()

# Додати поточний робочий каталог до шляху пошуку модулів
# sys.path.append(current_directory)
sys.path.append(os.path.abspath('..'))
# Додаємо шлях до кореневої директорії проекту до шляху Python
# sys.path.insert(0, os.path.abspath('..'))

project = 'Contact project'
copyright = '2024, Babenko A'
author = 'Babenko A'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.autodoc']

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'nature'
html_static_path = ['_static']
