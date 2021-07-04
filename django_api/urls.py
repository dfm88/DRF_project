
from django.contrib import admin
from django.urls import path
from test_app.views import Simple, SimpleGenericsUpdate, SimpleGenerics

urlpatterns = [
    path('admin/', admin.site.urls),
    path('simple/', Simple.as_view()),
    path('simple/<int:id>', Simple.as_view()),
    path('simple-generics', SimpleGenerics.as_view()),
    path('simple-generics/<int:id>', SimpleGenericsUpdate.as_view()),

]
