from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import RiskListView, RiskDataView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = {
	url(r'^auth/', include('rest_framework.urls', namespace='rest_framework')),
	url(r'^risks/$', RiskListView.as_view(), name="risks"),
    url(r'^risks/(?P<pk>[0-9]+)/$', RiskDataView.as_view(), name='risk_data'),
    url(r'^obtain-token/', obtain_auth_token),
}

urlpatterns = format_suffix_patterns(urlpatterns)
