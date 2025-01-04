from django.urls import path
from . import views

urlpatterns = [
    path('fund-types/', views.fund_type_view, name='fund_types'),
]