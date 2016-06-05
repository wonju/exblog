from django.conf.urls import url
from django.contrib import admin

from wpsblog.views import *


urlpatterns = [
    url(r'^admin/', admin.site.urls),

	url(r'^$', home, name="home"),
    url(r'^about/us/$', about, name="about"),
	url(r'^rooms/(?P<room_id>\d+)/$', room, name="room"),
	url(r'^news/$', news, name="news"),

    url(r'^policy/terms/$', terms, name="terms"),
    url(r'^policy/privacy/$', privacy, name="privacy"),
    url(r'^policy/disclaimer/$', disclaimer, name="disclaimer"),
]
