from django.urls import path

from . import views

urlpatterns = [
    path('<int:event_id>', views.event_details_view, name='event-details'),
    path('', views.event_list_view, name='event-list'),
]