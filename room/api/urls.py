from django.conf.urls import url, include

urlpatterns = [
    url(r'^v1/room/', include('room.api.v1.urls')),
]
