from django.urls import path, include, reverse
from django.http import HttpResponseRedirect

from django.contrib import admin


def redirect_to_login_view(request):
    return HttpResponseRedirect(reverse('login'))


admin.autodiscover()

urlpatterns = [
    path("", redirect_to_login_view),
    path("login/", include("login.urls")),
    path("admin/", admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
]
