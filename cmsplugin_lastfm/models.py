from cms.models import CMSPlugin
from django.db import models
from django.utils.translation import ugettext_lazy as _

class RecentTracks(CMSPlugin):
    lastfm_user= models.CharField(_("The LastFM username you wish to follow"),max_length=255)