# -*- coding: utf-8 -*-
# Copyright: (c) 2016, Chamchenko
# GNU General Public License v2.0+ (see LICENSE.txt or https://www.gnu.org/licenses/gpl-2.0.txt)
# This file is part of plugin.video.awaan


from __future__ import unicode_literals
import json
import xbmcplugin
import sys
import urlquick

from .vars import *
from .tools import *
from .create_item import addDir
from .create_item import addLink


def browseCategories():
    log('browseCategories')
    log(" Fetching url: %s" % CATEGORIES_URL)
    log(" Fetching params: %s" % CATEGORIES_PARAMS)
    categories = json.loads(
                    urlquick.get(CATEGORIES_URL,
                            params=CATEGORIES_PARAMS,
                            headers=headers).text)
    categories.append({'id': '', 'title_ar': 'الكل'})
    for category in categories:
        category_id = category['id']
        if category_id == "208109" or category_id == "30348":
            continue
        category_name = formatTitles(category['title_ar'])
        print(category_name)
        SHOWS_PARAMS.update({'cat_id': category_id})
        infos = json.dumps(SHOWS_PARAMS)
        addDir(category_name, infos, 3)


def browseGenre(cat_id):
    log('browseGenre')
    log(" Fetching url: %s" % CATEGORIES_URL)
    log(" Fetching params: %s" % CATEGORIES_PARAMS)
    del(SHOWS_PARAMS['exclude_cat_id'])
    cat_id = int(cat_id)
    SHOWS_PARAMS.update({'cat_id': cat_id, 'genre_id': 65})
    genres = json.loads(
                urlquick.get(SHOWS_URL,
                        params=SHOWS_PARAMS,
                        headers=headers).text)['data']['genres']
    genres.append({'id': '', 'title': 'الكل'})
    for genre in genres:
        genre_id = genre['id']
        genre_name = formatTitles(genre['title'])
        SHOWS_PARAMS.update({'genre_id': genre_id})
        infos = json.dumps(SHOWS_PARAMS)
        addDir(genre_name, infos, 3)

def getTvShows(infos):
    log('getTvShows')
    xbmcplugin.setContent(int(sys.argv[1]), 'videos')
    SHOWS_PARAMS = json.loads(infos)
    log(" Fetching url: %s" % SHOWS_URL)
    log(" Fetching params: %s" % SHOWS_PARAMS)
    apijson = json.loads(
                urlquick.get(SHOWS_URL,
                    headers=headers,
                    params=SHOWS_PARAMS).text)
    for item in apijson['data']['shows']:
        title = formatTitles(item['title_ar'])
        showId = item['id']
        plot =  item['description_ar'] 
        thumb = IMG_BASE_URL % (item['thumbnail'] or item['cover'] or item['atv_thumbnail'])
        fanart = IMG_BASE_URL % (item['atv_thumbnail'] or item['cover'] or item['thumbnail'])
        if not thumb.endswith('.jpg') or thumb.endswith('.jpeg') or thumb.endswith('.png'):
            thumb = fanart
        infoList = {
                    "mediatype": "tvshows",
                    "title": title,
                    "TVShowTitle": title,
                    "plot": plot
                }
        infoArt = {
                    "thumb": thumb,
                    "poster": thumb,
                    "fanart": fanart,
                    "icon": ICON,
                    "logo": ICON
                }
        infos = json.dumps({
                            'showId': showId,
                            'thumb': thumb,
                        })
        xbmcplugin.addSortMethod(int(sys.argv[1]) , xbmcplugin.SORT_METHOD_LABEL)
        xbmcplugin.addSortMethod(int(sys.argv[1]) , xbmcplugin.SORT_METHOD_TITLE)
        addDir(title, showId, 5, infoArt, infoList,0, showId)


def getEpisodes(showId):
    log('getEpisodes')
    xbmcplugin.setContent(int(sys.argv[1]), 'episodes')
    SHOW_PARAMS.update({'show_id': showId})
    log(" Fetching url: %s" % SHOW_URL)
    log(" Fetching params: %s" % SHOW_PARAMS)
    items = json.loads(urlquick.get(SHOW_URL, params=SHOW_PARAMS,
                    headers=headers).text)
    showTitle = formatTitles(items['cat']['title_ar'])
    default_season = items['default_season']
    if default_season and len(items['seasons']) > 1:
        for se in items['seasons']:
                title = formatTitles(se['title_ar'])
                seasonid = se['id']
                thumb = IMG_BASE_URL % (se['app_thumbnail'] or se['cover'] or se['app_cover'])
                infoList = {
                    "mediatype": "seasons",
                    "title": title,
                    "TVShowTitle": showTitle
                }
                infoArt = {
                    "thumb": thumb,
                    "poster": thumb,
                    "fanart": thumb,
                    "icon": thumb,
                    "logo": thumb
                }
                addDir(title, seasonid, 5, infoArt, infoList,0, se['id'])
        return

    if default_season:
        for se in items['seasons']:
            if se['id'] == default_season:
                try:
                    season = [int(s) for s in se['title_ar'].split() if s.isdigit()][-1]
                except:
                    season = 1
    else:
        try:
            season = [int(s) for s in showTitle.split() if s.isdigit()][-1]
            showTitle = formatTitles(items['cat']['root_title'])
        except:
            season = 1
            showTitle = formatTitles(items['cat']['root_title'])
    for item in items['videos']:
        streamID = item['id']
        title = formatTitles(item['title_ar'])
        thumb = IMG_BASE_URL % item['img']
        aired = str(item['publish_time']).split(' ')[0]
        duration = item['duration']
        infoLabels = {
                        "mediatype": "episode",
                        "title": title,
                        "aired": aired,
                        "duration": duration,
                        "TVShowTitle": showTitle
                    }
        infoArt = {
                    "thumb":thumb,
                    "poster":thumb,
                    "fanart":thumb,
                    "icon":thumb,
                    "logo":thumb
                }
        try:
            episode_number = [int(s) for s in title.split() if s.isdigit()][-1]
            infoLabels.update({'title': showTitle, 'episode': episode_number, 'season': season})
            xbmcplugin.addSortMethod(int(sys.argv[1]) , xbmcplugin.SORT_METHOD_EPISODE)
        except:
            pass
        addLink(title, streamID, 9, infoLabels, infoArt)
