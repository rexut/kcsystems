.. index::
   triple: Sphinx; Syntax; Paragraphs

Paragraphs
##########

The :duref:`paragraph <paragraphs>` is the most basic block in a
reStructuredText document. Paragraphs are simply chunks of text separated
by one or more blank lines. As in Python, indentation is significant in
reStructuredText, so all lines of the same paragraph must be left-aligned
to the same level of indentation. General rules can be looked up under
:doc:`/appendix/howtos/sphinx/concepts/whitespace`.

:the example:

   .. literalinclude:: paragraphs-example.rsti
      :end-before: .. Local variables:
      :language: rst
      :linenos:

:which gives:

   .. include:: paragraphs-example.rsti

Quotes (block quotation) element
********************************

:duref:`Block quoted <block-quotes>` paragraphs are quoted by just indenting
them more than the surrounding paragraphs.

:the example:

   .. literalinclude:: paragraphs-bq-example.rsti
      :end-before: .. Local variables:
      :language: rst
      :linenos:

:which gives:

   .. include:: paragraphs-bq-example.rsti

Line blocks
***********

:duref:`Line blocks <line-blocks>` are useful for addresses, verse, and
adornment-free lists. They are quoted by just a ``|`` pipe sign in front
of each single line.

:the example:

   .. literalinclude:: paragraphs-lb-example.rsti
      :end-before: .. Local variables:
      :language: rst
      :linenos:

:which gives:

   .. include:: paragraphs-lb-example.rsti

Doctest blocks
**************

:duref:`Doctest blocks <doctest-blocks>` are interactive Python sessions
cut-and-pasted into docstrings. They do not require the
:doc:`literal blocks </appendix/howtos/sphinx/concepts/code-example>` syntax.
The doctest block must end with a blank line and should not end with an unused
prompt, see :ref:`rst-doctest-blocks`.

:the example:

   .. literalinclude:: paragraphs-dt-example.rsti
      :end-before: .. Local variables:
      :language: rst
      :linenos:

:which gives:

   .. include:: paragraphs-dt-example.rsti

.. Local variables:
   coding: utf-8
   mode: text
   mode: rst
   End:
   vim: fileencoding=utf-8 filetype=rst :
