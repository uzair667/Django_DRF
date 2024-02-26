from django.contrib import admin

from .models import Users
from posts.models import Posts

admin.site.register(Users)
admin.site.register(Posts)
