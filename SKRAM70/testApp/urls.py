from django.urls import path
from django.conf.urls import url
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('CarInfo/<int:car_id>/', views.detail, name='detail'),
    path('create_account/', views.accounts, name='Accounts'),
    url(r'^search/$', views.search),
    path('staffPortal', views.staffPortal, name='staffPortal'),
    url(r'^staffPortal/vehicleReturns/$', views.returnPage),
    url('ContactUs', views.contactUs, name='contactUS'),
    path('successfulLogin', views.successfulLogin, name='successfulLogin'),
    path('editUser/', views.editUser, name = 'Edit'),
    path('Locations', views.LocationsView, name="Locations"),
    path('FrequentlyAskedQuestions', views.FAQView, name="FAQs"),
    path('RecommendCars', views.carRecomView, name="RecommendCars"),
    url(r'^staffPortal/CarPopularity/$', views.CarPopularityView),
    url(r'^favicon.ico$',
        RedirectView.as_view(
            url=staticfiles_storage.url('testApp/images/favicon.ico'),
        ),
        name="favicon"
    )
]
