
from django.contrib import admin
from django.urls import path
from post import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', views.hello_view),
    path('good_bye/', views.good_bye),
    path('current_date/', views.current_date),
    path('test/', views.test)
]
