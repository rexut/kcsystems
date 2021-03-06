.. index::
   pair: Sphinx; Block Diagram Family

Block Diagram Family
####################

`blockdiag <http://blockdiag.com/>`_ and its family generate diagram images
from simple text files:

.. blockdiag::

   blockdiag {
     blockdiag -> generates -> "block-diagrams";
     blockdiag -> is -> "very easy!";

     blockdiag [color = "greenyellow"];
     "block-diagrams" [color = "pink"];
     "very easy!" [color = "orange"];
   }

:Features:

   1. Supports many types of diagrams

      * block diagram (w/ :doc:`blockdiag <bldiag:blockdiag/sphinxcontrib>`)
      * sequence diagram (w/ :doc:`seqdiag <bldiag:seqdiag/sphinxcontrib>`)
      * activity diagram (w/ :doc:`actdiag <bldiag:actdiag/sphinxcontrib>`)
      * logical network diagram (w/ :doc:`nwdiag <bldiag:nwdiag/sphinxcontrib>`)
      * rack-structure diagram (w/ :doc:`rackdiag <bldiag:nwdiag/sphinxcontrib>`)
      * packet header diagram (w/ :doc:`packetdiag <bldiag:nwdiag/sphinxcontrib>`)

   2. Generates beautiful diagram images from simple text format
      (similar to Graphviz's ``dot`` format)
   3. Layouts diagram elements automatically
   4. Embeds to many documentations; Sphinx, Trac, Redmine,
      and some Wikis

.. toctree::
   :caption: List of Types
   :maxdepth: 1
   :titlesonly:

   blockdiag/blockdiag
   blockdiag/seqdiag
   blockdiag/actdiag
   blockdiag/nwdiag

.. Local variables:
   coding: utf-8
   mode: text
   mode: rst
   End:
   vim: fileencoding=utf-8 filetype=rst :
