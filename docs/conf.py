# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
projectPath = os.path.abspath('..')
sys.path.insert(0, projectPath)
sys.path.append(os.path.join(projectPath, 'src', 'Documentation'))


# -- Project information -----------------------------------------------------

project = 'Informatik 2'
copyright = '2022, Thomas Kirchmeier'
author = 'Thomas Kirchmeier'

# The full version, including alpha/beta/rc tags
release = '0.0.1'

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.napoleon',
    'sphinx.ext.autodoc', 
    'rinoh.frontend.sphinx' # works with Python3.9 for hmtl
    ]

latex_elements = {
    'papersize'    : 'a4paper',
    'pointsize'    : '11pt',
    'preamble'     : '',
    'figure_align' : 'htbp'
    }

rinoh_documents = [dict(
    doc='index',        # top-level file (index.rst)
    target='tk_doc',    # output file (manual.pdf)
    #template='article', #
    template='myTemplate.rtt', #
    )]   

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
# html_theme = 'alabaster'
html_theme = 'classic'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']