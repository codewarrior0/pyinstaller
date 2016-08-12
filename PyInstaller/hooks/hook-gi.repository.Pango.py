#-----------------------------------------------------------------------------
# Copyright (c) 2005-2016, PyInstaller Development Team.
#
# Distributed under the terms of the GNU General Public License with exception
# for distributing bootloader.
#
# The full license is in the file COPYING.txt, distributed with this software.
#-----------------------------------------------------------------------------
"""
Import hook for PyGObject https://wiki.gnome.org/PyGObject
"""

from PyInstaller.utils.hooks import get_gi_typelibs

binaries, datas, hiddenimports = get_gi_typelibs('Pango', '1.0')

def pre_safe_import_module(api):
    # PyGObject modules loaded through the gi repository are marked as
    # MissingModules by modulegraph so we convert them to
    # RuntimeModules so their hooks are loaded and run.
    api.add_runtime_module(api.module_name)
