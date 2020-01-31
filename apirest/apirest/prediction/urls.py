from django.conf.urls   import url
from prediction         import views

urlpatterns = [
    url(r'^predict/$'              , views.predict),
    url(r'^incidents/$'               , views.incident_list  ),
    url(r'^incident/(?P<pk>[0-9]+)/$' , views.incident_detail),
]