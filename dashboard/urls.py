from django.conf.urls import url
from dashboard.views import AdminDashboardView

urlpatterns = [
	url(r'^$', AdminDashboardView.as_view(), name="dashboard"),
]