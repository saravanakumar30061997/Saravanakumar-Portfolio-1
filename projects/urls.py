from django.urls import path
from . import views
app_name = 'projects'

urlpatterns=[
    path("",views.index,name='pro'),
    path('<int:proid>/',views.detail,name='pro-detail')
]