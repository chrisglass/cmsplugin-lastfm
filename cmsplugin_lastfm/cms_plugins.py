from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cmsplugin_lastfm import models

import feedparser
from datetime import datetime
from time import mktime

from string import Template
from django.core.cache import cache

# Cache stuff
CKEY = 'cmsplugin_lastfm_'
CTIMEOUT = 60*2# 2 minutes

URL = Template('http://ws.audioscrobbler.com/2.0/user/$user/recenttracks.rss')


def get_feed_for_user(user):
    local_key = "%s%s" % (CKEY, user)
    feed = cache.get(local_key)
    if not feed:
        feed = feedparser.parse(URL.substitute({'user':user}))
        cache.set(local_key,feed,CTIMEOUT)
        
    # If the feed contains a date in the future, remove it
    now = datetime.now()
    feed['items'] = [item for item in feed['items'] if datetime.fromtimestamp(mktime(item['updated_parsed'])) <= now]
        
    return feed

class RecentTracksPlugin(CMSPluginBase):
    model = models.RecentTracks
    name = 'LastFM Recently Played Tracks Plugin'
    render_template = 'cmsplugin_lastfm/recent_tracks.html'
    
    def render(self, context, instance, placeholder):
        feed = get_feed_for_user(instance.lastfm_user)
        context.update({'instance': instance, 'feed': feed})
        return context
    
plugin_pool.register_plugin(RecentTracksPlugin)