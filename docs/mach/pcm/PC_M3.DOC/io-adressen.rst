.. index:: pair: PC/M; Input/Output Adressen

Input/Output Adressen
#####################

.. .. tabularcolumns:: lLL
.. tabularcolumns:: p{0.12\linewidth}p{0.24\linewidth}p{0.44\linewidth}
.. table:: |PC/M| - IN-/OUT Port Adressen
   :name: kcsystems-mach-pcm-tabelle-1
   :widths: 15, 30, 55
   :class: longtable
   :align: center
   :width: 80%

   +-----------------------------+---------------------+----------------------------+
   | Adressen                    | Zuordnung           | Baustein                   |
   +=============================+=====================+============================+
   | :port:`80H` |-| :port:`83H` | Kanal 0 bis Kanal 3 | System |CTC| :comp:`D55`   |
   +-----------------------------+---------------------+----------------------------+
   | :port:`84H` |-| :port:`85H` | Daten Port A/B      | System |PIO| :comp:`D56`   |
   +-----------------------------+---------------------+----------------------------+
   | :port:`86H` |-| :port:`87H` | Steuerwort Port A/B | System |PIO| :comp:`D56`   |
   +-----------------------------+---------------------+----------------------------+
   | :port:`88H` |-| :port:`89H` | Daten Port A/B      | Anwender |SIO| :comp:`D57` |
   +-----------------------------+---------------------+----------------------------+
   | :port:`8AH` |-| :port:`8BH` | Steuerwort Port A/B | Anwender |SIO| :comp:`D57` |
   +-----------------------------+---------------------+----------------------------+
   | :port:`8CH` |-| :port:`8FH` | Kanal 0 bis Kanal 3 | Anwender |CTC| :comp:`D58` |
   +-----------------------------+---------------------+----------------------------+
   | :port:`90H` |-| :port:`91H` | Daten Port A/B      | Anwender |PIO| :comp:`D59` |
   +-----------------------------+---------------------+----------------------------+
   | :port:`92H` |-| :port:`93H` | Steuerwort Port A/B | Anwender |PIO| :comp:`D59` |
   +-----------------------------+---------------------+----------------------------+
   | :port:`94H` |-| :port:`97H` | Speicherblockselektport                          |
   +-----------------------------+--------------------------------------------------+
   | :port:`98H` |-| :port:`9BH` | |NMI| Generator                                  |
   +-----------------------------+--------------------------------------------------+
   | :port:`9CH` |-| :port:`9FH` | :signal:`/IOSEL 0` für den Anschluss peripherer  |
   |                             | Bausteine                                        |
   +-----------------------------+--------------------------------------------------+

.. Local variables:
   coding: utf-8
   mode: text
   mode: rst
   End:
   vim: fileencoding=utf-8 filetype=rst :
