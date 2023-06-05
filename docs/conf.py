import datetime
import os
import sys

from findmyorder import __version__

sys.path.append(os.path.abspath(os.pardir))

# -- General configuration ----------------------------------------------------
templates_path = ['_templates']
extensions = ['sphinx.ext.autodoc',
              'sphinx.ext.ifconfig',
              'sphinx.ext.extlinks']
source_suffix = '.rst'
master_doc = 'index'
project = 'FindMyOrder'
year = datetime.datetime.now().date().year
copyright = f'2023–{year}'
exclude_patterns = ['_build']
release = __version__
version = '.'.join(release.split('.')[:1])
last_stable = __version__
rst_prolog = '''
.. |last_stable| replace:: :findmyorder-doc:`{}`
'''.format(last_stable)

extlinks = {
    'pelican-doc':  ('https://talkytrader.gitbook.io/talky/', '%s')
}

# -- Options for HTML output --------------------------------------------------

html_theme = 'furo'
html_title = f'<strong>{project}</strong> <i>{release}</i>'
html_static_path = ['_static']
html_theme_options = {
    'light_logo': 'talky-logo.svg',
    'dark_logo': 'talky-logo.svg',
    'navigation_with_keys': True,
}

# Output file base name for HTML help builder.
htmlhelp_basename = 'fmo'

html_use_smartypants = True

# If false, no module index is generated.
html_use_modindex = False

# If false, no index is generated.
html_use_index = False

# If true, links to the reST sources are added to the pages.
html_show_sourcelink = False


def setup(app):
    # overrides for wide tables in RTD theme
    app.add_css_file('theme_overrides.css')   # path relative to _static


