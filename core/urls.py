from django.conf.urls import url
from core.views import ChartsView, FormsView

urlpatterns = [
    url(r'^charts$', ChartsView.as_view()),
    url(r'^forms$', FormsView.as_view()),
]