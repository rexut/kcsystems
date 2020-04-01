Documentation with Sphinx
#########################

Excerpts from the `Sphinx Tutorial by Eric Holscher`_ and
`Documentation Style Guide by Bareos GmbH & Co. KG and others`_.
See :cite:`juh2014swdocwspx` for an introduction to Sphinx.

This documentation is built using `Sphinx`_, a static-site generator designed
to create structured, semantic, and internally consistent documentation.
Source documents are written in `reStructuredText`_, a semantic, extensible
markup syntax similar to Markdown.

* :duuser:`reStructuredText Primer <quickstart>` --
  Introduction to reStructuredText

  * :duuser:`reStructuredText Quick Reference <quickref>`
  * :duuser:`reStructuredText 1-page cheat sheet <cheatsheet>`

* :doc:`Sphinx Markup <sphinx:usage/restructuredtext/index>` --
  Detailed guide to Sphinx's markup concepts and reStructuredText extensions

.. note::

   Sphinx and reStructuredText can be very flexible. For the sake of
   consistency and maintainability, this how to guide is *highly opinionated*
   about how documentation source files are organized and marked up.

.. toctree::
   :caption: Table of Contents
   :maxdepth: 1
   :titlesonly:

   sphinx/concepts
   sphinx/extensions
   sphinx/themes
   sphinx/cheatsheet

.. Local variables:
   coding: utf-8
   mode: text
   mode: rst
   End:
   vim: fileencoding=utf-8 filetype=rst :
