from django.contrib import admin

# Register your models here.
from .models import User, listing, bid, comment, category, watchlist

admin.site.register(User)
admin.site.register(listing)
admin.site.register(bid)
admin.site.register(comment)
admin.site.register(category)
admin.site.register(watchlist)