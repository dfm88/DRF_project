
from django.contrib import admin
from django.urls import path, include
# from test_app.views import Simple, SimpleGenericsUpdate, SimpleGenerics
from test_app.views import SimpleViewSet

from rest_framework.routers import DefaultRouter
from django.conf import settings

router = DefaultRouter()
router.register('simple-viewset', SimpleViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('simple/', Simple.as_view()),
    # path('simple/<int:id>', Simple.as_view()),
    # path('simple-generics', SimpleGenerics.as_view()),
    # path('simple-generics/<int:id>', SimpleGenericsUpdate.as_view()),
    path('', include(router.urls))
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls))
    ]
