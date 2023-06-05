# Configuration file for the Sphinx documentation builder.

#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'FindMyOrder'
copyright = '2023, MrAniki'
author = 'MrAniki'
release = '2023'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


smv_branch_whitelist = "main"
if os.getenv("BUILD_DOCS_FOR_HEAD", "False").lower() == "true":
    if not (branch := os.getenv("BRANCH_NAME")):
        with contextlib.suppress(git.InvalidGitRepositoryError):
            branch = git.Repo(PROJECT_ROOT).active_branch.name



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'furo'
html_static_path = ['_static']

