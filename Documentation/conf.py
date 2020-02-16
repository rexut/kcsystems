# -*- coding: utf-8 -*-
#
# kcsystems documentation build configuration file, created by
# sphinx-quickstart on Tue Oct  7 11:43:41 2014.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import sys
import os

# import Sphinx Bootstrap Theme
import sphinx_bootstrap_theme as bssp
    
# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#sys.path.insert(0, os.path.abspath('.'))
path = os.path.abspath(os.path.join(os.getcwd(), '..', 'tools', 'sphinx', 'contrib'))
sys.path.append(path)

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
needs_sphinx = '1.2'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
#   'easydev.copybutton',
#   'sphinx.ext.autodoc',
#   'sphinx.ext.autosummary',
#   'sphinx.ext.autosgen',
    'sphinx.ext.doctest',
    'sphinx.ext.coverage',
    'sphinx.ext.todo',
    'sphinx.ext.ifconfig',
#   'sphinx.ext.intersphinx',
#   'sphinx.ext.pngmath',
    'sphinx.ext.mathjax',
#   'sphinx.ext.jsmath',
#   'sphinx.ext.graphviz',
#   'sphinx.ext.inheritance_diagram',
    'sphinx.ext.extlinks',
#   'sphinx.ext.viewcode',
#   'sphinx.ext.linkcode',
#   'sphinxjp.themes.basicstrap',
    'sphinxarg.ext',
    'sphinxcontrib.bibtex',
    'sphinxcontrib.spelling',
    'sphinxcontrib.inlinesyntaxhighlight',
    'sphinxcontrib.programoutput',
    'sphinxcontrib.ansi',
    'sphinxcontrib.email',
    'sphinxcontrib.blockdiag',
    'sphinxcontrib.tikz',
#   'matplotlib.sphinxext.only_directives',
#   'matplotlib.sphinxext.plot_directive',
    'kcsystems'
]

# -- KC-Systems Sphinx Extension Configuration ----------------------------

# Source of the logo to be used on that project. must be an svg file
# kcsystems_logo_source = "images/lpn-project-logo.svg"

# List of directories that might contain images, which need to be preprocessed
# so far *.dia and *.svg formats are supported
kcsystems_image_dirs = ['images', 'release-notes/images']

# -- Specific configuration -----------------------------------------------

extlinks = {
    'dsarcidxf':    ('http://pdf.datasheetarchive.com/indexerfiles/%s', 'Datasheet Archive (IDXF): '),
    'dsarcmain':    ('http://pdf.datasheetarchive.com/datasheetsmain/%s', 'Datasheet Archive (MAIN): '),
    'hehaddrhl':    ('https://www-user.tu-chemnitz.de/~heha/bastelecke/Konsumg%%C3%%BCter-Bastelei/DDR-Halbleiter/%s', 'Henrik Haftmann, GDR-Semiconductor: '),
    'hehaddrhlpfx': ('https://www-user.tu-chemnitz.de/~heha/bastelecke/Konsumg%%C3%%BCter-Bastelei/DDR-Halbleiter/#%s', 'Henrik Haftmann, GDR-Semiconductor: '),
    'rtloc':        ('http://www.robotrontechnik.de/html/standorte/%s', 'Robotron Technique, Locations: '),
    'rtstd':        ('http://www.robotrontechnik.de/html/standards/%s', 'Robotron Technique, Standards: '),
    'rtsw':         ('http://www.robotrontechnik.de/html/software/%s', 'Robotron Technique, Software: '),
    'rtcpt':        ('http://www.robotrontechnik.de/html/computer/%s', 'Robotron Technique, Computer: '),
    'rtpnt':        ('http://www.robotrontechnik.de/html/drucker/%s', 'Robotron Technique, Printer: '),
    'rtnet':        ('http://www.robotrontechnik.de/html/netzwerke/netzwerk.htm#%s', 'Robotron Technique, Networks: '),
    'rtk1520':      ('http://www.robotrontechnik.de/html/komponenten/k1520pla.htm#%s', 'Robotron Technique, K1520: '),
    'rtcon':        ('http://www.robotrontechnik.de/html/komponenten/stecker.htm#%s', 'Robotron Technique, Connectors: '),
    'rtfdd':        ('http://www.robotrontechnik.de/html/komponenten/fs.htm#%s', 'Robotron Technique, Floppy Disk Drives: '),
    'rtemr':        ('http://www.robotrontechnik.de/html/komponenten/emr.htm#%s', 'Robotron Technique, The Single-Chip Microcontroller: '),
    'rtic':         ('http://www.robotrontechnik.de/html/komponenten/ic.htm#%s', 'Robotron Technique, Integrated Circuits: '),
    'rtkbd':        ('http://www.robotrontechnik.de/html/zubehoer/tastaturen.htm#%s', 'Robotron Technique, Keyboards: '),
    'tglcate':      ('http://www.wak-gmbh.de/index.php?id=542&tgl-nummer=%s', 'TGL Catalog (EWN): '),
    'tglbarc':      ('https://www.bbr-server.de/bauarchivddr/archiv/tglarchiv/%s', 'TGL Archive (BBSR): '),
    'udbevglddrhl': ('http://www.elektron-bbs.de/elektronik/tabellen/ddr/%s.htm', 'Udo Bertholdt, Vgl. GDR-Semiconductor: '),
    'vopofetch':    ('http://hc-ddr.hucki.net/wiki/lib/exe/fetch.php/%s', 'Volker Pohlers, GDR-HC Download: '),
    '__vopofetch':  ('http://www.homecomputer-ddr.de.vu/wiki/lib/exe/fetch.php/%s', 'Volker Pohlers, GDR-HC Download: '),
    'vopowiki':     ('http://hc-ddr.hucki.net/wiki/doku.php/%s', 'Volker Pohlers, GDR-HC Wiki: '),
    '__vopowiki':   ('http://www.homecomputer-ddr.de.vu/wiki/doku.php/%s', 'Volker Pohlers, GDR-HC Wiki: '),
    'pesarnet':     ('http://www.robotron-net.de/%s', 'Peter Salomon, Robotron Net.: '),
    'itwinfo':      ('http://www.itwissen.info/definition/lexikon/%s', 'German ITwissen.info: '),
    'wikide':       ('http://de.wikipedia.org/wiki/%s', 'German Wikipedia: '),
    'wikien':       ('http://en.wikipedia.org/wiki/%s', 'English Wikipedia: '),
}

# A list of regular expressions that match URIs that should not be checked
# when doing a linkcheck build. Example:
# linkcheck_ignore = [r'http://localhost:\d+/']

# A timeout value, in seconds, for the linkcheck builder. Only works
# in Python 2.6 and higher. The default is to use Python’s global
# socket timeout.
linkcheck_timeout = 60

# The number of worker threads to use when checking links.
# Default is 5 threads.
# linkcheck_workers = 5

# True or false, whether to check the validity of #anchors in links.
# Since this requires downloading the whole document, it’s considerably
# slower when enabled. Default is True.
# linkcheck_anchors = True
linkcheck_anchors = False

# This (boolean) setting triggers, if language, which is set by highlight
# directive, shall be used in code role, if no language is set by a
# customization. The default is True.
# inline_highlight_respect_highlight = True

# This (boolean) setting triggers, if ``literals`` shall be highlighted.
# Default is True.
# inline_highlight_literals = True

# Choose the image processing, either 'Netpbm' or 'ImageMagick'.
# The default is 'Netpbm'.
tikz_proc_suite = 'ImageMagick'

# Enable/disable transparent graphics. The default is True.
tikz_transparent = True

# Add some <string> to the sub process LaTeX preamble for the html build
# target. The default is None.
# tikz_latex_preamble = ''

# Add some \usetikzlibrary{<string>} to the sub process LaTeX preamble
# for the html build target. The default is None.
tikz_tikzlibraries = 'arrows,matrix,calendar,folding'

# String specifying the language, as understood by PyEnchant and enchant.
# Defaults to en_US for US English.
# spelling_lang = 'en_US'

# String specifying a file containing a list of words known to be spelled
# correctly but that do not appear in the language dictionary selected
# by spelling_lang. The file should contain one word per line. Refer to
# the PyEnchant tutorial for details.
# spelling_word_list_filename = 'spelling_wordlist.txt'

# Boolean controlling whether suggestions for misspelled words are printed.
# Defaults to False.
# spelling_show_suggestions = False

# Boolean controlling whether words that look like package names from PyPI
# are treated as spelled properly. When True, the current list of package
# names is downloaded at the start of the build and used to extend the list
# of known words in the dictionary. Defaults to False.
# spelling_ignore_pypi_package_names = False

# Boolean controlling whether words that follow the CamelCase conventions
# used for page names in wikis should be treated as spelled properly.
# Defaults to True.
# spelling_ignore_wiki_words = True

# Boolean controlling treatment of words that appear in all capital letters,
# or all capital letters followed by a lower case s. When True, acronyms are
# assumed to be spelled properly. Defaults to True.
# spelling_ignore_acronyms = True

# Boolean controlling whether names built in to Python should be treated as
# spelled properly. Defaults to True.
# spelling_ignore_python_builtins = True

# Boolean controlling whether words that are names of modules found on
# sys.path are treated as spelled properly. Defaults to True.
# spelling_ignore_importable_modules = True

# List of filter classes to be added to the tokenizer that produces words
# to be checked. The classes should be derived from enchant.tokenize.Filter.
# Refer to the PyEnchant tutorial for examples.
# spelling_filters = []

# Fontpath for blockdiag (truetype font), The default is None.
# blockdiag_fontpath = os.path.abspath('../../tools/sphinx/themes/sphinxdoc-ext/static/dejavusans_book_macroman/DejaVuSans-webfont.ttf')

# Fontmap for blockdiag (maps fontfamily name to truetype font).
# The default is None.
# blockdiag_fontmap = os.path.abspath('./diag.fontmap')

# If this is True, blockdiag generates images with anti-alias filter.
# The default is False.
blockdiag_antialias = True

# You can specify image format on converting docs to HTML; accepts 'PNG'
# or 'SVG'. The default is 'PNG'.
blockdiag_html_image_format = 'SVG'

# You can specify image format on converting docs to TeX; accepts 'PNG'
# or 'PDF'. The default is 'PNG'.
blockdiag_latex_image_format = 'PDF'

# If this is True, todo and todolist produce output, else they produce
# nothing. The default is False.
todo_include_todos = True

# If this is True, ANSI colour sequences in program output are interpreted.
# The default is False.
programoutput_use_ansi = True

# If you do not like the builtin stylesheets, set this to None and create
# your own stylesheet.
html_ansi_stylesheet = None

# Add any paths that contain templates here, relative to this directory.
templates_path = ['../tools/sphinx/templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
#source_encoding = 'utf-8-sig'

# The master toctree document. Default is 'contents'.
master_doc = 'index'

# General information about the main-/sub-projects. List of tuples
# (source start file, target base name, title,
#  author, documentclass)
documents = [
    (   #0: complete documentation
        u'index',
        u'kcsystems',
        u'KC-Systems',
        u'KC-Systems Team',
        u'manual',
    ),
    (   #1: release notes
        u'release-notes/index',
        u'kcsystems-rn',
        u'Release Notes',
        u'KC-Systems Team',
        u'manual',
    ),
]

# General information about the project.
project = documents[0][2]
author = documents[0][3]
publisher = u'Li-Pro.Net'
copyright = u'2014, ' + publisher

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = '0.0'
# The full version, including alpha/beta/rc tags.
release = version + '-unknown' + os.popen('../tools/setlocalversion ..').read().rstrip()

# A string of reStructuredText that will be included at the beginning of every
# source file that is read.
rst_prolog = '''
.. include:: /%s/docroles.inc
.. include:: /%s/docmeta.inc
.. |CREDITS| replace:: :download:`CREDITS </%s/CREDITS>`
.. |LICENSE| replace:: :download:`LICENSE </%s/LICENSE>`
.. |publisher| replace:: %s
.. |author| replace:: %s
.. |project| replace:: %s
.. |rn_project| replace:: %s
''' % (
    os.path.abspath('.'),
    os.path.abspath('.'),
    os.path.abspath('.'),
    os.path.abspath('.'),
    publisher,
    documents[0][3],
    documents[0][2],
    documents[1][2],
)

# A string of reStructuredText that will be included at the end of every source
# file that is read. This is the right place to add substitutions that should be
# available in every file.
rst_epilog = u'''
.. include:: /%s/termsgloss.inc
.. include:: /%s/termsrobtr.inc
.. include:: /%s/termsecisc.inc
.. include:: /%s/termstgls.inc
.. include:: /%s/docextlnk.inc
.. include:: /%s/docunicode.inc
''' % (
    os.path.abspath('.'),
    os.path.abspath('.'),
    os.path.abspath('.'),
    os.path.abspath('.'),
    os.path.abspath('.'),
    os.path.abspath('.'),
)

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = []

# The reST default role (used for this markup: `text`) to use for all
# documents.
#default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
#add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
#modindex_common_prefix = []

# If true, keep warnings as "system message" paragraphs in the built documents.
#keep_warnings = False


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'bootstrap'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#html_theme_options = {}
html_theme_options = {
    # Navigation bar title. (Default: ``project`` value)
    'navbar_title': "KCS Documentation",

    # Tab name for entire site. (Default: "Site")
    'navbar_site_name': "Components",

    # A list of tuples containing pages or urls to link to.
    # Valid tuples should be in the following forms:
    #    (name, page)                 # a link to a page
    #    (name, "/aa/bb", 1)          # a link to an arbitrary relative url
    #    (name, "http://example.com", True) # arbitrary absolute url
    # Note the "1" or "True" value above as the third argument to indicate
    # an arbitrary url.
#   'navbar_links': [
#       ("Examples", "examples"),
#       ("Link", "http://example.com", True),
#   ],

    # Render the next and previous page links in navbar. (Default: True)
#   'navbar_sidebarrel': False,

    # Render the current pages TOC in the navbar. (Default: True)
#   'navbar_pagenav': False,

    # Global TOC depth for "site" navbar tab. (Default: 1)
    # Switching to -1 shows all levels.
#   'globaltoc_depth': -1,

    # Include hidden TOCs in Site navbar?
    #
    # Note: If this is "false", you cannot have mixed ``:hidden:`` and
    # non-hidden ``toctree`` directives in the same page, or else the build
    # will break.
    #
    # Values: "True" (default) or "False"
#   'globaltoc_includehidden': "False",

    # HTML navbar class (Default: "navbar") to attach to <div> element.
    # For black navbar, do "navbar navbar-inverse"
#   'navbar_class': "navbar navbar-inverse",

    # Fix navigation bar to top of page?
    # Values: "True" (default) or "False"
#   'navbar_fixed_top': "False",

    # Location of link to source.
    # Options are "nav" (default), "footer" or anything else to exclude.
#   'source_link_position': "nav",
    'source_link_position': "footer",

    # Bootswatch (http://bootswatch.com/) theme.
    #
    # Options are nothing with "" (default) or the name of a valid theme
    # such as "amelia" or "cosmo" or "united".
   'bootswatch_theme': "custom",

    # Choose Bootstrap version.
    # Values: "3" (default) or "2" (in quotes)
    #         version "2" is not supported by "custom" theme
    'bootstrap_version': "3",
}

# Add any paths that contain custom themes here, relative to this directory.
#html_theme_path = []
html_theme_path = bssp.get_html_theme_path()

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
#html_title = None

# A shorter title for the navigation bar.  Default is the same as html_title.
#html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
#html_logo = None
html_logo = "lpn.svg"

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
#html_favicon = None
html_favicon = "lpn.ico"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['../tools/sphinx/static']

# Add any extra paths that contain custom files (such as robots.txt or
# .htaccess) here, relative to this directory. These files are copied
# directly to the root of the documentation.
#html_extra_path = []

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
#html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
#html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
#html_additional_pages = {}

# If false, no module index is generated.
#html_domain_indices = True

# If false, no index is generated.
#html_use_index = True

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, links to the reST sources are added to the pages.
#html_show_sourcelink = True

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
#html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
#html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = None

# Output file base name for HTML help builder.
htmlhelp_basename = 'kcsystemsdoc'


# -- Options for LaTeX output ---------------------------------------------

latex_additional_files = [
    os.path.abspath(os.path.join(
        os.getcwd(), '..', 'tools', 'sphinx', 'texinputs', 'Makefile')
    ),
]

# TODO: evaluate possible admonitionbox override, see:
#       http://stackoverflow.com/a/13661732
latex_custom = r'''
\setcounter{tocdepth}{3}
\usepackage{fontspec}
\setmainfont{DejaVu Sans Condensed}
\setsansfont{DejaVu Sans Condensed}
\setmonofont{DejaVu Sans Mono}
\setromanfont{DejaVu Serif Condensed}
\hypersetup{unicode=true}
\usepackage{tikz}''' + '''
\usepackage{pgfplots}
\usetikzlibrary{''' + tikz_tikzlibraries + '''}
'''

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    'papersize': 'a4paper',

    # The font size ('10pt', '11pt' or '12pt').
    'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    'inputenc': '',
    'utf8extra': '',
    'preamble': latex_custom,
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [(idx, doc + u'.tex', title, author, dclass)
     for (idx, doc, title, author, dclass) in documents]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
#latex_logo = None
latex_logo = "lpn.pdf"

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters. Default: False.
latex_use_parts = False

# If true, show page references after internal links. Default: False.
latex_show_pagerefs = True

# If true, show URL addresses after external links. Default: 'no'.
# latex_show_urls = 'no'
# latex_show_urls = 'footnote'
# latex_show_urls = 'inline'

# Documents to append as an appendix to all manuals.
latex_appendices = [
    'robotron',
    'ecisc',
    'tgls',
    'glossary',
    'bibliography',
]

# If false, no module index is generated.
#latex_domain_indices = True


# -- Options for Text output ----------------------------------------------

# Determines which end-of-line character(s) are used in text
# output: 'unix', 'windows', or 'native'. Default: 'unix'.
# text_newlines = 'unix'

# A string of 7 characters that should be used for underlining
# sections. The first character is used for first-level headings,
# the second for second-level headings and so on. The default is '*=-~"+`'.
text_sectionchars = '*=-~"+`'


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
# man_pages = [(idx, doc, title, [author], 7) for (idx, doc, title) in documents]

# If true, show URL addresses after external links.
#man_show_urls = False


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
# texinfo_documents = [
#      (idx, doc, title, author, u'Li-Pro.Net',
#      'One line description of project.',
#      'Miscellaneous')
#      for (idx, doc, title) in documents]

# Documents to append as an appendix to all manuals.
#texinfo_appendices = []

# If false, no module index is generated.
#texinfo_domain_indices = True

# How to display URL addresses: 'footnote', 'no', or 'inline'.
#texinfo_show_urls = 'footnote'

# If true, do not generate a @detailmenu in the "Top" node's menu.
#texinfo_no_detailmenu = False


# -- Options for Epub output ----------------------------------------------

# Bibliographic Dublin Core info.
epub_title = documents[0][2]
epub_author = documents[0][3]
epub_publisher = publisher
epub_copyright = copyright

# The basename for the epub file. It defaults to the project name.
#epub_basename = u'kcsystems'

# The HTML theme for the epub output. Since the default themes are not optimized
# for small screen space, using the same theme for HTML and epub output is
# usually not wise. This defaults to 'epub', a theme designed to save visual
# space.
#epub_theme = 'epub'

# The language of the text. It defaults to the language option
# or en if the language is not set.
#epub_language = ''

# The scheme of the identifier. Typical schemes are ISBN or URL.
#epub_scheme = ''

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
#epub_identifier = ''

# A unique identification for the text.
#epub_uid = ''

# A tuple containing the cover image and cover page html template filenames.
#epub_cover = ()

# A sequence of (type, uri, title) tuples for the guide element of content.opf.
#epub_guide = ()

# HTML files that should be inserted before the pages created by sphinx.
# The format is a list of tuples containing the path and title.
#epub_pre_files = []

# HTML files shat should be inserted after the pages created by sphinx.
# The format is a list of tuples containing the path and title.
#epub_post_files = []

# A list of files that should not be packed into the epub file.
epub_exclude_files = ['search.html']

# The depth of the table of contents in toc.ncx.
#epub_tocdepth = 3

# Allow duplicate toc entries.
#epub_tocdup = True

# Choose between 'default' and 'includehidden'.
#epub_tocscope = 'default'

# Fix unsupported image types using the PIL.
#epub_fix_images = False

# Scale large images.
#epub_max_image_width = 0

# How to display URL addresses: 'footnote', 'no', or 'inline'.
#epub_show_urls = 'inline'

# If false, no index is generated.
#epub_use_index = True