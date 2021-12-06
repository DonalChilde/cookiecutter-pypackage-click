=========
Dev Setup
=========

Initial Project Setup
---------------------

From the project directory, run

.. code-block:: bash
    # Make a virtualenv in the project directory, and install requirements.
    ./scripts/run.sh venv:init:all
    # Activate the virtualenv
    source ./.venv/bin/activate
    # Make a local git repo
    ./scripts/run.sh git:init
    # To set a github remote origin...
    # https://docs.github.com/en/github/using-git/adding-a-remote
    git remote add origin https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}.git

Downloading project from github
-------------------------------

From the parent directory of the project

.. code-block:: bash
    git clone git@github.com:{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}.git


TODO project setup from github

Remove Example Code
-------------------

TODO List code modules and doc files to be removed.


Tips and fixes
--------------

To run git commit without git precommit hooks -

.. code-block:: bash
    git commit -m "Some comments" --no-verify
