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

Generated Titles
~~~~~~~~~~~~~~~~

The extension automatically derives all titles and section headings from names in the
yMMSL file and from the filename itself. The same formatting rule applies throughout:
underscores are replaced with spaces and each word is capitalised (e.g.
``macro_micro_model`` becomes ``Macro Micro Model``).

**Page title**

The top-level page title comes from the **filename** of the yMMSL file (without the
``.ymmsl`` extension). For example, ``macro_micro_model.ymmsl`` produces the heading
*Macro Micro Model Documentation*.

To change the page title, rename the yMMSL file.

**Model section title**

Each model in the file gets its own section. The heading is derived from the **key
under** ``models:`` in the yMMSL file. For example:

.. code-block:: yaml

   models:
     macro_micro_model:
       ...

produces the section heading *Macro Micro Model*.

To change the model section title, rename the key under ``models:``.

**Component section title**

Each component within a model gets its own subsection. The heading comes from the
**key under** ``components:``. For example:

.. code-block:: yaml

   components:
     macro:
       ...

produces the subsection heading *Macro*.

To change a component subsection title, rename the key under ``components:``.

