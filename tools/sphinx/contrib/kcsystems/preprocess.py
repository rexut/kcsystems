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
import subprocess
import fnmatch
import tempfile

from docutils.utils import Reporter
from docutils import frontend
from sphinx.util import console

# from .font_map import DiagFontMap
from .util import silentremove



class KCSystemsReporter(Reporter):
    """
    Subclass of docutils.util.Reporter with default values
    """
    def __init__(self):
        settings = frontend.OptionParser().get_default_values()
        settings.report_level = 1
        Reporter.__init__(  # super does not work because of class-method-init
            self,
            source='KCSystems',
            report_level=settings.report_level,
            halt_level=settings.halt_level,
            stream=settings.warning_stream,
            debug=settings.debug,  # alternative: debug=console,
            encoding=settings.error_encoding,
            error_handler=settings.error_encoding_error_handler
        )


class FileHandlerWithRemoveOnError(object):
    """
    Context handler (to be used with *with* statement that

    - Encapsolates a file resouce
    - Removes the file in case of an Exception
    """
    def __init__(self, filename, option):
        self._fd = open(filename, option)
        self._filename = filename

    def __enter__(self):
        return self._fd

    def __exit__(self, e_type, e_value, e_traceback):
        self._fd.close()
        if e_type:  # we got a exception and invalidate the output
            silentremove(self._filename)
            return True  # do not reraise the exception


#############################################################################
# FIXME: use the Python native binding to librsvg and make sure,
#        that all generated files will be removed on the end of
#        Sphinx processing
#

# DIA to SVG conversion
DIA2SVG = ['dia']
DIA2SVG_FLAGS = [
    '--filter=svg',
]

# SVG to SVG conversion
SVG2SVG = ['rsvg-convert']
SVG2SVG_FLAGS = [
    '--format=svg',
    '--keep-aspect-ratio',
]

# SVG to PDF conversion
SVG2PDF = ['rsvg-convert']
SVG2PDF_FLAGS = [
    '--format=pdf',
    '--keep-aspect-ratio',
]

# SVG to PNG conversion
SVG2PNG = ['rsvg-convert']
SVG2PNG_FLAGS = [
    '--format=png',
    '--keep-aspect-ratio',
    '--dpi-x=90',
    '--dpi-y=90',
#   '--background-color=\#00',
]

SVG2ANY_LOGO_FLAGS = [
    '--width=100',
    '--height=100',
]

# ICO assembly
ICOTOOL = ['icotool']
ICOTOOL_FLAGS = [
    '--create',
    '--icon',
]


def find_files(directory, pattern):
    """
    @brief Find all files that match a pattern
    @param directory: The directory where to start from
    @param pattern: A file globbing pattern like *.svg
    @return !!Generator!! yields tuples of ( directory, basename, filename )
    """
    for root, _, files in os.walk(directory):
        for basename in files:
            if fnmatch.fnmatch(basename, pattern):
                filename = os.path.join(root, basename)
                yield (root, basename, filename)


class PreprocessImages(object):
    """
    This class is a Strategy pattern and implements preprocessing of images
    required for LaTeX and cleanup
    """
    _cleanup = []

    def __init__(self, app):
        self._app = app
        self._reporter = KCSystemsReporter()

    def run(self):
        """
        Image preprocessing:
        - process all images found in a list of directories matching
          certain patterns (*.dia, *.svg)
        - create pdf versions and png version
        - create svg from dia

        @param kcsystems_image_dirs: List of directories to parse (sphinx config)
        """
        self._reporter.debug('Start image preprocessing')
        self._reporter.info('kcsystems_image_dirs: {0}'.format(str(
                                        self._app.config.kcsystems_image_dirs)))


        for rel_image_dir in self._app.config.kcsystems_image_dirs:
            image_dir = os.path.join(self._app.srcdir, rel_image_dir)
            for ( _, _, img ) in find_files(image_dir, '*.dia'):

                self._reporter.info('Process Dia Image: {0}'.format(img))
                subprocess.call(DIA2SVG + DIA2SVG_FLAGS + [
                    '--export=' + img[:-4] + '.svg', img,
                ])
                self._cleanup.append(img[:-4] + '.svg')

            for ( _, _, img ) in find_files(image_dir, '*.svg'):

                self._reporter.info('Process SVG Image: {0}'.format(img))
                with FileHandlerWithRemoveOnError(img[:-4] + '.pdf', 'w') as out:
                    self._cleanup.append(img[:-4] + '.pdf')
                    subprocess.call(SVG2PDF + SVG2PDF_FLAGS + [img], stdout=out)
                with FileHandlerWithRemoveOnError(img[:-4] + '.png', 'w') as out:
                    self._cleanup.append(img[:-4] + '.png')
                    subprocess.call(SVG2PNG + SVG2PNG_FLAGS + [img], stdout=out)

        self._reporter.debug('Finish image preprocessing')

    def cleanup(self):
        """
        Remove the generated image files from source tree
        """
        self._reporter.debug('Cleanup image preprocessing')
        for filename in self._cleanup:
            silentremove(filename)
            self._reporter.info('Cleanup: remove {0}'.format(filename))


class ProcessLogo(object):
    """
    This class is a Strategy pattern and implements preprocessing of images
    required for LaTeX and cleanup
    """
    _cleanup = []

    def __init__(self, app):
        self._app = app
        self._reporter = KCSystemsReporter()

    def run(self):
        """
        Convert the logo (in svg) format to pdf and favicon.

        @param logo_source:  The relative path (from document source) and name
                             of source svg logo file (sphinx config)
        @param latex_logo:   The relative path (from document source) and name
                             of target LaTeX file - a pdf format (sphinx config)
                             if None no LaTeX logo will be produced
        @param html_logo:    The relative path (from document source) and name
                             of target HTML file - a svg format (sphinx config)
                             if None no HTML logo will be produced
        @param html_favicon: The relative path (from document source) and name
                             of HTML favicon file (sphinx config)
                             if None no favicon will be produced
        """
        self._reporter = KCSystemsReporter()
        self._reporter.debug('Start logo image preprocessing')
        self._reporter.debug('logo_source: {0}'.format(self._app.config.kcsystems_logo_source))
        self._reporter.debug('latex_logo: {0}'.format(self._app.config.latex_logo))
        self._reporter.debug('html_logo: {0}'.format(self._app.config.html_logo))
        self._reporter.debug('html_favicon: {0}'.format(self._app.config.html_favicon))

        src_logo = os.path.join(self._app.srcdir,
                                self._app.config.kcsystems_logo_source)

        if None != self._app.config.latex_logo:
            latex_logo = os.path.join(self._app.srcdir,
                                      self._app.config.latex_logo)
            with FileHandlerWithRemoveOnError(latex_logo, 'w') as output:

                self._cleanup.append(latex_logo)
                subprocess.check_call(SVG2PDF + SVG2PDF_FLAGS + \
                    SVG2ANY_LOGO_FLAGS + [src_logo], stdout=output)
                # raise Exception('test')
                self._reporter.info('Created LaTeX logo: {0}'.format(
                                                                latex_logo))

        if None != self._app.config.html_logo:
            html_logo = os.path.join(self._app.srcdir,
                                      self._app.config.html_logo)
            with FileHandlerWithRemoveOnError(html_logo, 'w') as output:

                self._cleanup.append(html_logo)
                subprocess.check_call(SVG2SVG + SVG2SVG_FLAGS + [
                    '--width=16', '--height=16', src_logo,
                ], stdout=output)
                # raise Exception('test')
                self._reporter.info('Created HTML logo: {0}'.format(
                                                                html_logo))

        if None != self._app.config.html_favicon:
            html_favicon = os.path.join(self._app.srcdir,
                                        self._app.config.html_favicon)
            tmp_16 = ''  # dummy temporary filenames,
            tmp_32 = ''  # that do not exist and cannot be removed
            with FileHandlerWithRemoveOnError(html_favicon, 'w') as output:

                with tempfile.NamedTemporaryFile(delete=False,
                        prefix='kcs-logo-16-', suffix='.png') as output_16:
                    tmp_16 = output_16.name  # this file needs to be removed
                    subprocess.check_call(SVG2PNG + SVG2PNG_FLAGS + [
                        '--width=16', '--height=16', src_logo,
                    ], stdout=output_16)

                with tempfile.NamedTemporaryFile(delete=False,
                        prefix='kcs-logo-32-', suffix='.png') as output_32:
                    tmp_32 = output_32.name
                    subprocess.check_call(SVG2PNG + SVG2PNG_FLAGS + [
                        '--width=32', '--height=32', src_logo,
                    ], stdout=output_32)

                self._cleanup.append(html_favicon)
                subprocess.check_call(ICOTOOL + ICOTOOL_FLAGS + [
                                output_16.name, output_32.name], stdout=output)

                self._reporter.info('Created HTML favicon: {0}'.format(
                                                                html_favicon))

            # all exceptions are catched, we need to remove potential temporary
            # file names
            silentremove(tmp_16)
            silentremove(tmp_32)
        self._reporter.debug('Finish logo image preprocessing')

    def cleanup(self):
        """
        Remove the generated image files from source tree
        """
        self._reporter.debug('Cleanup logo image preprocessing')
        for filename in self._cleanup:
            silentremove(filename)
            self._reporter.info('Cleanup: remove {0}'.format(filename))


def on_builder_inited(self):
    """
    @brief KCSystems stuff prepreprocessing
    """
    ProcessLogo(self.builder).run()
    PreprocessImages(self.builder).run()


def on_build_finished(self, exception):
    """
    @brief KCSystems stuff cleanup of preprocessing prepreprocessing
    """
    # DiagFontMap().cleanup()
    ProcessLogo(self.builder).cleanup()
    PreprocessImages(self.builder).cleanup()

