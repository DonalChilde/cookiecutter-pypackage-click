Welcome to {{ cookiecutter.project_name }}'s documentation!
======================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   readme
   installation
   usage
   api
   contributing
   {% if cookiecutter.create_author_file == 'y' -%}authors
   {% endif -%}changelog
   dev_instructions

Indices and tables
==================
* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
