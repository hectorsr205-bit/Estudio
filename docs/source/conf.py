# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# --- CONFIGURACIÓN DE RUTAS REQUERIDA POR EL EXAMEN ---
import os
import sys
sys.path.insert(0, os.path.abspath('../../'))

# -- Project information -----------------------------------------------------
project = 'Piedra Papel Tijera'
copyright = '2026, hector'
author = 'hector'

# -- General configuration ---------------------------------------------------
# --- EXTENSIONES OBLIGATORIAS DEL ENUNCIADO ---
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx_markdown_builder'
]

templates_path = ['_templates']
exclude_patterns = []

language = 'es'

# -- Options for HTML output -------------------------------------------------
html_theme = 'alabaster'
html_static_path = ['_static']
