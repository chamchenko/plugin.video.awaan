# -*- coding: utf-8 -*-
# Copyright: (c) 2016, Chamchenko
# GNU General Public License v2.0+ (see LICENSE.txt or https://www.gnu.org/licenses/gpl-2.0.txt)
# This file is part of plugin.video.awaan

from __future__ import unicode_literals
import json
import re
import xbmcplugin
import sys
import urlquick

from .vars import *
from .create_item import addLink
from .tools import log


def browseLiveTV():
    log(" Fetching url: %s" % URL_LIVES)
    log(" Fetching params: %s" % PARAMS_LIVES)
    items = json.loads(urlquick.get(URL_LIVES, params=PARAMS_LIVES, headers=headers).text)
    for channel in items:
        channel_id = channel['id']
        title = channel['title_en']
        thumb_path = channel['atv_thumbnail']
        fanart_path = channel['cover']
        if not thumb_path:
            thumb = ICON
        else:
            thumb = IMG_BASE_URL % thumb_path
        if not fanart_path:
            fanart = FANART
        else:
            fanart = IMG_BASE_URL % fanart_path
        infoLabels = {"title":title}
        infoArt = {
                    "thumb": thumb,
                    "poster": thumb,
                    "fanart": fanart,
                    "icon": thumb,
                    "logo": thumb
                }
        addLink(title, channel_id, 8, infoLabels, infoArt, len(items))
