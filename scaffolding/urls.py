"""(C) 2013-2024 Copycat Software, LLC. All Rights Reserved."""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import (
    include,
    path,
    re_path)
from django.views.generic.base import TemplateView


admin.autodiscover()


urlpatterns = [
    re_path(r"^admin/", admin.site.urls),
    re_path(r"^app/", include("app.urls")),
    re_path(r"^api/", include("api.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler400 = "app.views.handler400"
handler403 = "app.views.handler403"
handler404 = "app.views.handler404"
handler500 = "app.views.handler500"
