from django.contrib import admin
from watchlist_app import models

# Register your models here.

admin.site.register(models.WatchList)
admin.site.register(models.StreamingPlatform)
admin.site.register(models.Review)