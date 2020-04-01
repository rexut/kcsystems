.. index::
   triple: Sphinx; Syntax; Directives

Directives
##########

A :term:`sphinx:directive` is an
:doc:`/appendix/howtos/sphinx/concepts/explicit-markup`
that allows marking a block of content with special meaning.

.. rubric:: basic directive syntax looks like this

:the example:

   .. code-block:: rst
      :linenos:

      .. directive:: arg1 arg2 ...
         :option1: value
         :option2: value
         :option5: value
         ...

         Multiline content of the directive,
         ...

   This is no longer part of the block controlled by the directive.

   ``arg1, arg2, ...``
      Arguments. The last argument can contain spaces (depending on the
      directive implementation).

   ``:option0:, :option1:, ... :option9:``
      Options are optional.

Directives are supplied not only by Docutils, but Sphinx and custom extensions
can add their own. Directives are written as a block.

Docutils supports the following directives (incomplete list):

* :doc:`/appendix/howtos/sphinx/concepts/admonition`:
  :dudir:`attention`, :dudir:`caution`, :dudir:`danger`,
  :dudir:`error`, :dudir:`hint`, :dudir:`important`, :dudir:`note`,
  :dudir:`tip`, :dudir:`warning` and the generic
  :dudir:`admonition <admonitions>`. (Most themes style only "note" and
  "warning" specially.)

* :ref:`docutils:attention`
* :ref:`docutils:parsed-literal`
* :ref:`docutils:csv-table`
* :ref:`docutils:contents`
* :ref:`docutils:section-autonumbering`
* :ref:`docutils:header`
* :ref:`docutils:target-notes`
* :ref:`docutils:replace`
* :ref:`docutils:unicode`
* :ref:`docutils:include`
* :ref:`docutils:raw-directive`
* :ref:`docutils:classes`
* :ref:`docutils:role`
* :ref:`docutils:default-role`

.. seealso::

   * Refer to :ref:`sphinx:rst-directives`
     for directives provided by Docutils.
   * Refer to :doc:`sphinx:usage/restructuredtext/directives`
     for directives added by Sphinx.

.. Local variables:
   coding: utf-8
   mode: text
   mode: rst
   End:
   vim: fileencoding=utf-8 filetype=rst :
