from django.conf.urls import include, url
import core.views as coreviews

urlpatterns = [
    url(r'^$', coreviews.LandingView.as_view()),
    url(r'^location/$', coreviews.LocationListView.as_view()),
    url(r'^location/(?P<pk>\d+)/detail/$', coreviews.LocationDetailView.as_view(), name='location_list'),
]