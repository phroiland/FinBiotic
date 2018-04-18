from django.conf.urls import url
from .views import TimeSeriesView

app_name = 'data'
urlpatterns = [
    url(r'^$', TimeSeriesView.as_view())
    ]
