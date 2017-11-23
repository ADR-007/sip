# dlyapun

from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import TemplateView
from django.views.generic.base import RedirectView
from rest_framework import routers
from rest_framework.authtoken import views as authviews
from core import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name="index.html")),
    url(r'^', include('core.urls')),
    url(r'^api/', include(router.urls)),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/authenticate$', authviews.obtain_auth_token),
    url(r'^admin/', admin.site.urls),
    url(r'^sip/', include('sip.urls'))
]

if settings.DEBUG:
    urlpatterns += [] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += [] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    import debug_toolbar

    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]

urlpatterns += staticfiles_urlpatterns()
