from . import views
from django.urls import path


urlpatterns = [
    path('to-mandarin/', views.Translate.as_view())
]

