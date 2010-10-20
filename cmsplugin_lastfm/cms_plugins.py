from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cmsplugin_lastfm import models

import feedparser

class RecentTracksPlugin(CMSPluginBase):
    model = models.RecentTracks
    name = 'LastFM Recently Played Tracks Plugin'
    render_template = 'cmsplugin_lastfm/recent_tracks.html'
    
    def render(self, context, instance, placeholder):
        feed = feedparser.parse({'user':instance.lastfm_user})
        context.update({'instance': instance, 'feed': feed})
        return context