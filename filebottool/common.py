#
# common.py
#
# Copyright (C) 2009 laharah <laharah+fbt@gmail.com>
#
# Basic plugin template created by:
# Copyright (C) 2008 Martijn Voncken <mvoncken@gmail.com>
# Copyright (C) 2007-2009 Andrew Resch <andrewresch@gmail.com>
# Copyright (C) 2009 Damien Churchill <damoxc@gmail.com>
#
# Deluge is free software.
#
# You may redistribute it and/or modify it under the terms of the
# GNU General Public License, as published by the Free Software
# Foundation; either version 3 of the License, or (at your option)
# any later version.
#
# deluge is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with deluge.    If not, write to:
# 	The Free Software Foundation, Inc.,
# 	51 Franklin Street, Fifth Floor
# 	Boston, MA  02110-1301, USA.
#
#    In addition, as a special exception, the copyright holders give
#    permission to link the code of portions of this program with the OpenSSL
#    library.
#    You must obey the GNU General Public License in all respects for all of
#    the code used other than OpenSSL. If you modify file(s) with this
#    exception, you may extend this exception to your version of the file(s),
#    but you are not obligated to do so. If you do not wish to do so, delete
#    this exception statement from your version. If you delete this exception
#    statement from all source files in the program, then also delete it here.
#

import logging
from deluge.log import LOG as delugelog

PLUGIN_NAME = "FileBotTool"


def get_resource(filename):
    import pkg_resources, os
    return pkg_resources.resource_filename("filebottool", os.path.join("data", filename))


def version_tuple(s):
    # if not re.match(r'\d+\.', s):
    #     raise ValueError("Cannot parse version {0}.".format(s))
    return tuple(int(x) for x in s.split('.'))


class PrefixHandler(logging.Handler):
    def __init__(self, prefix=""):
        logging.Hander.__init__(self)
        self._prefix = prefix

    def emit(self, record):
        record.msg = "%s%s" % (self._prefix, record.msg)


LOG_HANDLER = PrefixHandler("[{0}]".format(PLUGIN_NAME))
