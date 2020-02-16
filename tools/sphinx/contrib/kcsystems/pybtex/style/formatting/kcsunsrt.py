# -*- coding: utf-8 -*-
#
# Copyright (c) 2014 Stephan Linz
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
# CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#

from pybtex.style.formatting.unsrt import Style as UnsrtStyle
from pybtex.style.template import (
    join, words, field, optional, first_of,
    names, sentence, tag, optional_field, href
)
from pybtex.richtext import Text, Symbol


class Style(UnsrtStyle):

    def format_edition(self, e):
        # FIXME: evaluate the field 'language' and translate
        return optional [
            words [
                field('edition', apply_func=lambda x: x.lower()),
                'edition',
            ]
        ]

    def format_volume_and_series(self, e, as_sentence=True):
        # FIXME: evaluate the field 'language' and translate
        volume_and_series = optional [
            words [
                'volume', field('volume'), optional [
                    words ['of', field('series')]
                ]
            ]
        ]
        number_and_series = optional [
            words [
                join(sep=Symbol('nbsp')) ['number', field('number')],
                optional [
                    words ['in', field('series')]
                ]
            ]
        ]
        series = optional_field('series')
        result = first_of [
                volume_and_series,
                number_and_series,
                series,
            ]
        if as_sentence:
            return sentence(capfirst=True) [result]
        else:
            return result

    def format_web_refs(self, e):
        # based on urlbst output.web.refs
        return sentence(capfirst=False) [
            optional [ self.format_isbn10(e) ],
            optional [ self.format_isbn13(e) ],
            optional [ self.format_oclc(e) ],
            optional [ self.format_url(e) ],
            optional [ self.format_eprint(e) ],
            optional [ self.format_pubmed(e) ],
            optional [ self.format_doi(e) ],
            optional [ self.format_dsa(e) ],
            optional [ self.format_ghd(e) ],
            optional [ self.format_gsc(e) ],
            ]

    def format_isbn10(self, e):
        # based on numbst format.isbn10
        return words [
            'ISBN-10:',
            href [
                join [
                    'http://GetTextbooks.com/isbn/',
                    field('isbn10')
                    ],
                field('isbn10')
                ]
            ]

    def format_isbn13(self, e):
        # based on numbst format.isbn13
        return words [
            'ISBN-13:',
            href [
                join [
                    'http://GetTextbooks.com/isbn/',
                    field('isbn13')
                    ],
                field('isbn13')
                ]
            ]

    def format_oclc(self, e):
        # based on numbst format.oclc
        return words [
            'OCLC:',
            href [
                join [
                    'http://www.worldcat.org/oclc/',
                    field('oclc')
                    ],
                field('oclc')
                ]
            ]

    def format_url(self, e):
        # based on urlbst format.url
        return words [
            'URL:',
            href [
                field('url'),
                field('url')
                ],
            join [
                optional [ '(', field('urldate'), ')' ]
                ]
            ]

    def format_dsa(self, e):
        # based on urlbst format.dsa
        return words [
            'DSA:',
            href [
                join [
                    'http://pdf.datasheetarchive.com/',
                    field('dsa'),
                    '.pdf'
                    ],
                field('dsa', apply_func=lambda x: x.split('/')[-1])
                ],
            join [
                sentence(capfirst=False, add_period=False) [
                    '(PDF',
                    optional_field('dsasize'),
                    optional_field('dsadate'),
                    ],
                ')'
                ]
            ]

    def format_ghd(self, e):
        # based on urlbst format.ghd
        return words [
            'GDR-HC Download:',
            href [
                join [
                    'http://www.homecomputer-ddr.de.vu/wiki/lib/exe/fetch.php/',
                    field('ghd')
                    ],
                field('ghd', apply_func=lambda x: x.split('/')[-1])
                ],
            join [
                sentence(capfirst=False, add_period=False) [
                    '(PDF',
                    optional_field('ghdsize'),
                    optional_field('ghddate'),
                    ],
                ')'
                ]
            ]

    def format_gsc(self, e):
        # based on urlbst format.gsc
        return words [
            'GDR-Semiconductor:',
            href [
                join [
                    'https://www-user.tu-chemnitz.de/~heha/bastelecke/Konsumg%C3%BCter-Bastelei/DDR-Halbleiter/',
                    field('gsc')
                    ],
                field('gsc', apply_func=lambda x: x.split('/')[-1])
                ],
            join [
                sentence(capfirst=False, add_period=False) [
                    '(PDF',
                    optional_field('gscsize'),
                    optional_field('gscdate'),
                    ],
                ')'
                ]
            ]
