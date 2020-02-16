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

import os
import sphinx
import pybtex.style.formatting
from preprocess import on_builder_inited, on_build_finished

def default_logo_path(config):
    """
    @brief Determine the default logo path. (svg)

    If kcsystems_logo_source is set it is used instead the build in path.

    If the kcsystems_logo_source is not set, it is set to default svg logo.

    @param config: The config object
    @return logo path pointing to the default svg logo, if nothing is set
    """
    path = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                        'lpn-logo.svg'))
    return path

def setup(app):
    """
    @brief Main entry point for KC Systems Sphinx contribution.

    Introduce style sheets,
    register event handling functions,
    define extension configuration items

    @param app: The documentation application
    """
    app.add_config_value('kcsystems_logo_source', default_logo_path, '')
    app.add_config_value('kcsystems_image_dirs', [], '')

    app.connect("builder-inited", on_builder_inited)
    app.connect("build-finished", on_build_finished)

    app.add_stylesheet('fix-cite.css')
    app.add_stylesheet('fix-float.css')
    app.add_stylesheet('ansi-color.css')
    app.add_stylesheet('strikethrough.css')
