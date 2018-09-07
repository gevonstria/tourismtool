from django.conf.urls import url
from core.views import ChartsView

urlpatterns = [
    url(r'^charts$', ChartsView.as_view()),
]