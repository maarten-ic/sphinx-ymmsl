Get Started
===============

This page gives a quick overview of how to get started with **sphinx-ymmsl**.

Installation
------------

To install sphinx-ymmsl use pip: 

.. code-block:: bash

   pip install sphinx-ymmsl

Configuration
-------------

To use sphinx-ymmsl in your Sphinx documentation project, you need to add it to the list of extensions in your ``conf.py`` file:

.. code-block:: python

   extensions = [
       'sphinx_ymmsl',
       # ... other extensions
   ]

Basic Usage
-----------

Once the extension is configured, you can use the ``.. ymmsl::`` directive in your reStructuredText files to include documentation generated from a yMMSL file.

Syntax
~~~~~~

The basic syntax is:

.. code-block:: rst

   .. ymmsl:: path/to/your/file.ymmsl

The path should be relative to your Sphinx source directory (typically the ``docs/`` folder).


When Sphinx builds your documentation, the ``.. ymmsl::`` directive will:

1. Parse the yMMSL file
2. Generate formatted Markdown documentation
3. Convert the Markdown to HTML

How It Is Converted
-------------------

This section describes how the yMMSL file is translated into documentation, so you
know what to change to adapt your documentation.

Generated Titles
~~~~~~~~~~~~~~~~

The extension automatically derives all titles and section headings from names in the
yMMSL file and from the filename itself. The same formatting rule applies throughout:
underscores are replaced with spaces and each word is capitalised (e.g.
``macro_micro_model`` becomes ``Macro Micro Model``).

**Page title**

The top-level page title comes from the **filename** of the yMMSL file (without the
``.ymmsl`` extension). For example, ``macro_micro_model.ymmsl`` produces the heading
*Macro Micro Model*.

To change the page title, rename the yMMSL file.

**Model and component section titles**

Each model and component gets its own section. The heading is derived from the
**key name** used in the yMMSL file — under ``models:`` for models and under
``components:`` for components. To change a heading, rename the corresponding key.

