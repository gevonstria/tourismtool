from django.conf.urls import url
from destinations.views import AdminDestinationsView

urlpatterns = [
    url(r'^$', AdminDestinationsView.as_view(), name="dashboard"),
]