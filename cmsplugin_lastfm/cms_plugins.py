from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cmsplugin_lastfm import models

import feedparser

from string import Template
from django.core.cache import cache

# Cache stuff
CKEY = 'cmsplugin_lastfm_'
CTIMEOUT = 60*2# 2 minutes

URL = Template('http://ws.audioscrobbler.com/2.0/user/$user/recenttracks.rss')

class RecentTracksPlugin(CMSPluginBase):
    model = models.RecentTracks
    name = 'LastFM Recently Played Tracks Plugin'
    render_template = 'cmsplugin_lastfm/recent_tracks.html'
    
    def render(self, context, instance, placeholder):
        local_key = "%s%s" % (CKEY, instance.lastfm_user)
        feed = cache.get(local_key)
        if not feed:
            feed = feedparser.parse(URL.substitute({'user':instance.lastfm_user}))
            cache.set(local_key,feed,CTIMEOUT)
        context.update({'instance': instance, 'feed': feed})
        return context
    
plugin_pool.register_plugin(RecentTracksPlugin)