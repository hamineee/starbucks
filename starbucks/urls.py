from django.urls import path
from starbucks.views import StarbucksView

urlpatterns=[
    path('', StarbucksView.as_view())
]