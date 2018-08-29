from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^cbv/$',views.DefaultHeaderContextDjangoBetterCustomClassView.as_view(),name='cbv')
]