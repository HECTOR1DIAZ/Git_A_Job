from django.conf.urls import url, include

urlpatterns = [
    url(r'^',include('apps.option_app.routes')),
]
