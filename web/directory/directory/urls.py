# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from directory.views import IndexView

urls = [
    url(r'^$', IndexView.as_view(), name=IndexView.view_name)
]

# use staticfiles with gunicorn (not recommneded!)
# TODO: switch to a real static file handler
urls += (
    static(settings.STATIC_URL, document_root=settings.STATIC_ROOT))
if settings.DEBUG:
    # add debug toolbar
    import debug_toolbar  # pragma: no cover

    urls += [  # pragma: no cover
        url(r"^__debug__/", include(debug_toolbar.urls)),  # pragma: no cover
    ]

urlpatterns = urls
