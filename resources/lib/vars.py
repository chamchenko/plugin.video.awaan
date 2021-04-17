# -*- coding: utf-8 -*-
# Copyright: (c) 2016, Chamchenko
# GNU General Public License v2.0+ (see LICENSE.txt or https://www.gnu.org/licenses/gpl-2.0.txt)
# This file is part of plugin.video.awaan

from __future__ import unicode_literals
import xbmcaddon
from xbmc import getInfoLabel
ADDON_ID = 'plugin.video.awaan'
REAL_SETTINGS = xbmcaddon.Addon(id=ADDON_ID)
ADDON_NAME = REAL_SETTINGS.getAddonInfo('name')
SETTINGS_LOC = REAL_SETTINGS.getAddonInfo('profile')
ADDON_PATH = REAL_SETTINGS.getAddonInfo('path')
ADDON_VERSION = REAL_SETTINGS.getAddonInfo('version')
ICON = REAL_SETTINGS.getAddonInfo('icon')
FANART = REAL_SETTINGS.getAddonInfo('fanart')
LANGUAGE = REAL_SETTINGS.getLocalizedString
DEBUG = REAL_SETTINGS.getSetting('Debugging') == 'true'
XBMC_VERSION = int(getInfoLabel("System.BuildVersion").split('-')[0].split('.')[0])
INPUTSTREAM_PROP = 'inputstream' if XBMC_VERSION >= 19 else 'inputstreamaddon'
USER_AGENT = "awaan-ios/5.4.4 (iPhone; iOS 14.4; Scale/2.00)"
headers = {"User-Agent": USER_AGENT}


IMG_BASE_URL = 'https://admango.cdn.mangomolo.com/analytics/%s'
API_BASE_URL = 'https://admin.mgmlcdn.com/analytics/index.php/'
URL_LIVES = API_BASE_URL + 'plus/live_channels'
URL_LIVE = API_BASE_URL + 'plus/getchanneldetails'
CATEGORIES_URL = API_BASE_URL + 'plus/categories'
SHOWS_URL = API_BASE_URL + 'endpoint/genres/shows_by_genre'
SHOW_URL = API_BASE_URL + 'plus/show'
EPISODE_URL = API_BASE_URL + 'nand/fullVideo'


PARAMS_LIVES = {
                    'user_id':71,
                    'key': 'e2c420d928d4bf8ce0ff2ec1',
                    'device_id': 'F10379E579E54FE3ABB3D46B6AACF62D',
                    'json': 1,
                    'is_radio': 0
                }
PARAMS_LIVE_TV = {
                    "key": "e2c420d928d4bf8ce0ff2ec1",
                    "user_id": 71,
                    "app_id": 1,
                    "need_playback": "yes",
                    "need_geo": "yes",
                    "need_live": "yes"
                }
CATEGORIES_PARAMS = {
                        'key': 'e2c420d928d4bf8ce0ff2ec1',
                        'user_id': '71',
                        'app_id': '1',
                        'exclude_channel_id': '176'
                    }
SHOWS_PARAMS = {
                    'user_id': '71',
                    'key': 'e2c420d928d4bf8ce0ff2ec1',
                    'p': '1',
                    'limit': '300',
                    'is_radio': '0',
                    'need_show_times': 'no',
                    'need_channel': 'yes',
                    'exclude_cat_id': '30348,208109',
                    'custom_order': 'yes',
                    'app_id': '1',
                    'exclude_channel_id': '176'
                }
SHOW_PARAMS = {
                'key': 'e2c420d928d4bf8ce0ff2ec1',
                'user_id': '71',
                'p': '1',
                'limit': '1000',
                'need_completion': 'yes',
                'channel_userid': '499344',
                'limit_also': '2',
                'need_trailer': 'yes',
                'app_id': '1',
                'need_like': 'yes',
                'cast': 'yes',
                'need_avg_rating': 'yes',
                'need_avg_videos_duration': 'yes',
                'need_production_year': 'yes'
            }
EPISODE_PARAMS = {
                    'key': 'e2c420d928d4bf8ce0ff2ec1',
                    'user_id': '71',
                    'channel_userid': '499344',
                    'app_id': '1',
                    'need_channel_details': 'yes'
                }
MAIN_MENU = [('\u0627\u0644\u0645\u0628\u0627\u0634\u0631', "", 1),
             ('\u0627\u0644\u0645\u0633\u0644\u0633\u0644\u0627\u062a', "30348", 2),
             ('\u0627\u0644\u0628\u0631\u0627\u0645\u062c', "", 6),
             ('\u0627\u0644\u0623\u0641\u0644\u0627\u0645', "208109", 2)]
