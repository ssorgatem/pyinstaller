#! /usr/bin/env python
#
# Build packages using spec files
#
# Copyright (C) 2005-2011, Giovanni Bajo
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA
# 02110-1301, USA

try:
    import PyInstaller
except ImportError:
    # if importing PyInstaller fails, try to load from current
    # directory or parent directory to support running without
    # installation
    import imp, os
    if not hasattr(os, "getuid") or os.getuid() != 0:
        imp.load_module('PyInstaller', *imp.find_module('PyInstaller', [".", ".."]))

import PyInstaller.build
from PyInstaller.lib.pyi_optparse import OptionParser

parser = OptionParser(usage="%prog [options] specfile")
parser.add_option('-C', '--configfile',
                  default=PyInstaller.build.DEFAULT_CONFIGFILE,
                  dest='configfilename',
                  help='Name of generated configfile (default: %default)')
PyInstaller.build.__add_options(parser)

opts, args = parser.parse_args()
if len(args) != 1:
    parser.error('Requires exactly one .spec-file')

PyInstaller.build.main(args[0], **opts.__dict__)
